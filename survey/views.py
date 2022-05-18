
import re
import uuid
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import HeadLines,Vote, Utilizer
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json  
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    return render(request, 'survey/surveypage.html') 

def updateUser(request,id):
        user,status= Utilizer.objects.get_or_create(prolificId=id)

        x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip=x_forwarded_for.split(',')[0]
        else:
            ip=request.META.get('REMOTE_ADDR')
        user.ipAddress=ip
        user.save()

        response=JsonResponse('success', safe=False)
        if ('userid' in request.COOKIES):
            if request.COOKIES['userid']==id:
                pass
            else:
                response.delete_cookie('userid')
                response.set_cookie('userid',id,max_age=360000000)
                return response
        else:
            response.set_cookie('userid',id,max_age=360000000)
        return response


def taskverify(request,data):
    user=Utilizer.objects.get(prolificId=request.COOKIES['userid']) 
    data=data.replace('"',"",4)
    data=data.strip('][ ').split(',')
    headline=HeadLines.objects.get(id=int(data[0]))
    
    try:
        vote=Vote.objects.get(headline=headline,user=user)
        status='true'
    except:
        status='false'


    # for i in headlines:
    #     try:
    #         upvote=Vote.objects.get(user=user,headline=i,vote='Upvote')
    
    #     except ObjectDoesNotExist:
    #         upvote=False

    #     try:  
    #         downvote=Vote.objects.get(user=user,headline=i,vote='Downvote')

    #     except ObjectDoesNotExist:
    #         downvote=False

    #     if upvote==False and downvote==False:
    #         status='false'

    return JsonResponse(status, safe=False)
@csrf_exempt
def info(request):
    if request.method=="POST":
        data=json.loads(request.body)
        user=Utilizer.objects.get(prolificId=request.COOKIES['userid'])
        user.age=data['userInfo']['age']
        user.qualification=data['userInfo']['qualifications']
        user.gender=data['userInfo']['gender']
        user.politicalInterest=data['userInfo']['interest']
        user.presidentialCandidate=data['userInfo']['candidate']
        user.party=data['userInfo']['republican']
        myuuid=uuid.uuid4()
        if not user.confirmationCode:
            user.confirmationCode=myuuid
        user.save()

        return JsonResponse(user.confirmationCode, safe=False)

    return render(request, 'survey/info.html')


@csrf_exempt
def vote(request,num:str,vote:str):
    if request.method=='POST':
        data=json.loads(request.body)
        obj=HeadLines.objects.get(id=int(num))
        user,created=Utilizer.objects.get_or_create(prolificId=request.COOKIES['userid'])
        if len(data['infoHeadline']) == 1:
            if vote=='upvote':
                try:
                    voted=Vote.objects.get(user=user,headline=obj,vote='Downvote')
                except:
                    voted=None

                if (voted):
                    voted.delete()
                Vote.objects.get_or_create(user=user,headline=obj,vote='Upvote')

            else:
                try:
                    voted=Vote.objects.get(user=user,headline=obj,vote='Upvote')
                except:
                    voted=None
                if (voted):
                    voted.delete()
                Vote.objects.get_or_create(user=user,headline=obj,vote='Downvote')
            return JsonResponse('success',safe=False)
        else:
            obj1=HeadLines.objects.get(id=int(data['infoHeadline'][0]))
            obj2=HeadLines.objects.get(id=int(data['infoHeadline'][1]))
     
            if data['infoHeadline'][0]==num:
                if vote=='upvote':
                    try:
                        voted=Vote.objects.get(user=user,headline=obj1,vote='Downvote')
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj1,vote='Upvote')

                    try:
                        voted=Vote.objects.get(user=user,headline=obj2,vote='Upvote')
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj2,vote='Downvote')
                else:
                    try:
                        voted=Vote.objects.get(user=user,headline=obj1,vote='Upvote')
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj1,vote='Downvote')

                    try:
                        voted=Vote.objects.get(user=user,headline=obj2,vote='Downvote')
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj2,vote='Upvote')
                return JsonResponse('success', safe=False)

            else:
                if vote=='upvote':
                    try:
                        voted=Vote.objects.get(user=user,headline=obj2,vote='Downvote')
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj2,vote='Upvote')
            
                    try:
                        voted=Vote.objects.get(user=user,headline=obj1,vote='Upvote')
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj1,vote='Downvote')
                else:
                    try:
                        voted=Vote.objects.get(user=user,headline=obj2,vote='Upvote')
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj2,vote='Downvote')
                    try:
                        voted=DownVote.objects.get(user=user,headline=obj1)
                    except:
                        voted=None
                    if (voted):
                        voted.delete()
                    Vote.objects.get_or_create(user=user,headline=obj1,vote='Upvote')
                return JsonResponse('success',safe=False)
def voteCasted(request,data):
    # data='[1,2]'
    user=Utilizer.objects.get(prolificId=request.COOKIES['userid']) 
    status={}
    data=data.replace('"',"",4)
    data=data.strip('][ ').split(',')
   
    if len(data)==1:
        try:
            news=HeadLines.objects.get(id=int(data[0]))
            check=Vote.objects.get(user=user,headline=news)
            if check:
                status[f'{news.id}']=check.vote
        except:
            pass

    elif len(data)==2:
        try:
            news1=HeadLines.objects.get(id=int(data[0]))
            news2=HeadLines.objects.get(id=int(data[1]))
            check1=Vote.objects.get(user=user,headline=news1)
            if check1:
                status[f'{news1.id}']=check1.vote
            check2=Vote.objects.get(user=user,headline=news2)
            if check2:
                status[f'{news2.id}']=check2.vote
        except:
            pass
    return JsonResponse(status)





def updateHeadline(request,num):
    headlines=HeadLines.objects.all()
    p=Paginator(headlines,2)
    try:
        pag=p.page(int(num))
    except PageNotAnInteger:
        pag=p.page(1)
    except EmptyPage:
        pag=p.page(p.num_pages)

    return render(request, 'survey/headline.html',{'p':pag}) 