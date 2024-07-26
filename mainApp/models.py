from django.db import models

# Create your models here.

class ExamPaper(models.Model):
    id= models.AutoField(primary_key=True)
    examname=models.CharField(max_length=50)
    examdisp = models.TextField()
    numofquestion = models.IntegerField()

    def __str__(self):
        return str(self.id)+" / "+self.examname

class Questionpaper(models.Model):
    id= models.AutoField(primary_key=True)
    nameofexam= models.ForeignKey(ExamPaper,on_delete=models.CASCADE)
    question = models.TextField()
    opt1=models.CharField(max_length=100)
    opt2=models.CharField(max_length=100)
    opt3=models.CharField(max_length=100)
    opt4=models.CharField(max_length=100)
    rigthopt = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)+" / "+str(self.nameofexam)+' / '+self.question



class Student(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=20,unique=True)
    sem = models.CharField(max_length=20)
    year= models.CharField(max_length=20)
    points=models.FloatField(null=True)
    def __str__(self):
        return str(self.id)+' / '+self.name+' / '+ self.username


    # test_attempted=models.IntegerField()
    #
class Result(models.Model):
    resultid=models.BigAutoField(primary_key=True,auto_created=True)
    username=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    examname=models.ForeignKey(ExamPaper,on_delete=models.CASCADE)
    # attempt=models.IntegerField()
    right=models.IntegerField()
    wrong=models.IntegerField()
    point=models.FloatField()
   



# from django.db import models
# class Candidate(models.Model):
#     username=models.CharField(primary_key=True,max_length=20)
#     password=models.CharField(null=False,max_length=20)
#     name=models.CharField(null=False,max_length=30)
#     test_attempted=models.IntegerField()
#     points=models.FloatField()

# class Question(models.Model):
#     qid=models.BigAutoField(primary_key=True,auto_created=True)
#     que=models.TextField()
#     a=models.CharField(max_length=255)
#     b=models.CharField(max_length=255)
#     c=models.CharField(max_length=255)
#     d=models.CharField(max_length=255)
#     ans=models.CharField(max_length=2)
# class Result(models.Model):
#     resultid=models.BigAutoField(primary_key=True,auto_created=True)
#     username=models.ForeignKey(Candidate,on_delete=models.CASCADE)
#     date=models.DateField(auto_now=True)
#     time=models.TimeField(auto_now=True)
#     attempt=models.IntegerField()
#     right=models.IntegerField()
#     wrong=models.IntegerField()
#     point=models.FloatField()
