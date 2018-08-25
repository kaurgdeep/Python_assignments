from __future__ import unicode_literals
from django.db import models
# Create your models here.
class dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<dojo object: {} {} {}>".format(self.name, self.city, self.state)


class ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    dojo = models.ForeignKey(dojo, related_name = "ninjas")
    def __repr__(self):
        return "<ninja object: {} {}>".format(self.first_name, self.last_name)

    