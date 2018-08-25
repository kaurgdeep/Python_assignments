# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt, datetime, random

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z\s]\w+')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        # name
        if len(postData['name']) < 3:
            errors['name'] = 'Name should be at least 3 characters'
        if not re.match(NAME_REGEX, postData['name']):
            errors['name_format'] = 'Name must contain letter characters only'
        # alias
        if User.objects.filter(alias=postData['alias']).count() > 0:
            errors['existing_alias'] = f"Alias {postData['alias']} already exists"
        if len(postData['alias']) <3:
            errors['alias'] = 'alias must be at least 3 characters'
        # email
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_format'] = "Wrong email format"
        if User.objects.filter(email=postData['email']).count() > 0:
            errors['email'] = f"Email {postData['email']} already exists"
        # password
        if len(postData['password']) < 8:
            errors['password_length'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirmPW']:
            errors['confirmPW'] = 'Passwords do not match'
        # date of birth
        if len(postData['birthday']) > 0:
            today = datetime.datetime.today()
            birthday = datetime.datetime.strptime(postData['birthday'], '%Y-%m-%d')
            if birthday > today:
                errors['birthday'] = 'Birthday cannot be in the future yo'
        if len(postData['birthday']) < 1:
            errors['birthday'] = 'Date of birth required'

        return errors

    def login_validator(self, postData):
        print ('made it to log login_validator')

        errors = {}
        email = postData['email']
        alias = postData['alias']
        password = postData['password']

        existing_user_list = User.objects.filter(email=email,alias=alias)
        if len(existing_user_list) > 0:
            if bcrypt.checkpw(password.encode(), (existing_user_list[0].password).encode()):
                return errors
        errors['login_error'] = 'Must enter valid alias/email/password combo'
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return f'<User object: {self.name} {self.alias} {self.password} {self.email} {self.birthday} {self.created_at} {self.updated_at}>'

class FriendManager(models.Manager):

    def addFriend(self, user_id, friend_id):     #in models or views?
        me = User.objects.get(id=user_id)
        friend = User.objects.get(id=friend_id)
        Friend.objects.create(
            requester = me,
            requestee = friend
        )
        Friend.objects.create(
            requester = friend,
            requestee = me
        )

    def unfriend(self, user_id, friend_id):
        me = User.objects.get(id=user_id)
        friend = User.objects.get(id=friend_id)
        Friend.objects.get(requester=me, requestee=friend).delete()
        Friend.objects.get(requester=friend, requestee=me).delete()

class Friend(models.Model):
    requester = models.ForeignKey(User, related_name="who_requested")
    requestee = models.ForeignKey(User, related_name='who_received')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = FriendManager()

    def __repr__(self):
        return f'<User object: {self.requester} {self.requestee} {self.created_at} {self.updated_at}>'
