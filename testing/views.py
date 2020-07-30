from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		todos = Todo.objects.filter(user=request.user)

	return render(request, 'todo/index.html', {'todo':todos})

@login_required(login_url = 'login')
def createTodo(request):
	if request.method == 'POST':
		title= request.POST.get('title')
		description= request.POST.get('desc')

		data= Todo(title=title, desc=description , user= request.user)
		data.save()

		return redirect('home')



	return render(request, 'todo/create.html')

def DeleteTodo(request, id):
	todo = Todo.objects.get(id=id)
	todo.delete()
	return redirect('home')

def UpdateTodo(request,id):
	todo = Todo.objects.get(id=id)
	if request.method == 'POST':
		t= True
		
		todo.title= request.POST.get('title')
		todo.desc= request.POST.get('desc')
		
		todo.save()
		return redirect('home')
		

	
	return render(request, 'todo/update.html' , {'todo':todo})