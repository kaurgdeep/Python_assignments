from django.db import models
import bcrypt,datetime


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
           response['errors'].append("Invalid username")

        if len(postData['password']) < 8:
            response['errors'].append("Invalid Password")

        if postData['confirm_pw'] != postData['password']:
            response['errors'].append("Invalid Password")

        # if len(postData['date']) > 0:
        #     today = datetime.datetime.today()
        #     date = datetime.datetime.strptime(postData['date'], '%Y-%m-%d')
        #     if date > today:
        #         response['errors'].append('Date Hired cannot be in the future')
        # if len(postData['date']) < 1:
        #     response['errors'].append('Date Hired required')


            

        if len(response['errors']) == 0:
            response['status'] = True
            response['user_id'] = User.objects.create(
                name=postData['name'],
                #last_name=postData['last_name'],
                username=postData['username'],
                password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            ).id
        return response 

    def validate_login(self, postData):
        response = {
           'status' : False,
           'errors' : []
        }
        #if len(User.objects.filter(eamil=postData['email'])) == 0:
        existing_users = User.objects.filter(username=postData['username'])
        if len(existing_users) == 0:
            response['errors'].append("invalid input")
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
                response['status'] = True
                response['user_id'] = existing_users[0].id
            else:
                response['errors'].append("invalid input")
        return response  

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    #last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()