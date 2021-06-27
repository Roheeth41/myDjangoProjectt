from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import User

cursor = connection.cursor()
cursor.execute('''SELECT USER FROM user_list''')
row = cursor.fetchall()

def db_connection_fetch(connection,query):
    with connection.cursor() as con:
        con.execute(query)
        rows = con.fetchone()
    return rows

def home_page(_):
    password='RK12'
    query='''select password from user_list where user= 'Roheeth' '''
    val,=db_connection_fetch(connection,query)
    if val == password:
        return render(_,'myFirstApp/index.html')
    else:
        return HttpResponse("Invalid Credentials")

def start_page(_):
    return HttpResponse("Hey You are just starting")

def last_page(_):
    return HttpResponse("Bye")

def index(request):
    user_data=User.objects.all() #get the data from database
    user_records={'User_Records':user_data}
    return render(request,'myFirstApp/index.html')
