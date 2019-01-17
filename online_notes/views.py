from django.shortcuts import render

def index(request):
    """学习笔记主页"""
    return render(request,'online_notes/index.html')
