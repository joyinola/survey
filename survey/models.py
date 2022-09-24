
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


Qualification=[
    ('Less than High School','Less than High School'),
    ('High School','High School'),
    ('Bachelor Degree','Bachelor Degree'),
    ('Masters Degree','Masters Degree'),
    ('Doctorate Degree','Doctorate Degree')
    
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

class Headline(models.Model):
    headLine=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    img=models.ImageField(upload_to="images/",null=True,blank=True)
    topic=models.CharField(max_length=100,null=True,blank=True)
    
    @property
    def upVotes(self):
        gen=Generation.objects.filter(is_active=True).last()
        first_gen=Generation.objects.all().order_by('date_added').first()
        if gen.name=='Generation 1' :
            return 0
        else:
            bfr_prev_gen=Generation.objects.filter(Q(id__lt=gen.id),Q(id__gte=first_gen.id))
            vote_cnt=0
            for i in bfr_prev_gen:
                vote_cnt+=Vote.objects.filter(headline=self.id,vote='Upvote',generation=i).count()
            return vote_cnt

            
    @property
    def downVotes(self):
        
        gen=Generation.objects.filter(is_active=True).last()
        first_gen=Generation.objects.all().order_by('date_added').first()
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
        return Vote.objects.filter(headline=self,vote='Downvote').count()

   
            
    

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

class Generation(models.Model):
    name=models.CharField(max_length=255,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
  

    class Meta:
        ordering=['date_added',]

    def __str__(self):
        return f'{self.name} is_active:{self.is_active}'

class Utilizer(models.Model):
    prolificId=models.CharField(max_length=100)
    generation=models.ForeignKey(Generation,on_delete=models.CASCADE,blank=True,null=True)
    gender=models.CharField(choices=Gender, max_length=50)
    age=models.CharField(max_length=50)
    puceTest=models.CharField(max_length=100,null=True,blank=True)
    ipAddress=models.CharField(max_length=250)
    qualification=models.CharField(choices=Qualification,max_length=50)
    confirmationCode=models.CharField(max_length=100,null=True)
    politicalInterest=models.CharField(choices=Interest,max_length=50,null=True)
    party=models.CharField(choices=Party,max_length=50,null=True)
    presidentialCandidate=models.CharField(choices=Candidate,max_length=50,null=True)
    def __str__(self):
        return self.prolificId

    def is_fully_filled(self):
        instance_fields=[f.name for f in self._meta.get_fields()]
        # print(self._meta.get_fields())

        for j in instance_fields:
            try:
                value=getattr(self,j)
                # print(value)
            except AttributeError:
                continue
            if value is None or value=='':
                return False
        return True
    def voted_completely(self):
        headlines=Headline.objects.all().count()
        user_vote_count=Vote.objects.filter(user=self).count()
        if user_vote_count==headlines/2:
            return True
        else:
            return False
    
    def clear_vote(self):
        Vote.objects.filter(user=self).delete()
class Vote(models.Model):
    user=models.ForeignKey(Utilizer,on_delete=models.SET_NULL,null=True)
    headline=models.ForeignKey(Headline,on_delete=models.CASCADE)
    vote=models.CharField(choices=VoteValue,max_length=20)
    generation=models.ForeignKey(Generation,on_delete=models.CASCADE,blank=True,null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True,null=True)
    

    def __str__(self):
        return f'{self.user} voted {self.vote} on {self.headline}'

