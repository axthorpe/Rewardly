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
from accounts.models import UserProfile
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
            profile = UserProfile(user=user)
            username = form.cleaned_data['username']
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            profile.suspended = False
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            auth_login(request, user)
            return HttpResponseRedirect('/')

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
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
