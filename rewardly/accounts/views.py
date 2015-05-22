from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, resolve_url

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import ugettext as _

from django.db.models import Q
from accounts.models import UserProfile,UserGroup, ScoreHistory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.http import int_to_base36
from django.core.mail import send_mail
import hashlib,datetime, random
from django.utils import timezone
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, get_user_model, update_session_auth_hash)

from django.template.response import TemplateResponse
from django.utils.http import is_safe_url

from django.contrib.auth.models import User
import requests
import ast
import json
import math
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def generateDates():
	transaction_year = 2010 + int(math.floor(random.random()*5))
	transaction_month = 1 + int(math.floor(random.random()*12))
	transaction_day = 1 + int(math.floor(random.random()*28))
	return (str(transaction_year) + str(transaction_month) + str(transaction_day))

def depAmounts():
	amount = 2000*random.random()
	return amount

def generateAndStoreData(request):
    deposits=[]
    for i in range(100):
        deposits.append({})
        deposits[i]['date'] = generateDates()
        deposits[i]['value'] = depAmounts()


    deposits.sort(key=lambda d:d['date'])
    request.session['deposits']=deposits

    scores = [random.random()*50 for i in range(50)]
    request.session['scores']=scores

    persona={
        'points':int(random.random()*50),
        'name':'Himanshu Ojha'
    }
    personb={
        'points':int(random.random()*50),
        'name':'Mark Cuban'
    }
    personc={
        'points':int(random.random()*50),
        'name':'George Smith'
    }
    persond={
        'points':int(random.random()*50),
        'name':'John Smith'
    }
    persone={
        'points':int(random.random()*50),
        'name':'Alan Smith'
    }
    personf={
        'points':int(random.random()*50),
        'name':'Richard Why'
    }

    group = [persona, personb, personc, persond, persone, personf]
    group.sort(key=lambda g: g['points'], reverse=True)
    group =group[:6]
    request.session['group']=group

    this_months_budget = 2500+random.random()*4000
    request.session['this_months_budget']=int(this_months_budget)

    request.session['this_months_spending']=int(this_months_budget*random.random())
    request.session['last_months_spending']=int(this_months_budget*(random.random()+.2))

    rewards = int(800+100*random.random())
    request.session['rewards']=rewards



def home(request):
    return render(request, 'index.html')

@sensitive_post_parameters()
@csrf_protect
@never_cache
def register(request, creation_form=UserCreationForm, extra_context=None):
    form = creation_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            if not request.POST.get("email"):
                error = "The email field is required!"
                return render(request, "myregistration/register.html", {'message': error})
            user = form.save();
            email = request.POST.get("email")
            user.email = email
            customer_id = request.POST.get("customer_id")
            user.customer_id = customer_id
            api_key = request.POST.get("api_key")
            user.api_key = api_key
            user.save()
            UserProfile.objects.create(user=user, customer_id=customer_id,api_key=api_key)
            profile = UserProfile.objects.get(user=user)
            url = 'http://api.reimaginebanking.com:8080/customers/{}/accounts?key={}'.format(profile.customer_id, profile.api_key)
            req = requests.get(url)
            # account_id = ast.literal_eval(req.content)[0]['_id']
            url = 'http://api.reimaginebanking.com:8080/accounts/{}?key={}'.format("5", profile.api_key)
            req = requests.get(url)
            # rewards = ast.literal_eval(req.content)['rewards']
            #return HttpResponseRedirect(reverse('dashboard', kwargs={'rewards': rewards}))

            generateAndStoreData(request)

            return redirect('dashboard')

    context = {
    'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, "register/register.html", context)

@csrf_protect
def login(request):
    #redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)

                #return HttpResponseRedirect(reverse('dashboard', kwargs={'rewards': rewards}))

                if 'group' not in request.session:
                    generateAndStoreData(request)
                return redirect('dashboard')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


@csrf_exempt
def get_all_data(request):
    data = {}
    vals = ['deposits','scores','group','rewards','this_months_budget','this_months_spending','last_months_spending']
    for i in vals:
        data[i]=request.session[i]
    return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def dashboard(request):
    user = request.user
    # profile = UserProfile.objects.get(user=user)
    # url = 'http://api.reimaginebanking.com:8080/customers/{}/accounts?key={}'.format(profile.customer_id, profile.api_key)
    # req = requests.get(url)

    # account_id = json.loads(req.content.decode('utf','ignore'))[0]['_id']
    # url = 'http://api.reimaginebanking.com:8080/accounts/{}?key={}'.format(account_id, profile.api_key)
    # req = requests.get(url)
    # rewards = json.loads(req.content.decode('utf','ignore'))['rewards']
    #
    # url="http://api.reimaginebanking.com:8080/accounts/{}/deposits?key={}".format(profile.customer_id,profile.api_key)
    # req = requests.get(url)
    # deposits = json.loads(req.content.decode('utf','ignore'))

    if 'group' not in request.session:
        generateAndStoreData(request)

    return render_to_response('dashboard.html',{
        'group':request.session['group'],
        'rewards': request.session['rewards'],
        'user': user,
        'deposits_recent':request.session['deposits'],
        'scores':request.session['scores'],
        'last_months_spending_score':request.session['scores'],
        'last_months_spending_dollar':request.session['scores'][25]*request.session['deposits'][0]['value'],
        'this_months_budget':request.session['this_months_budget'],
        'this_months_spending': request.session['this_months_spending'],
        'last_months_spending':request.session['last_months_spending']
    })


@login_required(login_url='/accounts/login/')
def rewards(request):
    return render_to_response('rewards.html')

@login_required(login_url='/accounts/login/')
def logout(request):
    auth_logout(request)

    return HttpResponseRedirect('/')
