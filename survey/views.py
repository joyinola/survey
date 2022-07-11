from distutils.ccompiler import gen_lib_options
import uuid
import random
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect, render
from .models import HeadLines,Vote, Utilizer,Generation
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json  
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

    
def index(request):
    return render(request, 'survey/surveypage.html') 

def updateUser(request,id):
    user,status= Utilizer.objects.get_or_create(prolificId=id)
    try:
        gen=Generation.objects.filter(is_active=True).last()
        user.generation=gen
        user.save()
        gen='Gen Found'
    except:
        gen='Gen not found'


    x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip=x_forwarded_for.split(',')[0]
    else:
        ip=request.META.get('REMOTE_ADDR')
    user.ipAddress=ip
    user.save()

    response=JsonResponse(gen, safe=False)
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
    current_gen=Generation.objects.get(is_active=True)
    data=data.replace('"',"",4)
    data=data.strip('][ ').split(',')
    headline1=HeadLines.objects.get(id=int(data[0]))
    headline2=HeadLines.objects.get(id=int(data[1]))
    vote1=None
    vote2=None
    try:
        vote1=Vote.objects.get(headline=headline1,user=user,generation=current_gen)
        # status='true'
    except:
        pass
    try:
        vote2=Vote.objects.get(headline=headline2,user=user,generation=current_gen)
        # status='true'
    except:
        pass
    if vote1 or vote2:
        status='true'
    else:
        status='false'
    print(vote1,vote2)
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
        del request.COOKIES['userid']

        return JsonResponse(user.confirmationCode, safe=False)

    return render(request, 'survey/info.html')


@csrf_exempt
def vote(request,num:str,vote:str):
    if request.method=='POST':
        
        data=json.loads(request.body)
        obj=HeadLines.objects.get(id=int(num))
        gen=Generation.objects.filter(is_active=True).last()
        #comment data
        counts={}
        user,created=Utilizer.objects.get_or_create(prolificId=request.COOKIES['userid'])
        
        if len(data['infoHeadline']) == 1:
            if vote=='upvote':
                try:
                    voted=Vote.objects.get(user=user,headline=obj,vote='Downvote',generation=gen)
                except:
                    voted=None

                if (voted):
                    voted.delete()
                Vote.objects.get_or_create(user=user,headline=obj,vote='Upvote',generation=gen)

            else:
                try:
                    voted=Vote.objects.get(user=user,headline=obj,vote='Upvote',generation=gen)
                except:
                    voted=None
                if (voted):
                    voted.delete()
                Vote.objects.get_or_create(user=user,headline=obj,vote='Downvote',generation=gen)
            
            counts['count1']={'upvote':obj.upVotes,'downvote':obj.downVotes}
            #uncomment the next line
            # return JsonResponse('success',safe=False)
        else:
            obj1=HeadLines.objects.get(id=int(data['infoHeadline'][0]))
            obj2=HeadLines.objects.get(id=int(data['infoHeadline'][1]))
            
            if vote=='upvote':
                try:
                    voted=Vote.objects.get(user=user,headline=obj,vote='Downvote',generation=gen)
                except:
                    voted=None
                if (voted):
                    voted.delete()
                Vote.objects.get_or_create(user=user,headline=obj,vote='Upvote',generation=gen)
            else:
                try:
                    voted=Vote.objects.get(user=user,headline=obj,vote='Upvote',generation=gen)
                except:
                    voted=None
                if (voted):
                    voted.delete()
                Vote.objects.get_or_create(user=user,headline=obj,vote='Downvote',generation=gen)
            

            if data['infoHeadline'][0]==num:
                try:
                    voted=Vote.objects.get(user=user,headline=obj2,generation=gen)
                except:
                    voted=None
                if (voted):
                    voted.delete()
            else:
                try:
                    voted=Vote.objects.get(user=user,headline=obj1,generation=gen)
                except:
                    voted=None
                if (voted):
                    voted.delete()
        
            counts['count1']={'upvote':obj1.upVotes,'downvote':obj1.downVotes}
            counts['count2']={'upvote':obj2.upVotes,'downvote':obj2.downVotes}
       
    return JsonResponse(counts)
    

def voteCasted(request,data):
    # data='[1,2]'
    user=Utilizer.objects.get(prolificId=request.COOKIES['userid']) 
    status={}
    data=data.replace('"',"",4)
    data=data.strip('][ ').split(',')
    current_gen=Generation.objects.get(is_active=True)
   
    if len(data)==1:
        try:
            news=HeadLines.objects.get(id=int(data[0]))
            check=Vote.objects.get(user=user,headline=news,generation=current_gen)
            if check:
                status[f'{news.id}']=check.vote
        except:
            pass

    elif len(data)==2:
        try:
            news1=HeadLines.objects.get(id=int(data[0]))
            check1=Vote.objects.get(user=user,headline=news1,generation=current_gen)
            if check1:
                status[f'{news1.id}']=check1.vote
            
        except:
            pass
        try:
            news2=HeadLines.objects.get(id=int(data[1]))
            check2=Vote.objects.get(user=user,headline=news2,generation=current_gen)
            if check2:
                status[f'{news2.id}']=check2.vote
        except:
            pass

    print(status)
    return JsonResponse(status)
@csrf_exempt
def saveTest(request):
    if request.method=='POST':
        data=json.loads(request.body)
        user=Utilizer.objects.get(prolificId=request.COOKIES['userid'])
        user.puceTest=data['testInput']
        user.save()
        return JsonResponse(data,safe=True)
    else:
        return JsonResponse('false',safe=False)



def updateHeadline(request,num):
    if 'data' in request.session:
        data=request.session['data']
    else:
        query_set=HeadLines.objects.all()
        votes=[ {query.id:{"upvote":query.upVotes,"downvote":query.downVotes}} for query in query_set]
        query_set_values = HeadLines.objects.values()

        for record in votes:
            for query_value in query_set_values:
                if list(record.keys())[0] == query_value['id']:
                    query_value.update(record[list(record.keys())[0]])
        

        result_set = {}
        for row in query_set_values:
            if result_set.get(row["topic"]) is not None:
                result_set[row["topic"]].append(row)
            else:
                result_set[row["topic"]] = [row]

        topics = list(result_set.keys())
        random.shuffle(topics)

        data=[]
        for topic in topics:
            random.shuffle(result_set[topic])
            data.extend(result_set[topic][:2])
    
        for topic in topics:
            data.extend(result_set[topic][2:])
        request.session['data']=data
        request.session.set_expiry(0)
    # request.session.set_expiry(1)

    request.session.clear_expired()
    # print(data)
    # print(request.session['data'])
    p=Paginator(data,2)
    try:
        pag=p.page(int(num))
    except PageNotAnInteger:
        pag=p.page(1)
    except EmptyPage:
        pag=p.page(p.num_pages)
   
    return render(request, 'survey/headline.html',{'p':pag}) 
   