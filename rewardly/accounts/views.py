from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'index.html')

def register(request):
    # form = creation_form(request.POST or None)
    # if request.method == "POST":
    #     if form.is_valid():
    #         error = "The email field is required."
    #         return render(request, "register/register.html", {'message': error})
    #     user = form.save();
    #     email = request.POST.get("email")
    #     user.email = email
    #     user.save()
    #     profile = UserProfile(user=user)
    #     username = form.cleaned_data['username']
    #     random_string = str(random.random()).encode('utf8')
    #     salt = hashlib.sha1(random_string).hexdigest()[:5]
    #     salted = (salt + email).encode('utf8')
    #     activation_key = hashlib.sha1(salted).hexdigest()
    #     key_expires = datetime.datetime.today() + datetime.timedelta(2)
    #     profile.activation_key = activation_key
    #     profile.key_expires = key_expires
    #     if len(UserProfile.objects.all()) is 0:
    #         profile.administrator = 1
    #     profile.save()
    #     email_subject = "Account confirmation"
    #     email_body = "Hey %s, thanks for signing up. To activate your account, click this link within" \
    #                      "48hours http://%s/accounts/confirm/%s" % (username, get_current_site(request).domain, activation_key) % ""
    #
    #     return render(request, "myregistration/register_success.html")
    #

    return redirect('/')

def login(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('login.html',{'state':state, 'username': username})


def dashboard(request):
    persona = {
        'name':'himanshu',
        'points':5
    }


    group = [persona, persona, persona,persona,persona,persona,persona]
    group.sort(key=lambda p: p['points'])

    return render_to_response('dashboard.html',{'group':group[:6]})