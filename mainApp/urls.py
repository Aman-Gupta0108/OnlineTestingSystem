
from django.urls import path,include
from mainApp import views

urlpatterns = [
    path('',views.homepage),
    path('signup/',views.signuppage,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('studentprofile/',views.studentprofile,name='student'),
    path('examsub/',views.examSubject,name='examsubject'),
    
    path('paper/<int:id>/',views.questionpaper),
    
    path('result/<int:id>/',views.resultpage,name='result'),
    path('updateprofile/<int:id>/',views.updateProfilePage,name='updateProfile'),
]




    # path('paperpage/<int:id>/',views.question),
    # path('resultpage/',views.result,name='result'),