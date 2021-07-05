from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required



#This function is for Home Page.

def home(request):
  if request.user.is_authenticated:
    return render(request,'cse/home2.html')
  else:
    return render(request,'cse/home.html')


#This function is for Python Page.

already_done=[]
qno=0
@login_required(login_url='/signin/')
def python(request):
  import pandas as pd
  import random
  global qno
  
  
  search_post = request.GET.get('search')

  if search_post:
    posts = ExcelFile.objects.filter(Q(Question__icontains=search_post) & Q(Answer__icontains=search_post))
    return render(request,)
  else:
    posts = "No search found"
  df=pd.read_excel("cse\static\cse\csv\QUIZDATA.xlsx")
  mylist=random.sample(range(0,20),20)
  for item in mylist: 
    if item not in already_done: 
      Question=df.Question[item]
      Option_A=df.Option_A[item]
      Option_B=df.Option_B[item]
      Option_C=df.Option_C[item]
      Option_D=df.Option_D[item]
      Answer=df.Answer[item]
      qno+=1  
      params={
            "Question":Question,
            "Option_A":Option_A,
            "Option_B":Option_B,
            "Option_C":Option_C,
            "Option_D":Option_D,
            "Answer":Answer,
            "Qno":qno,
            "post":posts,
            
            
            }
      already_done.append(item) 
      btnvalue1 = request.POST.get('submitbtnn') 
      return render(request,'cse/python.html',params)
    else:
      continue
  if qno==20:
      qno=0
      already_done.clear()
      return render(request,"cse/finished.html")

