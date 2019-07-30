from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from index.models import JobInfo


# Create your views here.
def loginView(request):
	title = '登录'
	unit_2 = '/user/register'
	unit_2_name = '立即注册'
	unit_1 = '/user/setpassword'
	unit_1_name = '修改密码'
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		if User.objects.filter(username = username):
			user = authenticate(username = username, password = password)
			if user:
				if user.is_active:
					login(request, user)
					request.session['username'] = username
					JobInfo.objects.update(status = 0)
				return redirect('/')
			else:
				tips = '账号密码错误，请重新输入'
		else:
			tips = '用户名不存在， 请注册'
	return render(request, 'user.html', locals())

def registerView(request):
	title = '注册'
	unit_2 = '/user/login'
	unit_2_name = '立即登录'
	unit_1 = '/user/setpassword'
	unit_1_name = '修改密码'
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		if User.objects.filter(username = username):
			tips = '用户已存在'
		else:
			user = User.objects.create_user(username=username, password = password)
			user.save()
			tips = '注册成功，请登录'
	return render(request, 'user.html', locals())

def setpasswordView(request):
		title = '登录'
		unit_2 = '/user/login'
		unit_2_name = '立即登录'
		unit_1 = '/user/register'
		unit_1_name = '立即注册'
		new_password = True
		if request.method == 'POST':
			username = request.POST.get('username', '')
			old_password = request.POST.get('password', '')
			new_password = request.POST.get('new_password', '')
			if User.objects.filter(username = username):
				user = authenticate(username = username, password = old_password)
				user.set_password(new_password)
				user.save()
				tips = '密码修改成功'
			else:
				tips = '用户不存在'
		return render(request, 'user.html', locals())

def logoutView(request):
	logout(request)
	return redirect('/')	