from django.db import models

# Create your models here.
class Vehicles(models.Model):
    title=models.CharField(max_length=20,unique=True,primary_key=True,db_column='Title')
    description=models.TextField(max_length=254,db_column='Description')

    def __str__(self):
        return self.title

class Saless(models.Model):
    name=models.CharField(max_length=254,primary_key=True,db_column='Name')
    company=models.ForeignKey(Vehicles,on_delete=models.DO_NOTHING,db_column='Company')
    year=models.IntegerField(db_column='Year')

    def __str__(self):
        return self.name

class UserList(models.Model):
    user=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30,null=False)

    class Meta:
        managed=False
        db_table='user_list'

    def __str__(self):
        return self.user

class User(models.Model):
    name=models.TextField(primary_key=True)
    age=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=20,blank=True,null=True)
    nationality=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed=False
        db_table='users'
