from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import datetime

from django.http import HttpResponseRedirect 
from mainApp.models import *
from django.contrib.auth.models import User 
from django.contrib.messages import error,success
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here
from django.contrib.auth.decorators import login_required

def homepage(Request):
  
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
# @login_required(login_url='login/')

@login_required(login_url='/ots/login/')
def studentprofile(Request):
    #  for gatting user from data base 
    student = Student.objects.get(username=Request.user.username)
    return render(Request,'studentprofile.html',{"student":student})

@login_required(login_url='/ots/login/')
def examSubject(Request):
    subject= ExamPaper.objects.all()

    return render(Request,'examsubject.html',{"subject":subject})

@login_required(login_url='/ots/login/')
def questionpaper(Request,id):
    subject = ExamPaper.objects.get(id=id)
    questions = Questionpaper.objects.filter(nameofexam=subject)
    context={"questions":questions,"subject":subject}
    return render(Request,"question.html",context)

   

@login_required(login_url='/ots/login/')
def resultpage(Request,id):
    subject=ExamPaper.objects.get(id=id)
    subjectname=ExamPaper.objects.get(examname = subject.examname)
    questions=Questionpaper.objects.filter(nameofexam = subject)
    user = Request.user
    student = Student.objects.get(username = user.username)
    result = Result(username=student,examname= subjectname,date=datetime.date.today())
    rightans=0
    wrongans=0
    for question in questions:
        answer=Request.POST.get(f'option{question.id}')
        if answer== question.rigthopt:
            rightans += 1
        else:
            wrongans += 1 
    result.right = rightans
    result.wrong = wrongans
    result.point = rightans * 5
    result.save()
    
    context={"result":result , "student":student}
    return render(Request,"result.html",context)



def signuppage(Request):
    if Request.method == "POST":
        password=Request.POST.get('password') 
        cpassword=Request.POST.get("cpassword")
        if password == cpassword:
            username = Request.POST.get("username")
            email = Request.POST.get("email")
            name = Request.POST.get("name")
            #  try for if user all ready regester
            try:  
            # User.objects.create_user(username=username,email=email,password=password,first_name=name)
                User.objects.create_user(username=username, password=password ,email=email,first_name=name)
                s = Student()
                s.name=name
                s.email=email
                s.username=username
                s.sem=Request.POST.get("sem")
                s.year=Request.POST.get("year")
                s.save()
                return HttpResponseRedirect('/ots/login/')
                
            except:
                error(Request,"UserName Already Taken !!!")
        else:
            error(Request, "Password and confirm password DoesN't Match ")

    # template = loader.get_template('signup.html')
    # return HttpResponse(template.render())
    return render(Request,"signup.html")



def loginpage(Request):
    if Request.method == 'POST' :
        username= Request.POST.get("username") 
        password=Request.POST.get("password")
        user= authenticate(username=username,password=password)

        if (user != None):
            login(Request,user)

            if(user.is_superuser):
                return HttpResponseRedirect('/admin')
            else:
                # pass
                # print()
                return HttpResponseRedirect('/ots/studentprofile/')
        else:
            error(Request,"Invalide Username or password !!!")
    return render(Request,"loginpage.html")


@login_required(login_url='/ots/login/')
def logoutpage(Request):
    logout(Request)
    return HttpResponseRedirect('/ots/')
    #   logout(request)
