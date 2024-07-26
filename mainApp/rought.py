# def question(Request,id):
#     # examname

#     # questions = Questionpaper.objects.filter(nameofexam__id=id)   # __ ka mtlb hai ki jaha se yah foream key aarhi h 
#     subject = ExamPaper.objects.get(id=id)
#     subjectname= ExamPaper.objects.get(examname=subject.examname)
#     questions = Questionpaper.objects.filter(nameofexam=subject)
#     user = Request.user
#     student=Student.objects.get(username = user.username )
#     result = Result(username=student,examname=subjectname,date=datetime.date.today())
#     rightans= 0
#     worngans =0 
#     # questions = Questionpaper.objects.filter(nameofexam__examname=examname)
#     # ques = questions.question.all()
#     # right_opt = {}

#     if Request.method =="POST":
#         # qusid=Request.POST.get("question_id")
#         for question in questions:
#             answer=Request.POST.get(f'option{question.id}')
#             if answer== question.rigthopt:
#                 rightans += 1
#             else:
#                 worngans += 1 
#     result.right = rightans
#     result.wrong = worngans
#     result.point = rightans * 5
#     result.save()
       
            
#     context={"questions":questions,"subject":subject}
#     return render(Request,"question.html",context)

# def result(Request):
#     user = Request.user
#     result = Result.objects.get(username = user.username)
#     context={"result":result}
#     return render(Request,"result.html",context)





# def signuppage(Request):

#     if (Request.method == 'POST'):
#         # b= Buyer
#         # b.name = Request.POST.get("name")
        
#         password = Request.POST.get("password")
#         cpassword = Request.POST.get("cpassword")
#         if(password == cpassword):
#             username = Request.POST.get("username")
#             email = Request.POST.get("email")
#             name = Request.POST.get("name")
#             try:
#                 User.objects.create_user(username=username,email=email,password=password,first_name=name)

#                 phone = Request.POST.get("phone")

#                 b= Buyer()
#                 b.name=name
#                 b.email=email
#                 b.username = username
#                 b.phone = phone
#                 b.save()
#                 return HttpResponseRedirect('/login/')
#             except:
#                 error(Request,"UserName Already Taken !!!")
#         else:
#             error(Request, "Password and confirm password DoesN't Match ")

#     return render(Request,'signup.html')




# def loginpage(Request):
    # if(Request.method=="POST"):
    #     username= Request.POST.get("username")
    #     password= Request.POST.get("password")
    #     user = authenticate(username=username,password=password)
    #     if (user is not None):
    #         login(Request,user)

    #         if(user.is_superuser):
            
    #             return HttpResponseRedirect("/admin/")
    #         else:
    #             return HttpResponseRedirect("/profile/")
        
    #     else:
    #         error(Request,"Invalid Username or password ")
    # return render(Request,'login.html')