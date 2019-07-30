from django.shortcuts import render,redirect
from .models import Position, JobInfo
from jianli.models import jianli
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, F
import json
from pylab import *
import pylab as pl

# Create your views here.
@csrf_exempt
def indexView(request):
    username = request.user.username
    flag = request.GET.get('flag')
    job = request.GET.get('job')
    prepage = request.GET.get('prepage')
    nextpage = request.GET.get('nextpage')
    if flag == '0':
        if job == None:
            if nextpage == None:
                if prepage == None:
                    jobs = JobInfo.objects.all().order_by('-clik')[0: 20]
                    nextpage = 2
                    prepage = 0
                    return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage),'username':username})
                
                jobs = JobInfo.objects.all().order_by('-clik')[(int(prepage)-1)*20: (int(prepage)-1)*20+20]
                nextpage = int(prepage) + 1
                prepage = int(prepage) - 1
                return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage),'username':username})
            
            jobs = JobInfo.objects.all().order_by('-clik')[(int(nextpage)-1)*20: (int(nextpage)-1)*20+20]
            nextpage = int(nextpage) + 1
            prepage = int(nextpage) - 1
            return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage-1), 'count':len(jobs),'username':username})
        
        if nextpage == None:
            if prepage == None:
                jobs = JobInfo.objects.filter(Q(name__icontains=job)).order_by('-clik')[0: 20]
                nextpage = 2
                prepage = 0
                return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage), 'job':job, 'count':len(jobs),'username':username})
            
            jobs = JobInfo.objects.filter(Q(name__icontains=job)).order_by('-clik')[(int(prepage)-1)*20: (int(prepage)-1)*20+20]
            nextpage = int(prepage) + 1
            prepage = int(prepage) - 1
            return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage), 'job':job,'username':username})
        
        jobs = JobInfo.objects.filter(Q(name__icontains=job)).order_by('-clik')[(int(nextpage)-1)*20: (int(nextpage)-1)*20+20]
        nextpage = int(nextpage) + 1
        prepage = int(nextpage) - 1
        return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage-1), 'job':job, 'count':len(jobs),'username':username})

    if job == None:
        if nextpage == None:
            if prepage == None:
                jobs = JobInfo.objects.all().order_by('-time')[0: 20]
                nextpage = 2
                prepage = 0
                return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage),'username':username})
            
            jobs = JobInfo.objects.all().order_by('-time')[(int(prepage)-1)*20: (int(prepage)-1)*20+20]
            nextpage = int(prepage) + 1
            prepage = int(prepage) - 1
            return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage),'username':username})
        
        jobs = JobInfo.objects.all().order_by('-time')[(int(nextpage)-1)*20: (int(nextpage)-1)*20+20]
        nextpage = int(nextpage) + 1
        prepage = int(nextpage) - 1
        return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage-1), 'count':len(jobs),'username':username})
        
    if nextpage == None:
        if prepage == None:
            jobs = JobInfo.objects.filter(Q(name__icontains=job)).order_by('-time')[0: 20]
            nextpage = 2
            prepage = 0
            return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage), 'job':job, 'count':len(jobs),'username':username})
        
        jobs = JobInfo.objects.filter(Q(name__icontains=job)).order_by('-time')[(int(prepage)-1)*20: (int(prepage)-1)*20+20]
        nextpage = int(prepage) + 1
        prepage = int(prepage) - 1
        return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage), 'job':job,'username':username})
    
    jobs = JobInfo.objects.filter(Q(name__icontains=job)).order_by('-time')[(int(nextpage)-1)*20: (int(nextpage)-1)*20+20]
    nextpage = int(nextpage) + 1
    prepage = int(nextpage) - 1
    return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(prepage-1), 'job':job, 'count':len(jobs),'username':username})
    
def sort(request):
    
    company_get = request.GET.get('company')
    salary_get = request.GET.get('salary')
    city_get = request.GET.get('city')
    job = request.GET.get('job')
    position = request.GET.get('position')

    citys1 = JobInfo.objects.values('city').distinct()[:16]
    citys2 = JobInfo.objects.values('city').distinct()[16:]
    companys = JobInfo.objects.values('companySize').distinct()
    salarys1 = JobInfo.objects.values('salary').distinct()[:8]
    salarys2 = JobInfo.objects.values('salary').distinct()[16:]


    L = []

    if city_get == None:        
        city = '全国'
        salary = '全部'
        company = '全部'
        positions = Position.objects.filter(position_trade = position)[:30]
        jobs = JobInfo.objects.filter(Q(name__icontains=job))
        return render_to_response('sort.html',{'positions':positions,'jobs':jobs, 'position':position,'job':job,'city':city, 'salary':salary, 'company':company, 'citys1':citys1, 'citys2':citys2, 'companys':companys, 'salarys1':salarys1, 'salarys2':salarys2})
    
    if city_get == '全国':
        city_get = ''

    if salary_get == '全部':
        salary_get = ''

    if company_get == '全部':
        company_get = ''
        
    jobs = JobInfo.objects.filter(Q(name__icontains=job)).filter(Q(city__icontains=city_get)).filter(Q(salary__icontains=salary_get)).filter(Q(companySize__icontains=company_get))
    positions = Position.objects.filter(position_trade = position)[:30]
    
    if city_get == '':
        city_get = '全国'
    
    if salary_get == '':
        salary_get = '全部'
    
    if company_get == '':
        company_get = '全部'
    
    city = city_get
    salary = salary_get
    company = company_get
    return render_to_response('sort.html',{'positions':positions,'jobs':jobs, 'position':position,'job':job,'city':city, 'salary':salary, 'company':company, 'companys':companys, 'citys1':citys1, 'citys2':citys2, 'salarys1':salarys1, 'salarys2':salarys2})


# def click(request):
#     idname = request.GET.get('idname')
#     # url = JobinfoClik.objects.filter(idName = idname)[:1]['url']
#     JobInfoClik.objects.filter(idName = idname).update(clik = F('clik')+1)
#     return redirect('https://m.lagou.com/jobs/'+idname+'.html')


def info(request):
    idname = request.GET.get('idname')
    jobs = JobInfo.objects.filter(idName = idname)
    # url = JobinfoClik.objects.filter(idName = idname)[:1]['url']
    JobInfo.objects.filter(idName = idname).update(clik = F('clik')+1)
    try:
        jianli_name = jianli.objects.all().filter(username = request.session['username'])[:1]
    except Exception:
        return HttpResponseRedirect('/user/login')
    return render_to_response('info.html', {'jobs':jobs, 'jianli_name':jianli_name, 'idname':idname}) 



def tongji(request):
    city_dict = {}
    citys = JobInfo.objects.values('city').distinct()
    for i in citys:
        city_num = len(JobInfo.objects.filter(city = i['city']))
        city_dict[i['city']] = city_num
        t = sorted(city_dict.items(), key =lambda item: item[1], reverse = True)
        city_dict1 = dict(t)
    print(city_dict1)

    city_list = []
    num_list = []
    import matplotlib.pyplot as plt
    import numpy as np
    

    for v in city_dict1.values():
        num_list.append(v)
    for k in city_dict1.keys():
        city_list.append(k)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    fig, ax = plt.subplots()
    x = np.arange(15)
    y= num_list[:15]
    width = 0.25
    # plt.title('city')
    ax.bar(x, y, width, color='r') # 画柱子
    ax.set_xticks(x+width)
    ax.set_xticklabels(city_list[:15])

    fig.savefig("d:/job/static/city.jpg") 
    # fig.show()

    salary_dict = {}
    salarys = JobInfo.objects.values('salary').distinct()
    for i in salarys:
        salary_num = len(JobInfo.objects.filter(salary = i['salary']))
        salary_dict[i['salary']] = salary_num
        t = sorted(salary_dict.items(), key =lambda item: item[1], reverse = True)
        salary_dict1 = dict(t)
    print(salary_dict1)

    salary_list = []
    num_list = []
    import matplotlib.pyplot as plt
    import numpy as np
    
    for v in salary_dict1.values():
        num_list.append(v)
    for k in salary_dict1.keys():
        salary_list.append(k)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    fig, ax = plt.subplots()
    x = np.arange(15)
    y= num_list[:15]
    width = 0.25
    ax.bar(x, y, width, color='r') # 画柱子
    ax.set_xticks(x+width)
    ax.set_xticklabels(salary_list[:15])
    pl.xticks(rotation=270)

    fig.savefig("d:/job/static/salary.jpg") 
    


    # fig.show()

    company_dict = {}
    companys = JobInfo.objects.values('companySize').distinct()
    for i in companys:
        company_num = len(JobInfo.objects.filter(companySize = i['companySize']))
        company_dict[i['companySize']] = company_num
        t = sorted(company_dict.items(), key =lambda item: item[1], reverse = True)
        company_dict1 = dict(t)
    print(company_dict1)

    company_list = []
    num_list = []
    import matplotlib.pyplot as plt
    import numpy as np
    import os
    
    for v in company_dict1.values():
        num_list.append(v)
    for k in company_dict1.keys():
        company_list.append(k)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    
    fig, ax = plt.subplots()
    x = np.arange(len(company_list))
    y= num_list
    width = 0.25
    plt.title('公司规模')
    ax.bar(x, y, width, color='r') # 画柱子
    ax.set_xticks(x+width)
    ax.set_xticklabels(company_list)# 下标注明
    pl.xticks(rotation=30)

    fig.savefig("d:/job/static/company.jpg") 

    L = []
    filelist = os.listdir('d:/job/static')
    for i in filelist:
        if os.path.splitext(i)[1] == ".jpg":
            L.append(i)
    return render_to_response('tongji.html', {'L':L})



    # username = request.user.username
    # type_list = Position.objects.values('position_type', 'position_trade').distinct()
    # name_list = Position.objects.values('position_name', 'position_type')
    # context = {'type_list': type_list, 'name_list': name_list}
    # return render_to_response('index.html', {'jobs': jobs, 'nextpage':str(nextpage), 'prepage':str(perpage)})
      