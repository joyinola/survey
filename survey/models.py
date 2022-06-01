
from django.db import models
from django.forms import CharField, IntegerField, URLField

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
        prev_gen=Generation.objects.filter(is_active=False).last()
        gen=Generation.objects.filter(is_active=True).last()
        if gen.name=='Generation 1':
            return 0

        else:
            return Vote.objects.filter(headline=self.id,vote='Upvote',generation=prev_gen).count()
   
            
    @property
    def downVotes(self):
        prev_gen=Generation.objects.filter(is_active=False).last()
        gen=Generation.objects.filter(is_active=True).last()
        if gen.name=='Generation 1':
            return 0
            
        else:
            return Vote.objects.filter(headline=self.id,vote='Downvote',generation=prev_gen).count()
            
            
    

    def __str__(self):
        try:
            upvote=self.upVotes()
        except:
            upvote=0
        try:
            downvote=self.downVotes()
        except:
            downvote=0

        return f'{self.headLine} upvote{upvote} downvote{downvote}'
class Generation(models.Model):
    name=models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)

    class Meta:
        ordering=['date_added',]

    def __str__(self):
        return self.name
   
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

