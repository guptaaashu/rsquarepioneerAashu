from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from collections import OrderedDict
from .fusioncharts import FusionCharts
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, StudentAddForm, DriverAddForm, ConductorAddForm, BusAddForm, RouteAddForm, AddOwnerForm, StudentFormWithDate
from .forms import SchoolAddForm, TeacherAddForm, InUserAddForm, FeeCollectorAddForm
from .models import Student, Driver, Conductor, Bus, Route, Owner, School, Teacher, PBSUser, FeeCollector, Diesel
from django.contrib import messages
import datetime


# Create your views here.
@login_required
def dashboard(request):
    count = 0
    hr = 0
    for p in Driver.objects.all():
        hr = hr + 1
    for q in Owner.objects.all():
        hr = hr + 1
    for r in Conductor.objects.all():
        hr = hr + 1
    for s in FeeCollector.objects.all():
        hr = hr + 1
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    for i in students:
        count += 1
    for j in teachers:
        count += 1
    try:
        just_logged_in = request.session.get('just_logged_in', False)

    except:
        just_logged_in = False
    if just_logged_in:
        messages.success(request, 'Logged In sucessfully')
    return render(request, 'index.html', {'students': students, 'teachers': teachers, 'count': count, 'hr': hr})




'''def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'User Account Created')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})
'''
@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Added Sucessfully')

            return redirect('viewstudent')
    else:
        form = StudentAddForm()
    return render(request, 'add_student.html', {'form': form,})

@login_required
def view_student(request):
    try:
        students = Student.objects.all()
    except Student.DoesNotExist:
        raise Http404("No Student Model exists")
    return render(request, 'view_student.html', {'students': students})


@login_required
def viewdriver(request):
    try:
        drivers = Driver.objects.all()
    except Driver.DoesNotExists:
        raise Http404("No Driver Model Exists")
    return render(request, 'drivers.html', {'drivers': drivers})

@login_required
def adddriver(request):
    if request.method == "POST":
        form = DriverAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver Added Sucessfully')
            return redirect('viewdrivers')
    else:
        form = DriverAddForm()
    return render(request, 'adddriver.html', {'form': form,})

@login_required
def conductor(request):
    try:
        conductors = Conductor.objects.all()
    except Conductor.DoesNotExists:
        raise Http404("No Conductor Model Exists")
    return render(request, 'conductors.html', {'conductors': conductors,})

@login_required
def addconductor(request):
    if request.method == "POST":
        form = ConductorAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor Added Sucessfully')
            return redirect('conductors')
    else:
        form = ConductorAddForm()
    return render(request, 'addconductor.html', {'form': form, })

@login_required
def bus(request):

    try:
        busses = Bus.objects.all()
    except Bus.DoesNotExists:
        raise Http404("No bus Model Exists")
    return render(request, 'viewbus.html', {'busses': busses})

@login_required
def addbus(request):
    if request.method == "POST":
        form = BusAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bus Added Sucessfully')
            return redirect('viewbus')
    else:
        form = BusAddForm()
    return render(request, 'addbus.html', {'form': form})
@login_required
def routes(request):
    try:
        routes = Route.objects.all()
    except Route.DoesNotExists:
        raise Http404("No Route Model Exists")
    return render(request, 'routes.html', {'routes': routes})

@login_required
def addroute(request):
    if request.method == "POST":
        form = RouteAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Route Added Sucessfully')
            return redirect('routes')
    else:
        form = RouteAddForm()
    return render(request, 'addroute.html', {'form':form})

@login_required
def owner(request):
    try:
        owners = Owner.objects.all()
    except Owner.DoesNotExists:
        raise Http404("No Owner Model Exists")
    return render(request, 'owners.html', {'owners': owners})

@login_required
def addtheowner(request):
    if request.method == "POST":
        form = AddOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Owner Added Sucessfully')
            return redirect('owners')
    else:
        form = AddOwnerForm()
    return render(request, 'addowner.html', {'form': form})

@login_required
def school(request):
    try:
        schools = School.objects.all()
    except School.DoesNotExists:
        raise Http404("No School Model Exists")
    return render(request, 'school.html', {'schools': schools})

@login_required
def addschool(request):
    if request.method == "POST":
        form = SchoolAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'School Added Sucessfully')
            return redirect('school')
    else:
        form = SchoolAddForm()
    return render(request, 'addschool.html', {'form': form})

@login_required
def teacher(request):
    try:
        teachers = Teacher.objects.all()
    except Teacher.DoesNotExists:
        raise Http404("No Teacher Model Exists")
    return render(request, 'teacher.html', {'teachers': teachers})

@login_required
def addteacher(request):
    if request.method == "POST":
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher Added Sucessfully')
            return redirect('teacher')
    else:
        form = TeacherAddForm()
    return render(request, 'addteacher.html', {'form': form})

@login_required
def manageaccounts(request):
    try:
        accounts = PBSUser.objects.all()
    except PBSUser.DoesNotExists:
        raise Http404("No User Database Exists")
    return render(request, 'accounts.html', {'accounts': accounts})

@login_required
def signupdashboard(request):
    if request.method == "POST":
        form = InUserAddForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'User Added Sucessfully')
            return redirect('manageaccounts')
    else:
        form = InUserAddForm()
    return render(request, 'newsignup.html', {'form': form})

@login_required
def collectfee(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'collectfee.html', {'students': students, 'teachers': teachers})

@login_required
def diesel_con(request):
    diesel = Diesel.objects.all()
    return render(request, 'diesel.html', {'diesel': diesel})

@login_required
def invoice(request, pk):
    student = Student.objects.get(id=pk)
    date = datetime.datetime.now()

    return render(request, 'invoice.html', {'student': student, 'date': date})

@login_required
def student_single(request, pk):
    student = Student.objects.get(id=pk)
    date = datetime.datetime.now()

    return render(request, 'student_single.html', {'student': student, 'date': date})

@login_required
def teacher_single(request, pk):
    teacher = Teacher.objects.get(id=pk)
    date = datetime.datetime.now()

    return render(request, 'teacher_single.html', {'teacher': teacher, 'date': date})

@login_required
def driver_single(request, pk):
    driver = Driver.objects.get(id=pk)
    date = datetime.datetime.now()

    return render(request, 'driver_single.html', {'driver': driver, 'date': date})

@login_required
def conductor_single(request, pk):
    conductor = Conductor.objects.get(id=pk)
    date = datetime.datetime.now()

    return render(request, 'conductor_single.html', {'conductor': conductor, 'date': date})

@login_required
def feecollector_single(request, pk):
    feecollector = FeeCollector.objects.get(id=pk)
    date = datetime.datetime.now()

    return render(request, 'feecollector_single.html', {'feecollector': feecollector, 'date': date})

@login_required
def owner_single(request, pk):
    owner = Owner.objects.get(id=pk)
    date = datetime.datetime.now()
    return render(request, 'owner_single.html', {'owner': owner, 'date': date})

@login_required
def bus_single(request, pk):
    bus = Bus.objects.get(id=pk)
    date = datetime.datetime.now()
    return render(request, 'bus_single.html', {'bus': bus, 'date': date})

@login_required
def feecollector(request):
    try:
        feecollectors = FeeCollector.objects.all()
    except FeeCollector.DoesNotExists:
        raise Http404("No Fee Collector Model Exists")
    return render(request, 'feecollector.html', {'feecollectors': feecollectors,})

@login_required
def addfeecollector(request):
    if request.method == "POST":
        form = FeeCollectorAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fee Collector Added Sucessfully')
            return redirect('feecollector')
    else:
        form = FeeCollectorAddForm()
    return render(request, 'addfeecollector.html', {'form': form, })

@login_required
def userprofile(request, pk):
    user = get_object_or_404(PBSUser, id=pk)
    return render(request, 'userprofile.html', {'user': user})

@login_required
def singleroute(request, pk):
    route = get_object_or_404(Route, id=pk)
    return render(request, 'single_route.html', {'route': route})
