from django.shortcuts import render
from allauth.socialaccounts.models import ScoialAccount
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

def index(request):
    context = {}
    if request.user.is_authenticated:
        context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
    return render(request, "index.html", context)

# Create your views here.
