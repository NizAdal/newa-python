from django.shortcuts import render,HttpResponse,redirect
from nizam.models import Blog,About,Message,Contact,Membership,Notes,Survey,Questions,Data
from django.core.mail import send_mail
from django.views import View
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q
from nizam.task import send_mail_func
from new import settings
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from celery.schedules import crontab
from .task import test_func
import math
import json
from django.conf import settings

# Create your views here.
def posts(request):
    no_of_posts = 6
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)    
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts:page*no_of_posts]
    if page > 1:
        prev = page -1
    else:
        prev = None
    if page < math.ceil(length/no_of_posts):    
        nxt = page + 1          
    else:
        nxt = None
    context = {'blogs': blogs,'prev': prev,'nxt': nxt}
    return render(request,'app/posts.html', context)

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, 'app/blogpost.html', context)

def home(request):
    gee = About.objects.filter()
    mub = Message.objects.all()
    cont = {'gee': gee,'mub':mub}
    return render(request,'app/index.html',cont)  

def contact(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            desc = request.POST.get('desc')
            instance = Contact(name=name, email=email, phone=phone, desc=desc)
            instance.save()
            send_mail(
            "Here is Create ",
            "This is firstname:" + name + "\n" + 
            "This is email:" + email + "\n" + "This is phone:" + phone + "\n" + "This is desc:" + desc,
            "nizamaniabdulmalik321@gmail.com",
            [email],
            fail_silently=False,
            )
        return render(request,'app/contact.html')        

def membership(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            father = request.POST.get('father')
            date = request.POST.get('date')
            dep = request.POST.get('dep')
            year = request.POST.get('year')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            file = request.FILES.get('file')
            hi = Membership(name=name,father=father,date=date,dep=dep,year=year, email=email, phone=phone, file=file)
            try:
                hi.save()
                messages.success(request, "Congratulations! User Registered Successfully")
                send_mail(
                    "Membership Created",
                    "This is name: " + name + "\n" +
                    "This is email: " + email + "\n" +
                    "This is phone: " + phone + "\n" +
                    "This is department: " + dep,
                    "nizamaniabdulmalik321@gmail.com",
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                messages.warning(request, "Failed to save membership: " + str(e))  
        return render(request,"app/membership.html",locals())

def membersdetail(request):
    no_of_posts = 20
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)    
    mem = Membership.objects.filter(status=True)
    length = len(mem)
    mem = mem[(page-1)*no_of_posts:page*no_of_posts]
    if page > 1:
        prev = page -1
    else:
        prev = None
    if page < math.ceil(length/no_of_posts):    
        nxt = page + 1          
    else:
        nxt = None
    if mem:
        malik = {'mem': mem,'prev': prev,'nxt': nxt}
        return render(request,"app/membersdetail.html",malik)
    else:
        return render(request,"app/membersdetail.html")

def notes(request):      
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        dep = request.POST.get('dep')
        year = request.POST.get('year')
        semester = request.POST.get('semi')
        subject = request.POST.get('sub')
        phone = request.POST.get('phone', 0)
        file = request.FILES.get('file')
        ha = Notes(name=name,dep=dep,year=year,semester=semester,subject=subject,phone=phone,file=file)
        ha.save()
    return render(request,"app/notes.html")

def getnotes(request):
    no_of_posts = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    notes = Notes.objects.filter(status=True)
    length = len(notes)
    notes = notes[(page-1)*no_of_posts:page*no_of_posts]
    if page > 1:
        prev = page -1
    else:
        prev = None
    if page < math.ceil(length/no_of_posts):    
        nxt = page + 1          
    else:
        nxt = None    
    if notes:
        co = {'notes': notes,'prev': prev,'nxt': nxt}
        return render(request, "app/getnotes.html", co)
    else:
        return render(request, "app/no_notes.html")       

def filenotes(request, pk):
    files = Notes.objects.get(pk=pk)
    fi = {'files': files} 
    return render(request,"app/filenotes.html",fi)

def search(request):
    query = request.GET['search']
    allPosts=Blog.objects.filter(Q(slug__icontains=query) | Q(title__icontains=query))
    al=Membership.objects.filter(Q(name__icontains=query))
    aa=Notes.objects.filter(Q(dep__iexact=query) | Q(semester__iexact=query)| Q(year__iexact=query)| Q(subject__iexact=query)| Q(teacher__iexact=query))
    if allPosts.exists() or al.exists() or aa.exists():
        return render(request,"app/search.html",locals())    
    else:    
        return render(request,"app/sear.html") 

def survey(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        rollno = request.POST.get('rollno')
        year = request.POST.get('year')
        adal = Data(name=name,dept=dept,rollno=rollno,year=year)
        adal.save()
    else:    
        messages.warning(request, "Failed to save the form: " )                  
    return render(request, 'app/survey.html', locals())          

def savesurvey(request):
    if request.method == 'GET':
        sur = Survey.objects.all().first()
        context = {'sur': sur}
    return render(request, 'app/survey.html', context)


def startsurvey(request):
    if request.method == "GET":
        questions = Questions.objects.all()
        context = {'questions': questions }
    if request.method == "POST":
        answer1 = request.POST.getlist('answer1')
        answer2 = request.POST.getlist('answer2')
        answer3 = request.POST.getlist('answer3')
        answer4 = request.POST.getlist('answer4')
        answer5 = request.POST.getlist('answer5')
        answer6 = request.POST.getlist('answer6')
        answer7 = request.POST.getlist('answer7')
        answer8 = request.POST.getlist('answer8')
        answer9 = request.POST.getlist('answer9')
        answer10 = request.POST.getlist('answer10')
        answer11 = request.POST.getlist('answer11')
        answer12 = request.POST.getlist('answer12')
        n = Questions(answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,
        answer8=answer8,answer9=answer9,answer10=answer10,answer11=answer11,answer12=answer12)
        n.save()
        messages.success(request, "Thanks For Participating In Survey")
    return render(request, 'app/index.html')






# def send_email(request):
#     send_email_fun.delay("your_subject", "your_message", settings.EMAIL_HOST_USER, "receiver_email_address")
#     return HttpResponse("Sent Email Successfully...Check your mail please")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")    

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour= 1, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", tasks='send_mail_app.task.send_mail_func') #, args = json.dumps((2,3,))) 
    return HttpResponse("Done")