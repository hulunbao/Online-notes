from django.shortcuts import render
from .models import Topic

def index(request):
    """学习笔记主页"""
    return render(request,'online_notes/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'online_notes/topics.html',context)

def topic(request,topic_id):
    """显示主题对应的内容"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries}
    return render(request,'online_notes/topic.html',context)
