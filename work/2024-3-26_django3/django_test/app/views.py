from django.shortcuts import render, HttpResponse, redirect

from app.models import UserInfo

def index(req):
    from django_test import urls
    us = urls.urlpatterns
    us=map(lambda x:'/'+str(x.pattern),us)
    return render(req,"index.html",{'urls':us})


def test(req):
    arr = [1, 2, 3, 4, 5, {"name": "小华"}, {"a": "a", "b": "b", "c": "c"}]
    drt = {"a": "a", "b": "b", "c": "c"}
    return render(req, "test.html", {"name": "徐远钜", "arr": arr, "drt": drt})

    # print(req.method)
    # print(req.GET)

    # import requests
    # r=requests.get("http://111.22.69.99:58080/guide/06.html#%E8%AF%BE%E7%A8%8B%E8%AE%A1%E5%88%92")
    # # return HttpResponse('r.text')
    # return redirect("http://www.baidu.com")


def user_add(req):
    if req.method == "GET":
        return render(req, "user_add.html")
    else:
        uname = req.POST.get("username")
        upsw = req.POST.get("password")
        uage = req.POST.get("age")
        UserInfo.objects.create(username=uname, password=upsw, age=int(uage))
        return redirect("/user/list")
    

def user_delete(req):
    uid=req.GET.get("id")
    UserInfo.objects.filter(id=uid).delete()
    return redirect("/user/list")


def user_list(req):
    dt = UserInfo.objects.all()
    return render(req, "user_list.html", {"uarr": dt})


def login(req):
    if req.method == "GET":
        return render(req, "login.html")
    else:
        uname = req.POST.get("username")
        upsw = req.POST.get("password")
        dt = UserInfo.objects.filter(username=uname).first()
        if dt != None and upsw == dt.password:
            return redirect("/index")
        else:
            return render(req, "login.html", {"err": "用户名或密码错误"})
            # return redirect('/login')
