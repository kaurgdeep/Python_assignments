from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages, sessions
from django.db.models import Q
import bcrypt

def index(request):
	print ('*****')
	print ('made it to index page')
	print ('*****')
	return redirect('/main')

def main(request):
	print ('*****')
	print ('made it to index page - main url')
	print ('*****')
	return render(request, 'friends_app/index.html')

def processReg(request):
	print ('*****')
	print ('processing registration')
	print ('*****')
	errors = User.objects.registration_validator(request.POST)
	if len(errors):
		print (errors)
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		hashedPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

		new_user = User.objects.create(
			name=request.POST['name'],
			alias=request.POST['alias'],
			email=request.POST['email'],
			password=hashedPW,
			birthday=request.POST['birthday']
			)
	request.session.modified = True

	request.session['user_id'] = new_user.id
	request.session['name'] = request.POST['name']
	request.session['alias'] = request.POST['alias']
	request.session['email'] = request.POST['email']
	return redirect('/friends')

def processLog(request):
	print ('*****')
	print ('processing login')
	print ('*****')
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.items():
			messages.error(request, error, extra_tags=tag)
			return redirect('/')
	else:
		me = request.POST['alias']
		my_user_object = User.objects.get(alias=me)
		request.session.modified = True
		request.session['user_id']= my_user_object.id #stores REGISTERED user in session
		request.session['name'] = my_user_object.name
		request.session['alias'] = me
		request.session['email'] = my_user_object.email
		return redirect('/friends')

def friends(request):
	print ('*****')
	print ('made it to friends dashboard page')
	print ('*****')
	me = request.session['alias']
	my_id = request.session['user_id']
	my_user_object = User.objects.get(id=my_id)

	my_friends = Friend.objects.filter(requester=my_id)
	print(my_friends)
	not_friends = Friend.objects.exclude(requestee=my_id)
	print(not_friends)
# .difference() subtract q set from other q set
	friend_id = []
	print(friend_id)
	for user in my_friends:
		friend_id.append(user.requestee.id)
	context = {
		'users': User.objects.all(),
		'friends': Friend.objects.all(),
		'my_friends': User.objects.filter(id__in=friend_id),
		'not_my_friends': User.objects.exclude(id__in=friend_id),
	}
	return render(request, 'friends_app/friends.html', context)

def addFriend(request, user_id, id):
	print ('*****')
	print ('adding friend')
	print ('*****')
	friend_id = id
	Friend.objects.addFriend(user_id, friend_id)
	return redirect('/friends')

def unfriend(request, user_id, id):
	print ('*****')
	print ('removing friend')
	print ('*****')
	friend_id = id
	Friend.objects.unfriend(user_id, friend_id)
	return redirect('/friends')

def users(request, user_id):
	print ('*****')
	print ('made it to users profile page')
	print ('*****')
	context = {
		'user': User.objects.get(id=user_id)
	}
	return render(request, 'friends_app/users.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')
