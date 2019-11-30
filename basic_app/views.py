from django.shortcuts import render,redirect
from basic_app.forms import UserForm
from basic_app.forms import StudentForm
from basic_app.forms import UpdateForm
from basic_app.forms import PlacedstudentForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages

from django.views.generic import TemplateView,CreateView
from basic_app.models import Student,Placed_student

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pa

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
           # messages.success(request,'User Registration Successfully')
            user.save()
            registered = True
            return render(request,'thanks.html',{})
            return redirect('/home')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                uname=user.username
                if uname[0]=='I' and uname[1]=='T':
                    return show(request)
                else:
                    if User_present(uname):
                        return render(request,'you_have_register.html',{})
                    else:
                        return student_info(request)

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return render(request,'invalid.html',{})
    else:
        return render(request,'login.html',{})


class home(TemplateView):
    template_name = 'home.html'


def student_info(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()                
                return render(request,'thanks.html',{})
            except:
                pass
    else:
        form=StudentForm()
    return render(request,'student.html',{'form':form})


def User_present(p):
    if Student.objects.filter(Username=p).exists() or Placed_student.objects.filter(Username=p).exists():
        return True
    else:
        return False

def show(request):
    s_details=Student.objects.order_by('FirstName')
    return render(request,'admin.html',{'s_details':s_details})


def edit(request,id):
    s_edit=Student.objects.get(id=id)
    return render(request,'edit.html',{'s_edit':s_edit})


def map(request):
    return render(request,'map.html',{})

def update(request,id):
    s_edit=Student.objects.get(id=id)
    form=UpdateForm(request.POST or None,instance = s_edit)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'s_edit':s_edit})

def delete(request,id):
    s_delete=Student.objects.get(id=id)
    Placed_student.objects.create(Username=s_delete.Username,FirstName=s_delete.FirstName,LastName=s_delete.LastName,EmailID=s_delete.EmailID,MobileNumber=s_delete.MobileNumber,
    Fagg_percentage=s_delete.Fagg_percentage,F_YroPassing=s_delete.F_YroPassing,Sagg_percentage=s_delete.Sagg_percentage,S_YroPassing=s_delete.S_YroPassing,
                                  Tagg_percentage=s_delete.Tagg_percentage,T_YroPassing=s_delete.T_YroPassing,Total=s_delete.Total)
    s_delete.delete()

    return redirect('/show')



def per_delete(request,id):
    sp_delete = Student.objects.get(id=id)
    sp_delete.delete()
    return redirect('/show')


id=0
def sort(request):
    global id
    id=request.POST.get("S")
    s_details=Student.objects.filter(Total__gt=int(id))
    return render(request,'sorted_student.html',{'s_details':s_details})


import smtplib
import socket

socket.getaddrinfo('localhost',8080)

def email(request):
    global id
    s_details = Student.objects.filter(Total__gt=id)
    emails = []
    for s in s_details:
        emails.append(s.EmailID)
    print(emails)
    for i in range(len(emails)):
        print(i)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        message=request.POST.get("m")
        s.sendmail(settings.EMAIL_HOST_USER,emails[i],message)
        s.quit()
    return redirect('/show')
#-------------------------For Placed Student---------------------#


def pstudent(request):
    ps_details=Placed_student.objects.order_by('FirstName')
    return render(request,'placed_student.html',{'ps_details':ps_details})


def pedit(request,id):
    s_edit=Placed_student.objects.get(id=id)
    return render(request,'pedit.html',{'s_edit':s_edit})




def pupdate(request,id):
    s_edit=Placed_student.objects.get(id=id)
    form=PlacedstudentForm(request.POST or None,instance = s_edit)
    if form.is_valid():
        form.save()
        return redirect('/pstudent')
    return render(request,'pedit.html',{'s_edit':s_edit})



def p_per_delete(request,id):
    sp_delete = Placed_student.objects.get(id=id)
    sp_delete.delete()
    return redirect('/pstudent')


comname=""
def searchcompany(request):
    global comname
    comname=request.POST.get("c")
    scompany=Placed_student.objects.filter(Q(Company_name__icontains=comname))
    return render(request, 'pstdsearch.html', {'scompany': scompany})


import csv
def data_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['content-Disposition']='attachment; filename="Total_Placed_Student.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Email Address','Company Name'])
   # field_names=[field.name for field in opts.fields]
    users=Placed_student.objects.all().values_list('FirstName','LastName','EmailID','Company_name')
    for user in users:
        writer.writerow(user)
       # writer.writerow([getattr(user,field) for field in field_names])

    return response
    
def data_csv1(request):
    response=HttpResponse(content_type='text/csv')
    response['content-Disposition']='attachment; filename="P_std_company.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Email Address','Company Name'])
   # field_names=[field.name for field in opts.fields]
    users=Placed_student.objects.all().values_list('FirstName','LastName','EmailID','Company_name').filter(Q(Company_name__icontains=comname))
    for user in users:
        writer.writerow(user)
    return response









#----------------------------------------------------------#
def mplimage(request):
    place_student=Placed_student.objects.count()
    unplace_student=Student.objects.count()
    place_student_percent = (place_student* 360) / (place_student + unplace_student)
    unplace_student_percent = (unplace_student * 360) / (place_student+ unplace_student)
    count_list = [place_student_percent, unplace_student_percent]
    print(count_list)
    place_studentlable = "Placed Student {}"
    unplace_studentlable = "Unplaced Student {}"


    pielable = [place_studentlable.format(place_student), unplace_studentlable.format(unplace_student)]
    n = 2
    exp = [0, 0.2]
    section = np.arange(n)
    #ax1 = plt.subplots()
    plt.pie(count_list, explode=exp, labels=pielable)
    plt.title('Analysis Of Student')
    buf = io.BytesIO()
    plt.savefig(buf,format='png')
    plt.close()

    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response
#-------------------------------Search---------------------------------#

def search(request):
    if request.method=="POST":
        srch=request.POST['srh']
        if srch:
            match=Student.objects.filter(Q(FirstName__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                messages.error(request, 'no result found')

    return render(request, 'search.html', {})
