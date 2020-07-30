from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
	if request.method == 'POST':
		
		username= request.POST.get('username')
		
		
		email= request.POST.get('Email')
		
		
		password1= request.POST.get('pass1')
		password2= request.POST.get('pass2')
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'User already exists')
				return redirect ('register')

			elif User.objects.filter(email= email).exists():
				messages.info(request, 'email already exists')
				return redirect('register')

			else:
				user= User.objects.create_user(username=username, email= email, password=password1)
				user.save()
				
				print('user data created')
				return redirect('login')
		else:
			messages.info(request, 'password not maching')
			print('password not matching')
		return redirect('register')
		
	return render(request , 'accounts/register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['pass1']
		user = auth.authenticate(username=username, password=password)

		if (user is not None) and (password == password):
			auth.login(request,user)
			return redirect('home')

		else:
			messages.info(request,'invalid credentials')
			return redirect('login')


	else:
		return render(request, 'accounts/login.html')


def logout(request):
	auth.logout(request)
	return redirect('home')