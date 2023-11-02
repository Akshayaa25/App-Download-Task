from django.shortcuts import render, redirect
from .models import Admin, Apps

# Create your views here.
def home(request):
    return render(request, 'home.html')

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        try:
            admin = Admin.objects.get(username=username)
            if admin.password == password1:
                response = redirect('adminDashboard')
                response.set_cookie('user', 'admin')
                response.set_cookie('username', username)
                response.set_cookie('password1', password1)
                return response
            else:
                context = {
                    'user': 'admin',
                    'error': 'Incorrect password'
                }
                return render(request, 'login.html', context)
        except Admin.DoesNotExist:
            context = {
                'user': 'admin',
                'error': 'Invalid user'
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html', {'user': 'admin'})


def adminSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return render(request, 'signup.html', {'user': 'admin', 'error': 'Password mismatch'})
        else:
            myuser = Admin()
            myuser.username = username
            myuser.password = password1
            myuser.confirmpassword = password2
            myuser.save()
            return redirect('adminLogin')
    context = {'user': 'admin'}
    return render(request, 'signup.html', context)


def logout(request):
    response = redirect('home')
    response.delete_cookie('user')
    response.delete_cookie('username')
    response.delete_cookie('password1')
    return response


def adminDashboard(request):
    if (request.COOKIES.get('username') and request.COOKIES.get('password1')):
        return render(request, 'admindashboard.html')
    else:
        return redirect('home')


def addApps(request):
    if request.method == 'POST':
        appname = request.POST['appname']
        applink = request.POST['applink']
        appcategory = request.POST['appcategory']
        subcategory = request.POST['subcategory']
        points = request.POST['points']
        admin = Admin.objects.get(username=request.COOKIES.get('username'))
        if Apps.objects.filter(appname=appname).exists():
            msg = "App Already Exists"
        else:
            myapp = Apps(admin=admin, appname=appname, applink=applink, appcategory=appcategory, subcategory=subcategory, points=points)
            myapp.save()
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                myapp.photo = photo
                myapp.save()
            msg = "App Added Successfully"
    context = {
        'msg': msg,
        'link': 'addApps'
    }
    return render(request, 'admindashboard.html', context)
