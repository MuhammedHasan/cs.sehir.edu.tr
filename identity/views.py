from django.shortcuts import render, redirect
from oauth2client.client import OAuth2WebServerFlow
from django.core.urlresolvers import reverse
from django.conf import settings
from apiclient.discovery import build
from django.contrib.auth import login
from home.models import FacultyMember
import httplib2
from home.models import User


def login_redirect(request):
    flow = create_flow()
    return redirect(flow.step1_get_authorize_url())


def authenticate_user(request):
    if request.GET.get('error', '') == '':
        user_email = str()
        try:
            flow = create_flow()
            credentials = flow.step2_exchange(request.GET.get('code'))
            user_info_service = build(
                serviceName='oauth2',
                version='v2',
                http=credentials.authorize(httplib2.Http()))
            user_email = user_info_service.userinfo().get().execute()['email']
        except:
            return redirect(reverse('home:index'))
        if FacultyMember.objects.filter(email=user_email).count() > 0:
            # Do not delete admin user because i authorize every body with it
            # Look following line for that
            user = User.objects.filter(username='admin')[:1][0]
            # I am hacker
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect(reverse('admin:index'))
    return redirect(reverse('home:index'))


def create_flow():
    # update redirect_uri
    return OAuth2WebServerFlow(
        client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
        client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        scope=['email', 'profile'],
        redirect_uri='http://cs.sehir.edu.tr/identity/authenticate-user/')
