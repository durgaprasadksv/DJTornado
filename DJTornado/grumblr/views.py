from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login


from models import *
from forms import *
# Create your views here.

def defaultroute(request):
    context = {}
    if request.user.is_authenticated():
        return home(request)
    else:
        context['registerform'] = CreateUserForm()
        return render(request, 'grumblr/signup.html', context)

def register(request):

    context = {}
    if request.method == 'GET':
        context['registerform'] = CreateUserForm()
        return render(request, 'grumblr/signup.html', context)

    
    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    registerform = CreateUserForm(request.POST)
    context['registerform'] = registerform
    # Validates the form.
    if not registerform.is_valid():
        return render(request, 'grumblr/signup.html', context)

    # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password1'],
                                        email=request.POST['email'],
                                        first_name=request.POST['first_name'],
                                     last_name=request.POST['last_name'])
    
    new_user.save()
    user = GrumblrUser(user=new_user, aboutme='about_me_newuser')
    user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=request.POST['username'], password=request.POST['password1'],
                            email=request.POST['email'])
    login(request, new_user)
    return redirect('/grumblr/')
    
def forgotpassword(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'grumblr/changepass.html', context)
    else:
        return render(request, 'grumblr/launch.html', context)

@login_required
def updateprofile(request):

    context = {}
    if request.method == 'GET':
        grumbls = Grumbl.objects.all().filter(user=request.user)
        return render(request, 'grumblr/editprofile.html', {'grumbls':grumbls})

    errors = {}
    context['errors'] = errors

    if not 'username' in request.POST or not request.POST['username']:
        #some malicious user
        return render(request, 'grumblr/')

    #not that the username we received from request and the user name we have must match.

    if not 'email' in request.POST or not request.POST['email']:
        errors['email'] = '* Email is required.'
    else:
        context['email'] = request.POST['email']


    if errors:
        return render(request, '/grumblr/launch.html', context)


    firstname =''
    lastname=''

    if not 'firstname' in request.POST or not request.POST['firstname']:
        firstname = ''
    else:
        firstname = request.POST['firstname']


    if not 'lastname' in request.POST or not request.POST['lastname']:
        lastname = ''
    else:
        lastname = request.POST['lastname']

    # Update the users profile
    updated_user = User.objects.filter(username=request.POST['username']).update(
                                        email=request.POST['email'],
                                        first_name= firstname, last_name=lastname)

    return redirect('/grumblr/')

def routelogin(request):

    context = {}
    if request.method == 'GET':
        context['registerform'] = CreateUserForm()
        return render(request, 'grumblr/launch.html', context)

    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/grumblr')
                 # Redirect to a success page.
            else:
                return redirect('/grumblr')
        else:
            return redirect('/grumblr')
               

@login_required
def home(request):
    # Sets up list of just the logged-in user's (request.user's) items
    grumbls = Grumbl.objects.all().exclude(user=request.user)
    return render(request, 'grumblr/index.html', {'grumbls':grumbls})

@login_required
def profile(request):
    # Sets up list of just the logged-in user's (request.user's) items
    grumbls = Grumbl.objects.all().filter(user=request.user)
    return render(request, 'grumblr/index.html', {'grumbls':grumbls})

@login_required
def search(request):

    if not 'search' in request.GET or not request.GET['search']:
        return render(request, 'grumblr/')
    else:
        grumbls = Grumbl.objects.filter(text__contains=request.GET['search'])
    return render(request, 'grumblr/index.html', {'grumbls':grumbls})

@login_required
def grumbl(request):

    context={}
    if not 'grumbl' in request.POST or not request.POST['grumbl']:
        context['grumbl_error'] = '* No Message posted or length is zero'
    elif len(request.POST['grumbl']) > 42:
        context['grumbl_error'] = "* Grumbl length exceeded"

    else:
        new_grumbl = Grumbl(text=request.POST['grumbl'], user=request.user)
        new_grumbl.save()
        context['grumbl_error'] = "Successfully posted !!"

    grumbls = Grumbl.objects.all().exclude(user=request.user)
    context['grumbls'] = grumbls
    return render(request, 'grumblr/index.html', context)


@login_required
def feedrefresh(request):
    context={}
    return render(request, 'grumblr/index.html', context)


@login_required
def delete_grumbl(request, id):
    errors = []

    # Deletes item if the logged-in user has an item matching the id
    try:
        grumbl_to_delete = Grumbl.objects.get(id=id, user=request.user)
        grumbl_to_delete.delete()
    except ObjectDoesNotExist:
        errors.append('This Grumbl cannot be deleted by you')

    grumbls = Grumbl.objects.filter(user=request.user)
    context = {'grumbls' : grumbls, 'errors' : errors}
    return render(request, 'grumblr/editprofile.html', context)






