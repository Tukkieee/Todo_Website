from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if len(task) <1:
            messages.error(request, 'Input can not be empty')
            return redirect('home-page')
        
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()
    todos = todo.objects.filter(user=request.user)
    todo_user = request.user
    a = todo.objects.filter(user=request.user, status="False")
    todos_len = len(a) 

    return render(request, 'todo.html', {"todos":todos, "todos_len":todos_len, "user":todo_user})

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters')
            return redirect('register')
        
        get_all_user_by_username = User.objects.filter(username=username)
        
        if get_all_user_by_username:
            messages.error(request, 'Error,Username already exists')
            return redirect('register')


        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User successfully created, login now')
        return redirect('login')

    return render(request, 'register.html', {})

def logoutButton(request):
    logout(request)
    return redirect('login')



def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user= authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error,Wrong User Details or User doesn\'t exist')
            return redirect('login')

    return render(request, 'login.html', {})

@login_required
def DeleteTask(request, id):
    get_todo = todo.objects.get(user=request.user, id=id)
    get_todo.delete()
    return redirect('home-page')

@login_required
def CompleteTask(request, id):
    get_todo = todo.objects.get(user=request.user, id=id)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')


@login_required
def DeleteAllTask(request):
    get_todos = todo.objects.filter(user=request.user)
    get_todos.delete()
    return redirect('home-page')

def EditTask(request, id):
    get_todo = todo.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        return render(request, 'editPage.html', {'todo': get_todo})
    elif request.method == "POST":
        task = request.POST.get('task')
        get_todo.todo_name = task
        get_todo.save()
        return redirect('home-page')

    


    
        
        