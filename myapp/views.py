from django.shortcuts import render,redirect
from .models import Attendance,vacancies1,Books,student,papers1
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
import os
from django.http import FileResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def sign_in(request):
    from pytesseract import image_to_string
    import cv2
    import time
    import easyocr
    import re
    from PIL import Image
    import cv2
    import time
    feature4=vacancies1.objects.get(id1=1)
    if(feature4.vac==0):
        return redirect('b')
    camera_port = 0
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise IOError("can not open")
    return_value, image = camera.read()
    cv2.imwrite("img2.png", image)
    reader = easyocr.Reader(['en'])
    output = reader.readtext('img2.png')
    l=[]
    for i in output:
        for j in i:
           if isinstance(j,str):
               l.append(j)
    s=" ".join(l)
    x1=re.findall(r'..131A....',s)
    x="".join(x1)
    if(len(x1)==0):
        return render(request,'invalid.html')
    else:
        def nth_repl(s, sub, repl, n):
            find = s.find(sub)
            i = find != -1
            while find != -1 and i != n:
                find = s.find(sub, find + 1)
                i += 1
            if i == n:
                return s[:find] + repl + s[find+len(sub):]
            return s
        my_string = x
        my_string=nth_repl(my_string,"O","0",1)
        my_string=nth_repl(my_string,"O","0",2)
        my_string=nth_repl(my_string,"4","A",1)
        my_string=nth_repl(my_string,"A","4",2)
        my_string=nth_repl(my_string,"S","5",1)
        q=Attendance()
        q.rollno=my_string
        z=student.objects.get(rollno=my_string)
        q.name=z.name
        import datetime
        import time
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        q.start=current_time
        q.end='00:00:00'
        q.date=datetime.date.today()
        date=datetime.date.today()
        now = datetime.datetime.now()
        q.month=now.strftime('%B')
        q.save()
        feature=vacancies1.objects.get(id1=1)
        feature.vac=feature.vac-1
        feature.save()
        return render(request,'sign_in.html')
def sign_out(request):
    from PIL import Image
    from pytesseract import image_to_string
    import cv2
    import time
    import easyocr
    import re
    camera_port = 0
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise IOError("can not open")
    return_value, image = camera.read()
    cv2.imwrite("img2.png", image)
    reader = easyocr.Reader(['en'])
    output = reader.readtext('img2.png')
    l=[]
    for i in output:
        for j in i:
           if isinstance(j,str):
               l.append(j)
    s=" ".join(l)
    x=re.findall(r'20........',s)
    x="".join(x)
    def nth_repl(s, sub, repl, n):
        find = s.find(sub)
        i = find != -1
        while find != -1 and i != n:
            find = s.find(sub, find + 1)
            i += 1
        if i == n:
            return s[:find] + repl + s[find+len(sub):]
        return s
    my_string = x
    my_string=nth_repl(my_string,"O","0",1)
    my_string=nth_repl(my_string,"O","0",2)
    my_string=nth_repl(my_string,"4","A",1)
    my_string=nth_repl(my_string,"A","4",2)
    my_string=nth_repl(my_string,"S","5",1)
    feature=vacancies1.objects.get(id1=1)
    feature.vac=feature.vac+1
    feature.save()
    a=Attendance.objects.get(rollno=my_string,end="00:00:00")
    import datetime
    import time
    from datetime import datetime
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    a.end=current_time
    from datetime import datetime
    start_time = str(a.start)
    end_time = str(a.end)
    t1 = datetime.strptime(start_time, "%H:%M:%S")
    print('Start time:', t1.time())
    t2 = datetime.strptime(end_time, "%H:%M:%S")
    print('End time:', t2.time())
    delta = t2 - t1
    ms = delta.total_seconds()
    a.total=int(ms/60)
    a.save()
    return render(request,'sign_out.html')
def vacancies(request):
    feature=vacancies1.objects.get(id1=1)
    return render(request,'vacancies.html',{'feature':feature})

def books(request):
    a=request.GET['dept']
    features=Books.objects.filter(dept=a)
    return render(request,'books.html',{'features':features})
def take(request):
    features=Books.objects.all()
    return render(request,'take.html',{'features':features})
def take1(request):
    rollno=request.GET['rollno']
    book=request.GET['books']
    import datetime
    from datetime import timedelta
    a=student.objects.get(rollno=rollno)
    if(a.b1!='NA' and a.b2!='NA' and a.b3!='NA'):
        return redirect('a')
    elif(a.b1=='NA'):
        a.b1=book
        a.due1=datetime.date.today()+timedelta(days=15)
        c=Books.objects.get(Name=book)
        c.availability=c.availability-1
        c.save()
    elif(a.b1!='NA' and a.b2=='NA'):
        a.b2=book
        a.due2=datetime.date.today()+timedelta(days=15)
        c=Books.objects.get(Name=book)
        c.availability=c.availability-1
        c.save()
    elif(a.b1!='NA' and a.b2!='NA' and a.b3=='NA'):
        a.b3=book
        a.due3=datetime.date.today()+timedelta(days=15)
        c=Books.objects.get(Name=book)
        c.availability=c.availability-1
        c.save()
    a.save()
    features=student.objects.get(rollno=rollno)
    return render(request,'final.html',{'features':features})
def return1(request):
    features=Books.objects.all()
    return render(request,'return.html',{'features':features})
def return2(request):
    rollno=request.GET['rollno']
    book1=request.GET['books']
    import datetime
    from datetime import timedelta
    a=student.objects.get(rollno=rollno)
    if(a.b1==book1):
        a.b1='NA'
        a.due1='2000-01-01'
        c=Books.objects.get(Name=book1)
        c.availability=c.availability+1
        c.save()
    elif(a.b2==book1):
        a.b2='NA'
        a.due2='2000-01-01'
        c=Books.objects.get(Name=book1)
        c.availability=c.availability+1
        c.save()
    elif(a.b3==book1):
        a.b3='NA'
        a.due3='2000-01-01'
        c=Books.objects.get(Name=book1)
        c.availability=c.availability+1
        c.save()
    a.save()
    features=student.objects.get(rollno=rollno)
    return render(request,'final.html',{'features':features})
def attendance(request):
    a=request.GET['rollno']
    features=Attendance.objects.filter(rollno=a)
    return render(request,'attendance.html',{'features':features})
def index1(request):
    return render(request,'index1.html')
def about(request):
    return render(request,'about.html')
def check(request):
    a=request.GET['rollno']
    features=student.objects.get(rollno=a)
    return render(request,'final.html',{'features':features})
def a(request):
    return render(request,'a.html')
def b(request):
    return render(request,'b.html')
def c(request):
    return render(request,'c.html')
def otp(request):
    return render(request,'otp.html')
def otp1(request):
    roll=request.GET['rollno']
    features=student.objects.get(rollno=roll)
    a=features.email
    ph=features.phone
    c=[]
    ph=str(ph)
    s=len(ph)
    for i in range(s):
       if i % 2 == 0:
          c.append(ph[i])
    s=''.join(c)
    message=s
    subject="Login OTP"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=recipient_list = [a, ]
    send_mail( subject,message, email_from, recipient_list )
    return render(request,'otp1.html')
def otp2(request):
    d=request.GET['otp']
    e=request.GET['rollno']
    features=student.objects.get(rollno=e)
    phone=features.phone
    phone=str(phone)
    c=[]
    s=len(phone)
    for i in range(s):
       if i % 2 == 0:
          c.append(phone[i])
    s=''.join(c)
    if(d==s):
       return render(request,'student.html',{'features':features})
    else:
        messages.info(request,'You have entered worng otp')
        return render(request,'otp.html')
def mattendance(request):
    roll=request.GET['rollno']
    month=request.GET['month']
    features=Attendance.objects.filter(rollno=roll,month=month)
    return render(request,'attendance.html',{'features':features})
def librarian(request):
    import datetime
    features=student.objects.filter(Q(due1=datetime.date.today())|Q(due2=datetime.date.today())|Q(due3=datetime.date.today()))
    l=[]
    for feature in features.iterator():
        l.append(feature.email)
    message="You have to submit your book by today evening otherwise you will be fined"
    subject="reminder"
    email_from=settings.EMAIL_HOST_USER
    send_mail( subject,message, email_from, l )
    return render(request,'sent.html')
    
def librarian1(request):
    a=request.GET['key']
    if(a=='123'):
        return render(request,'librarian.html')
    else:
        return render(request,'index1.html')

def update(request):
    a=request.GET['bname']
    b=request.GET['dname']
    c=request.GET['count']
    b1=Books()
    b1.Name=a
    b1.dept=b
    b1.availability=c
    b1.save()
    return render(request,'update.html')
def research(request):
    dept=request.GET['dname']
    file=request.GET['url']
    a=papers1()
    a.dept1=dept
    a.paper1=file
    a.save()
    return render(request,'final1.html')

def paper1(request):
    a=request.GET['dept']
    features=papers1.objects.filter(dept1=a)
    return render(request,'viewpapers.html',{'features':features})
def invalid(request):
    return render(request,'invalid.html')
def present(request):
    date=request.GET['date']
    features=Attendance.objects.filter(date=date,end='00:00:00')
    return render(request,'attendance.html',{'features':features})
