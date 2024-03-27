from django.shortcuts import redirect, render

from dj2app.models import Employee, Department


def index(req):
    from dj2 import urls

    us = urls.urlpatterns
    us = map(lambda x: "/" + str(x.pattern), us)
    return render(req, "index.html", {"urls": us})


def dept_list(req):
    dt = Department.objects.all()
    return render(req, "dept_list.html", {"uarr": dt})


def dept_add(req):
    if req.method == "GET":
        return render(req, "dept_add.html")
    else:
        uname = req.POST.get("name")
        Department.objects.create(name=uname)
        return redirect("/dept/list")


def dept_delete(req):
    did = req.GET.get("id")
    Department.objects.filter(id=did).delete()
    return redirect("/dept/list")


def dept_edit(req, id):
    dt = Department.objects.filter(id=id).first()
    if req.method == "GET":
        return render(req, "dept_edit.html", {"dt": dt})
    else:
        nname = req.POST.get("name")
        Department.objects.filter(id=id).update(name=nname)
        return redirect("/dept/list")


def emp_list(req):
    dt = Employee.objects.all()
    return render(req, "emp_list.html", {"uarr": dt, "sexarr": Employee.gender_choices,"deparr":Department.objects.all()})


def emp_add(req):
    if req.method == "GET":
        return render(req, "emp_add.html")
    else:
        uname = req.POST.get("name")
        Employee.objects.create(name=uname)
        return redirect("/emp/list")


def emp_delete(req):
    did = req.GET.get("id")
    Employee.objects.filter(id=did).delete()
    return redirect("/emp/list")


def emp_edit(req, id):
    dt = Employee.objects.filter(id=id).first()
    if req.method == "GET":
        return render(req, "emp_edit.html", {"dt": dt})
    else:
        nname = req.POST.get("name")
        Employee.objects.filter(id=id).update(name=nname)
        return redirect("/emp/list")
