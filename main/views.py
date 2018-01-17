from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.forms.models import model_to_dict

import json, math
import logging
import datetime
import csv
import sys
import utility
import os
import commands
import time
import traceback

from config import SELFLOCATION
from models import *
from forms import LoginForm

#---------Logger --------------#                                                                                                                                                                            
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler(SELFLOCATION + 'webserver_log.txt', mode='a', encoding=None, delay=False)
hdlr.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

@login_required
def index(request):
    return render(request, 'index.html', {})

@csrf_protect
def login(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    logger.info(username + " successfully logged in ")
                    return HttpResponseRedirect('/')
                else:
                    return render_to_response('login.html', RequestContext(request, {'form': form, 'error': False}))
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form, 'error': True}))
        else:
            return render_to_response('login.html', RequestContext(request, {'form': form}))
    else:
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form}))

@login_required
def logout_view(request):
    logger.info(request.user.username + " logged out ")
    logout(request)
    return HttpResponseRedirect('/')
