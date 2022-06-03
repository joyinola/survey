
from django.db import models
from django.forms import CharField, IntegerField, URLField
from django.db.models import Q
from django.core.exceptions import ValidationError

# Create your models here.
Gender=[
    ('Female','Female'),
    ('Male','Male'),
    ('Other','Other')
]

Age=[
    ('Less than 20','Less than 20'),
    ('20-35','20-35'),
    ('36-45','36-45'),
    ('Above 45','Above 45')
]
Qualification=[
    ('Less than High School','Less than High School'),
    ('High School','High School'),
    ('College Degree','College Degree'),
    ('Doctorate Degree','Doctorate Degree'),
    ('PhD holder','PhD holder')
]
Interest=[
("Not at all Interested","Not at all Interested"),
("Not very Interested","Not very Interested"),
("Somewhat Interested","Somewhat Interested"),
("Very Interested","Very Interested")]

Party=[
("Strong Republican","Strong Republican"),
("Not Strong Republican","Not Strong Republican"),
("Lean Republican","Lean Republican"),
("Independent","Independent"),
("Lean Democrat","Lean Democrat"),
("Not Strong Democrat","Not Strong Democrat"),
("Strong Democrat","Strong Democrat")]

Candidate=[
("Joe Biden","Joe Biden"),
("Donald Trump","Donald Trump"),
("Someone Else","Someone Else"),
("I didn't vote","I didn't vote")]

VoteValue=[
("Upvote","Upvote"),
("Downvote","Downvote")]

class HeadLines(models.Model):
    headLine=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    img=models.ImageField(upload_to="images/",null=True,blank=True)
    
    @property
    def upVotes(self):
        gen=Generation.objects.filter(is_active=True).last()
        if gen.name=='Generation 1' :
            return 0
        else:
            bfr_prev_gen=Generation.objects.filter(Q(id__lt=gen.id),Q(id__gte=first_gen.id))
            vote_cnt=0
            for i in bfr_prev_gen:
                vote_cnt+=Vote.objects.filter(headline=self.id,vote='Upvote',generation=i).count()
            return vote_cnt
        # gen=Generation.objects.filter(is_active=True).last()
        # first_gen=Generation.objects.all().first()
        # prev_gen=gen.prev_gen
        # if gen.name=='Generation 1' :
        #     return 0

        # else:
        #     bfr_prev_gen=Generation.objects.filter(Q(id__lte=prev_gen.id),id__gte=first_gen.id)
        #     vote_cnt=0
        #     for i in bfr_prev_gen:
        #         vote_cnt+=Vote.objects.filter(headline=self.id,vote='Upvote',generation=i).count()
        #     return vote_cnt
   
            
    @property
    def downVotes(self):
        
        gen=Generation.objects.filter(is_active=True).last()
        if gen.name=='Generation 1' :
            return 0
        else:
            bfr_prev_gen=Generation.objects.filter(Q(id__lt=gen.id),Q(id__gte=first_gen.id))
            vote_cnt=0
            for i in bfr_prev_gen:
                vote_cnt+=Vote.objects.filter(headline=self.id,vote='Downvote',generation=i).count()
            return vote_cnt
    def upvote_total(self):
        return Vote.objects.filter(headline=self,vote='Upvote').count()   
    def downvote_total(self):
        return Vote.objects.filters(headline=self.vote,vote='Downvote').count()

            
            
    

    def __str__(self):
        try:
            upvote=self.upvote_total()
        except:
            upvote=0
        try:
            downvote=self.downvote_total()
        except:
            downvote=0

        return f'{self.headLine} upvote{upvote} downvote{downvote}'
# def get_prev_gen():
#     pass
        # gen=Generation.objects.filter(is_active=True).last()
        # prev_gen=Generation.objects.filter(is_active=False,date_added__lt=gen.date_added).last()
        # return prev_gen
class Generation(models.Model):
    name=models.CharField(max_length=255,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    # prev_gen=models.ForeignKey('self',default=get_prev_gen(),on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering=['date_added',]

    def __str__(self):
        return f'{self.name} is_active:{self.is_active}'
    # def save(self,*args,**kwargs):
    #     if self.is_active:
    #         if Generation.objects.filter(Q(is_active=True),~Q(id=self.id)):

    #             raise ValidationError('An active generation already exists')
    #     return super(Generation,self).save(*args,**kwargs)
# def get_prev_gen():
#         gen=Generation.objects.filter(is_active=True).last()
#         prev_gen=Generation.objects.filter(is_active=False,date_added__lt=gen.date_added).last()
#         return prev_gen
   
class Utilizer(models.Model):
    prolificId=models.CharField(max_length=100)
    generation=models.ForeignKey(Generation,on_delete=models.CASCADE,blank=True,null=True)
    gender=models.CharField(choices=Gender, max_length=50)
    age=models.CharField(choices=Age,max_length=50)
    puceTest=models.CharField(max_length=100,null=True,blank=True)
    ipAddress=models.CharField(max_length=250)
    qualification=models.CharField(choices=Qualification,max_length=50)
    confirmationCode=models.CharField(max_length=100,null=True)
    politicalInterest=models.CharField(choices=Interest,max_length=50,null=True)
    party=models.CharField(choices=Party,max_length=50,null=True)
    presidentialCandidate=models.CharField(choices=Candidate,max_length=50,null=True)
    def __str__(self):
        return self.prolificId

class Vote(models.Model):
    user=models.ForeignKey(Utilizer,on_delete=models.SET_NULL,null=True)
    headline=models.ForeignKey(HeadLines,on_delete=models.CASCADE)
    vote=models.CharField(choices=VoteValue,max_length=20)
    generation=models.ForeignKey(Generation,on_delete=models.CASCADE,blank=True,null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True,null=True)

