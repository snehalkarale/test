
from django.contrib import admin
from django.urls import path
# from mysite.testapp.views import test
# from mysite.testapp import views
# from views import test
from testapp.views import *

urlpatterns = [
    path('test', testview.as_view(), name="testview"),
]


