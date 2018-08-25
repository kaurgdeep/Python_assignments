from django.db import models
import bcrypt,datetime


class UserManager(models.Manager):
    def validate_registration(self, postData):
        response = {
           'status' : False,
           'errors' : []
        }
        if len(postData['first_name']) < 2:
           response['errors'].append("name too short")

  #if len(postData['last_name']) < 2:
          # response['errors'].append("last_name too short")

        if len(postData['email']) < 5:
           response['errors'].append("invalid username")

        if len(postData['password']) < 8:
            response['errors'].append("invalid password")

        if postData['confirm_pw'] != postData['password']:
            response['errors'].append("invalid password")
        if len(postData['date']) > 0:
            today = datetime.datetime.today()
            date = datetime.datetime.strptime(postData['date'], '%Y-%m-%d')
            if date > today:
                response['errors'].append('Date cannot be in the future')
        if len(postData['date']) < 1:
            response['errors'].append('Date required')
        
            

        if len(response['errors']) == 0:
            response['status'] = True
            response['user_id'] = User.objects.create(
                first_name=postData['first_name'],
                #last_name=postData['last_name'],
                email=postData['email'],
                password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            ).id
        return response 

    def validate_login(self, postData):
        response = {
           'status' : False,
           'errors' : []
        }
        #if len(User.objects.filter(eamil=postData['email'])) == 0:
        existing_users = User.objects.filter(email=postData['email'])
        if len(existing_users) == 0:
            response['errors'].append("invalid input")
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
                response['status'] = True
                response['user_id'] = existing_users[0].id
            else:
                response['errors'].append("invalid input")
        return response

class ItemManager(models.Manager):

    def validate_create_item(self,postData):
        response = {
            "status" : False,
            "errors": []
        }
        if len(postData['item']) == 0:
            response['errors'].append("list cannot be empty")
        if len(postData['item']) < 3:
            response['errors'].append("invalid list")

        if len(response['errors']) == 0:
            response['status'] = True
        return response
        

    def addlist(self, item_id, user_id):
        me = User.objects.get(id=user_id)
        item = Item.objects.get(id=item_id)
        print("*******",me.first_name,item.item)

        item.people_wish_item.add(me) 
        item.save() 

    def remove_list(self, item_id, user_id):
        me = User.objects.get(id=user_id)
        item = Item.objects.get(id=item_id)
        item.people_wish_item.remove(me) 
        item.save() 
       

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Item(models.Model):
    item = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    added_by = models.ForeignKey(User, related_name="added_items", null=True)
    people_wish_item = models.ManyToManyField(User, related_name="items", null=True)
    objects = ItemManager()

