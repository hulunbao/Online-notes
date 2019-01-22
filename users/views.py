from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('online_notes:index'))
