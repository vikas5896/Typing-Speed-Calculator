from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request , 'index.html')
  
def home(request):
    return render(request , 'index.html')

  

def signup(request):
    # return render(request , 'signup.html')

    if request.method == "POST":
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(email,pass1)
        myuser.first_name = fname 
        myuser.last_name = lname
        myuser.password = pass1

        myuser.save()

        messages.success(request,"you signed up thankyou")

        return redirect('/login')

    return render(request , 'signup.html')


def signin(request):

    if request.method =="POST":
        email = request.POST['email']
        pass1 = request.POST['pass1']


        user = authenticate(email = email , password = pass1)

        if user is not None:
            login(request,user)
            return render(request , "index.html" , {'fname' :request.first_name})

        else:
            messages.error(request,"please enter valid details")
            return redirect('/home')


    return render(request , 'login.html')
        

def game1(request):
    return render(request , 'game1.html')
   

def game2(request):
    return render(request , 'game2.html')
  

def easy(request):
    return render (request , "easy-test.html")

def moderate(request):
    return render (request , "moderate-test.html")

def hard(request):
    return render (request , "hard-test.html")

def test(request):
    return render(request , 'difficulty.html')
