from django.shortcuts import render

from dj2app.models import Employee

def index(req):
    from dj2 import urls
    us = urls.urlpatterns
    us=map(lambda x:'/'+str(x.pattern),us)
    return render(req,"index.html",{'urls':us})


def dept_list(req):
    dt = Employee.objects.all()
    return render(req, "dept_list.html", {"uarr": dt})