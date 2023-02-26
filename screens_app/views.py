from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User #this is an inbuilt model in the django

from django.contrib import messages, auth


# Importing all the models from the models.py
from . models import Courses, Evaluation

# Create your views here.
def register(request):
    if request.method == 'POST':
        # saving the details into the database
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password= request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        username = request.POST['username']

        if password == password2:
            if User.objects.filter(email=email).exists():
                # if the email is aleady in the database we will send them the error message
                return render('./error.html')
            else:
                # if the email is not in the db then we will register the user
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
                # saving the user to the database
                user.save()
                return render(request, './Welcome.html')
        else:
            return render('./passwordnotmatch.html')
            
    return render(request, './index.html')


def welcome(request):
    return render(request, './Welcome.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # if user existed
            auth.login(request,user)
            return redirect('dashboard')
        else:
            # Need to work with the notifications css
            messages.error(request,'incorrect details')
            return redirect('login')
    else:
        return render(request, './Login.html')


def dashboard(request):
    course = Courses.objects.all()
    context={
        'courses':course
    }
    return render(request, './Dashboard.html', context)


def course(request, course_id):
    data = User.objects.all() #to display emails in UI
    evaluations  = Evaluation.objects.all()
    reports = evaluations.filter(course_Id = course_id)
    print(reports,"**************")
    course = get_object_or_404(Courses, pk=course_id)
    print(course.id,"/*/*/*/*/")
    context={
        'course':course,
        'data':data,
        'reports':reports
    }
    return render(request, './Course.html', context)


# submits the report of the student
def evalution(request):
    if request.method == 'POST':
        email = request.POST['email']
        marks = request.POST['marks']
        remarks = request.POST['remarks']
        course_Id = request.POST['course_id']

        # saving the data to the database
        report = Evaluation(email=email, remarks=remarks, marks=marks, course_Id=course_Id)
        report.save()
        return redirect(f'/course/{course_Id}')
    return render(request,'./Course.html')
