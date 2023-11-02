from django.shortcuts import render, redirect
from User.models import User, Task
from Admin.models import Admin, Apps

def home(request):
    return render(request, 'home.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        try:
            user = User.objects.get(username=username)
            if user.password == password1:
                response = redirect('userDashboard')
                response.set_cookie('user', 'user')
                response.set_cookie('username', username)
                response.set_cookie('password1', password1)
                return response
            else:
                context = {
                    'user': 'user',
                    'error': 'Incorrect password'
                }
                return render(request, 'login.html', context)
        except User.DoesNotExist:
            context = {
                'user': 'user',
                'error': 'Invalid user'
            }
            return render(request, 'login.html', context)
    context = {'user': 'user'}
    return render(request, 'login.html', context)

def userSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return render(request, 'signup.html', {'user': 'user', 'error': 'Password mismatch'})
        else:
            myuser = User()
            myuser.username = username
            myuser.password = password1
            myuser.confirmpassword = password2
            myuser.save()
            return redirect('userLogin')
    context = {'user': 'user'}
    return render(request, 'signup.html', context)

def logout(request):
    response = redirect('home')
    response.delete_cookie('user')
    response.delete_cookie('username')
    response.delete_cookie('password1')
    return response

def userDashboard(request):
    if (request.COOKIES.get('username') and request.COOKIES.get('password1')):
        user = User.objects.get(username=request.COOKIES.get('username'))
        total_points = user.total_points()
        context = {
            'user': user,
            'total_points': total_points
        }
        return render(request, 'userdashboard.html', context)
    else:
        return redirect('home')

def userProfile(request):
    user = User.objects.get(username=request.COOKIES.get('username'))
    total_points = user.total_points()
    context = {
        'user': user,
        'total_points': total_points,
        'link': 'profile'
    }
    return render(request, 'userdashboard.html', context)

def taskAssigned(request):
    tasks = Apps.objects.all()
    context = {
        'tasks': tasks,
        'link': 'taskAssigned'
    }
    return render(request, 'userdashboard.html', context)

def taskCompleted(request):
    user = User.objects.get(username=request.COOKIES.get('username'))
    completed_tasks = Task.objects.filter(user=user)
    context = {
        'completed_tasks': completed_tasks,
        'link': 'taskCompleted'
    }
    return render(request, 'userdashboard.html', context)

def taskDetails(request, id):
    task = Apps.objects.get(id=id)
    context = {
        'task': task,
        'link': 'taskDetails'
    }
    return render(request, 'userdashboard.html', context)

def screenShot(request, id):
    user = User.objects.get(username=request.COOKIES.get('username'))
    task = Apps.objects.get(id=id)
    appname = task.appname
    points = task.points
    screenshot = request.FILES.get('screenshot')
    if Task.objects.filter(user=user, appname=appname).exists():
        msg = "Task Completed Already"
        context = {
            'msg':msg,
            'task': task,
            'link': 'taskDetails'
        }
        return render(request, 'userdashboard.html', context)
    if not screenshot:
        msg = "Screenshot not uploaded"
        context = {
            'msg':msg,
            'task': task,
            'link': 'taskDetails'
        }
        return render(request, 'userdashboard.html', context)
    
    new_task = Task.objects.create(user=user, appname=appname, points=points, screenshot=screenshot)
    new_task.save()
    msg = "Task Completed Successfully"
    context = {
        'msg':msg,
        'task': task,
        'link': 'taskDetails'
    }
    return render(request, 'userdashboard.html', context)