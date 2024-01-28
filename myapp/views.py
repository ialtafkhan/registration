from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignUpPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('cpassword')
        if pass1!= pass2:
            return HttpResponse('your password and confirm password are not same')
        else:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
        # return HttpResponse("user has been crested Successfully!")
        

    return render (request,'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request,username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorect!')

        # print(username, pass1)

    return  render(request, 'login.html')  

def Logout(request):
    logout(request)
    return redirect('login')