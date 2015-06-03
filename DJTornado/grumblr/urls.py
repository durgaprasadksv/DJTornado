from django.conf.urls import patterns, include, url
from forms import *
# Generates the routes for the Controller.
# Typical use is a regular expression for a URL pattern, and then the
# action to call to process requests for that URL pattern.
urlpatterns = patterns('',
    url(r'^$', 'grumblr.views.home'),
    # Route for built-in authentication with our own custom login page
    url(r'^login', 'django.contrib.auth.views.login', {'template_name':'grumblr/login.html','authentication_form': LoginForm,
         'extra_context':{'new_user_form':CreateUserForm}}, name='login'),
    url(r'^register$', 'grumblr.views.register'),
    url(r'^grumbl$', 'grumblr.views.grumbl'), # post a grumbl
    url(r'^profile$', 'grumblr.views.profile'), # view my grumbls
    url(r'^updateprofile$', 'grumblr.views.updateprofile'), # view my grumbls
    url(r'^delete-grumbl/(?P<id>\d+)$', 'grumblr.views.delete_grumbl'),
    url(r'^search$', 'grumblr.views.search'),
    url(r'^forgotpass', 'grumblr.views.forgotpassword'),
    url(r'^changepass', 'django.contrib.auth.views.password_change'),
)

