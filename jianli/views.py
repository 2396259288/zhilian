from django.contrib.auth.models import User
from .models import BadsicInfo,ProExper,WorkExper,jianli
from index.models import JobInfo
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
import os


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart

# Create your views here.
@csrf_exempt
def create_jianli(request):
    if request.method == "POST":
        name = request.POST['name']
        sex = request.POST['sex']
        email = request.POST['email']
        school = request.POST['school']
        prof = request.POST['prof']
        intro = request.POST['intro']
        honor = request.POST['honor']
        want_salary = request.POST['want_salary']
        want_position = request.POST['want_position']
        BadsicInfo.objects.create(name = name, sex = sex, email = email, school = school, prof = prof, intro = intro, honor = honor, want_salary = want_salary, want_position = want_position, username = request.session['username'])
        print(request.session['username'])
        return render_to_response('pro_exper.html')
    return render_to_response('create_jianli.html')
@csrf_exempt
def pro_exper(request):
    if request.method == "POST":
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        info = request.POST['info']
        main_work = request.POST['main_work']
        flag = 0
        ProExper.objects.create(name = name, start_date = start_date, end_date = end_date, info = info, main_work = main_work, username = request.session['username'])
        return render_to_response('pro_exper.html',{'flag':flag})
    return render_to_response('pro_exper.html')

@csrf_exempt
def work_exper(request):
    if request.method == "POST":
        company = request.POST['company']
        position = request.POST['position']
        salary = request.POST['salary']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        info = request.POST['info']
        honor = request.POST['honor']
        flag = 0
        WorkExper.objects.create(company = company, position = position, salary = salary, start_date = start_date, info = info, honor = honor, username = request.session['username'])
        return render_to_response('work_exper.html', {'flag':flag})
    return render_to_response('work_exper.html')

@csrf_exempt

def upload_jianli(request):
    username = request.session['username']
    upload = request.FILES['upload']
    f = open(os.path.join('static/jianli', upload.name), 'wb')
    for i in upload.chunks():
        f.write(i)
    f.close()
    print('---------上传简历成功-----------')
    n = len(jianli.objects.filter(username = username))
    if n > 0:
        jianli.objects.filter(username = username).update(jianli = upload.name)
    else:
        jianli.objects.create(username = username, jianli = upload.name)
    return HttpResponseRedirect('/jianli/show_jianli')


def show_jianli(request):
    user = request.GET.get('user')
    if user == None:
        global jianli_name
        jianli_name = jianli.objects.all().filter(username = request.session['username'])[:1]
        jianli_num = len(jianli_name)
        basic_info = BadsicInfo.objects.all().filter(username = request.session['username'])[:1]
        num = len(basic_info)
        work_expers = WorkExper.objects.all().filter(username = request.session['username'])
        pro_expers = ProExper.objects.all().filter(username = request.session['username'])
        return render_to_response('show_jianli.html', {'basic_info': basic_info, 'work_expers': work_expers, 'pro_expers': pro_expers, 'num': num, 'jianli_name':jianli_name, 'jianli_num':jianli_num})

    basic_info = BadsicInfo.objects.all().filter(username = user)[:1]
    
    work_expers = WorkExper.objects.all().filter(username = user)
    pro_expers = ProExper.objects.all().filter(username = user)
    return render_to_response('show_jianli.html', {'basic_info': basic_info, 'work_expers': work_expers, 'pro_expers': pro_expers})






@csrf_exempt
def push_jianli1(request):
    
    idname = request.GET.get('idname')
    email = JobInfo.objects.filter(idName = idname)[0].companyEmail
    user = request.session['username']
    my_sender='2396259288@qq.com'    # 发件人邮箱账号
    my_pass = 'ucyknmtmusjyeaff'              # 发件人邮箱密码
    my_user=email      # 收件人邮箱账号，我这边发送给自己







    def mail():
        ret=True
        try:
            msg = MIMEMultipart()
            msg['From'] = Header("贾浩", 'utf-8')
            msg['To'] =  Header("您好", 'utf-8')
            subject = '应聘'
            msg['Subject'] = Header(subject, 'utf-8')

            info = "<a href= 'http://127.0.0.1/jianli/show_jianli?user=%s'>简历</a>" % (user)
            msg.attach(MIMEText(info, 'html', 'utf-8'))

            
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            JobInfo.objects.filter(idName = idname).update(status = 1)
        except Exception as e:
            print(e)
            ret=False  
            



     
    ret=mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送成功")

    return HttpResponseRedirect('/info?idname='+idname)












def push_jianli(request):
    idname = request.GET.get('idname')
    email = JobInfo.objects.filter(idName = idname)[0].companyEmail
    jl = jianli.objects.all().filter(username = request.session['username'])[0]
    jianli_name = jl.jianli
    my_sender='2396259288@qq.com'    # 发件人邮箱账号
    my_pass = 'ucyknmtmusjyeaff'              # 发件人邮箱密码
    my_user=email      # 收件人邮箱账号，我这边发送给自己

    def mail():
        ret=True
        try:
            msg = MIMEMultipart()
            msg['From'] = Header("贾浩", 'utf-8')
            msg['To'] =  Header("您好", 'utf-8')
            subject = '应聘'
            msg['Subject'] = Header(subject, 'utf-8')
            msg.attach(MIMEText('我对该工作十分感兴趣希望您有时间可以看一下简历...', 'plain', 'utf-8'))

            att1 = MIMEText(open(os.path.join('static/jianli', jianli_name), 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="resume.docx"'
            msg.attach(att1)

            
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            JobInfo.objects.filter(idName = idname).update(status = 1)
        except Exception as e:
            print(e)
            ret=False  
            



     
    ret=mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送成功")

    return HttpResponseRedirect('/info?idname='+idname)




