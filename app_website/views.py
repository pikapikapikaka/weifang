from django.shortcuts import render, redirect
from django.http import HttpResponse
import time, os
from . import models

"""
 django.http模块中定义了HttpResponse 对象的API
 作用：不需要调用模板直接返回数据
 HttpResponse属性：
    content: 返回内容,字符串类型
    charset: 响应的编码字符集
    status_code: HTTP响应的状态码
"""

"""
hello 为一个视图函数，每个视图函数必须第一个参数为request。哪怕用不到request。
request是django.http.HttpRequest的一个实例
"""


def index(request):
    pics = models.pic.objects.all()
    context = {
        'result': True,
        'reason': '',
        'name': '',
        'phone': '',
        'comment': '',
        "pics": pics,
    }
    return render(request, 'index.html', context)


def product(request):
    pics = models.pic.objects.all()
    context = {'pics': pics}
    return render(request, 'product.html', context)


def contact(request):
    context = {
        'result': True,
        'reason': '',
        'name': '',
        'phone': '',
        'comment': '',
    }
    return render(request, 'contact.html', context)


def post_comment(request):
    context = {
        'result': False,
        'reason': '数据不能为空',
        'name': '',
        'phone': '',
        'comment': '',
    }
    name = request.POST.get('name').strip()
    phone = request.POST.get('phone').strip()
    comment = request.POST.get('comment').strip()
    if name == "" or phone == "" or comment == "" or len(name) > 10:
        context['name'] = name
        context['phone'] = phone
        context['comment'] = comment
        return render(request, 'contact.html', context)

    try:
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        data = models.userinfo(name=name, phone=phone, comment=comment, time=date)
        data.save()
        context['result'] = True
        context['reason'] = '留言成功'
    except:
        context['reason'] = '留言提交失败，请再次提交'
        context['name'] = name
        context['phone'] = phone
        context['comment'] = comment

    return render(request, 'contact.html', context)


def login(request):
    context = {
        "reason": "",
    }
    return render(request, 'login.html', context)


def check(request):
    context = {
        "reason": "用户名或者密码错误",
    }
    name = request.POST.get('name', '').strip()
    password = request.POST.get('password', '').strip()
    # 用户名密码不正确
    if name != 'admin' or password != 'admin':
        return render(request, 'login.html', context)

    context['reason'] = "恭喜您答对了"
    return show_pic(request)


def show_pic(request):
    pics = models.pic.objects.all()
    context = {'pics': pics}
    return render(request, 'manage_pic.html', context)


def add_pic(request):
    context = {}
    print("method:", request.method)
    if request.method == "POST":  # 请求方法为POST时，进行处理
        img_url = request.FILES.get('img', None)  # 获取上传的文件，如果没有文件，则默认为None
        if not img_url:
            context['reason'] = '无法发现文件'
            return render(request, 'manage_pic.html', context)
        name = request.POST.get('name', '')
        data = models.pic(name=name, img_url=img_url)
        data.save()
        return redirect('show_pic')
    else:
        context['reason'] = '上传失败,请重试'
        return render(request, 'manage_pic.html', context)


def delete_pic(request):
    id = request.GET.get('qid', -1)
    print('item:', request.GET.get('qid', -1))
    models.pic.objects.filter(id=id).delete()
    return redirect('show_pic')
