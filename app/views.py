from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=TOPIC.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic inserted')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['url']
        email=request.POST['email']
        RTO=TOPIC.objects.get(topic_name=tn)
        WO=WEBPAGE.objects.get_or_create(topic_name=RTO,name='na',url='url',email='email')[0]
        return HttpResponse('WEBPAGE INSERTED SUCESSFULLY')
    return render(request,'insert_webpage.html')