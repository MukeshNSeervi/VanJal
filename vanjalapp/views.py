from django.shortcuts import render,redirect
from datetime import datetime
from . import functions
from django.http import HttpResponse
import re

# Create your views here.
def index(request):
	"""
	This is the First page of the Project!!!
	"""
	request.session['d'] = False
	return render(request,'vanjalapp/index.html')

def login(request):
	"""
	This is the login page which retrives the information from the browser give by
    the user and compraes with the signup page for gmail and passord!!!"""	
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		authen = functions.checklogin(email,password)
		if authen == False:
			return render(request,'vanjalapp/error.html',{'d':'looks like your email-id or password is wrong!!'})
		else:
			username = email[:email.find('@')]
			authen = authen.strip()
			t = str(datetime.now())[11:13]
			da = int(t)
			if da >= 12 and da <= 16:
				t = 'Good Afternoon'
			elif da < 12:
				t = 'Good Morning'
			else:
				t = 'Good Evening'
			d = {'state':authen,'username':username,'t':t}
			request.session['d']=d
			return render(request,'vanjalapp/loginIndex.html',request.session.get('d'))
	else:
		return render(request,'vanjalapp/login.html')

def register(request):
	"""
	This is  for registration form people who hav not registered!!! 
	cant complain or checks about their state condition!!"""
	if request.method == 'POST':
		email    = request.POST.get('email')
		password = request.POST.get('password')
		name     = request.POST.get('name')
		state    = request.POST.get('state')
		check_email = functions.signup(email,password,name,state)
		if check_email == False:
			return render(request,'vanjalapp/error.html',{'d':'looks like this email-id already exist please choose different!!'})
		else:
		 	return redirect('http://127.0.0.1:8000/index/login')
	else:
		return render(request,'vanjalapp/register.html')

def loginIndex(request):
	"""
	The Page after the Login
	"""
	t = {'t':str(datetime.now())}
	if request.session.get('d'):
		return render(request,'vanjalapp/loginIndex.html',request.session.get('d'))
	return HttpResponse("Login First...!")

def about(request):
	"""
	this page contains the content of the particular state
	"""
	if request.session.get('d'):
		return render(request,'vanjalapp/about.html',{'d':request.session.get('d'),'file':open('files/{}.txt'.format(request.session['d']['state'])).read()})

def trees(request):
	"""
	This page contains about the trees and anyone add about it!!!
	"""
	if request.method == 'POST':
		about = request.POST.get('about')
		with open("files\\trees.txt",'a') as f:
			f.write('\n'+"<P>"+about+"<P>"+'\n')
		return render(request,'vanjalapp/tree.html',{'d':open('files/trees.txt').read()})
	else:
		return render(request,'vanjalapp/tree.html',{'d':open('files/trees.txt').read()})

def water(request):
	"""
	This Page contains about Water and anyone can add about it!!!!
	"""
	if request.method == 'POST':
		about = request.POST.get('about')
		with open("files/water.txt",'a') as f:
			f.write('\n'+"<P>"+about+"<P>"+'\n')
		return render(request,'vanjalapp/water.html',{'d':open('files/water.txt').read()})
	else:
		return render(request,'vanjalapp/water.html',{'d':open('files/water.txt').read()})

def air(request):
	"""
	This page contains about Air and anyone can add about it!!
	"""
	if request.method == 'POST':
		about = request.POST.get('about')
		with open("files/air.txt",'a') as f:
			f.write('\n'+"<p>"+about+"</p>"+'\n')
		return render(request,'vanjalapp/air.html',{'d':open('files/air.txt').read()})
	else:
		return render(request,'vanjalapp/air.html',{'d':open('files/air.txt').read()})
def error(request):
	"""
	Error Page if the gmail already exist or if anything is wrong during login!!!!
	"""
	return render(request,'vanjalapp/error.html')	
def addAboutPage(request):
	"""
	A user can add About their Projects!!!!
	"""
	if request.method == 'POST':
		about = request.POST.get('about')
		name = request.session['d']['username']
		with open("files\\{}.txt".format(request.session['d']['state']),'a') as f:
			f.write('<h1>'+ name +'</h1>'+"<h3>"+about+"</h3>"+'\n')
		return redirect('http://127.0.0.1:8000/index/loginIndex/')
		#return render(request,'vanjalapp/about.html',{'file':open('files/{}.txt'.format(request.session['d']['state'])).read()})
	else:
		return render(request,'vanjalapp/addAboutPage.html')
#href = "{% url 'oxyVanJal:name of the url' %}"

def complaints(request):
	if request.method == 'POST' and request.session.get('d'):
		with open('files/complaints.txt','a') as f:
			f.write()

	return render(request,"vanjalapp/complaints.html",request.session.get('d'))
def govLogin(request):
	if request.method == 'POST':
		s = request.POST.get('name')
		password = request.POST.get('password')
		state_name = s.title()
		f =  open('files/{}.txt'.format(state_name)).read() 
		return render(request,'vanjalapp/Complaints.html',{'file':f})
	else:
		return render(request,'vanjalapp/govLogin.html')
# def govLogin(request):
# 	if request.method == 'POST':
# 		state_name = title(request.POST.get('name'))
# 		password = request.POST.get('password')
# 		if password == 'modi' :
# 			with open('files/complaints.txt') as f:
# 				for each_line in f.readlines():
# 					if state_name == each_line[:each_line.find('|')]:
# 						with open('files/temp.txt','a') as f:
# 							write = each_line[each_line.find('|'):]
# 							f.write('<p>'+write+'</p>'+'\n')
# 			return render(request,'vanjalapp/getcomplaints.html',{'c':open('files/temp.txt').read()})
# 	else:
# 		return render(request,'vanjalapp/govLogin.html')

def getcomplaints(request):
	if request.session.get('d'):
		return render(request,'vanjalapp/getcomplaints.html')

def user(request):
	if request.method == 'POST' and request.session.get('d'):
		new_state_name = request.POST.get('state')
		with open("files/signup.txt",'a') as f:
			for each_line in f.readlines():
				if request.session['d']['username'] == each_line[:each_line.find('@')]:
					f = each_line[each_line.find('|'):]
					s = each_line[each_line.find('|',f+1):]
					t = each_line[each_line.find('|'),s+1:]
					t = new_state_name
					l = len(t)
					each_line = each_line[:l]+t
					f.write(each_line)
					request.session['d']['state'] = new_state_name 
		return render(request,'vanjalapp/loginIndex.html',request.session.get('d'))
	else:
		with open('files/{}.txt'.format(request.session['d']['state'])) as f:
				for my_complaints in f.readlines():
					if request.session['d']['username'] in my_complaints:
						with open('files/temp.txt','w')	as t:
							t.write(my_complaints)
					else:
						with open('files/temp.txt','w') as t:
							t.write(" ")
					h = open('files/temp.txt').read()
		return render(request,'vanjalapp/user.html',request.session.get('d'),{'h':h})