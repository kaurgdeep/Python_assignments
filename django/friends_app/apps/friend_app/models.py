from django.db import models
import bcrypt


class UserManager(models.Manager):
    def validate_registration(self, postData):
        response = {
           'status' : False,
           'errors' : []
        }
        if len(postData['name']) < 2:
           response['errors'].append("Name too short")

        #if len(postData['last_name']) < 2:
           #response['errors'].append("last_name too short")

        if len(postData['username']) < 5:
           response['errors'].append("invalid username")

        if len(postData['password']) < 8:
            response['errors'].append("invalid password")

        if postData['confirm_pw'] != postData['password']:
            response['errors'].append("invalid password")
            

        if len(response['errors']) == 0:
            response['status'] = True
            response['user_id'] = User.objects.create(
                first_name=postData['name'],
                #last_name=postData['last_name'],
                email=postData['username'],
                password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            ).id
        return response 

    def validate_login(self, postData):
        response = {
           'status' : False,
           'errors' : []
        }
        #if len(User.objects.filter(eamil=postData['email'])) == 0:
        existing_users = User.objects.filter(email=postData['username'])
        if len(existing_users) == 0:
            response['errors'].append("invalid input")
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
                response['status'] = True
                response['user_id'] = existing_users[0].id
            else:
                response['errors'].append("invalid input")
        return response    

          

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
