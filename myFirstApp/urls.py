from django.conf.urls import url

from myFirstApp import views

urlpatterns=[
    url(r'^$',views.last_page,name="Last Page"),
    url(r'1/',views.start_page,name="Last First"),
    url(r'2/',views.start_page,name="Last Second"),
    url(r'3/',views.start_page,name="Last Third"),
]
