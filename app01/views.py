import uuid

from django.shortcuts import render
from aip import AipFace
from app01 import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse("欢迎使用")
    return render(request, 'index.html')  # 渲染一个指定的HTML模板


# 博客页面
def blog(request):
    return render(request, 'blog/blog.html')


def jishu1(request):
    return render(request, 'blog/jishu1.html')


def jishu2(request):
    return render(request, 'blog/jishu2.html')


def jishu3(request):
    return render(request, 'blog/jishu3.html')


# 场景展示

def about(request):
    return render(request, 'scene/about.html')


def Author(request):
    return render(request, 'blog/Author.html')


def link(request):
    return render(request, 'link/link.html')


def digital(request):
    return render(request, 'scene/digital.html')


def profile(request):
    return render(request, 'scene/profile.html')


def front(request):
    return render(request, 'scene/front.html')


def rear(request):
    return render(request, 'scene/rear.html')


def service(request):
    return render(request, 'scene/service.html')


def AI(request):
    return render(request, 'scene/AI.html')


def login(request):
    """
    :param request:
    :return:
    :author:何晓辉
    :time:2023/6/23
    :function: 登录功能
    """
    if request.method == 'POST':
        # 1.获取请求参数
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # 2.封装数据库中的数据
            user = models.User.objects.get(username=username, password=password)

            # 3.判断用户表单中的数据是否与数据库中的数据相同
            if user.username == username and user.password == password:
                # 将数据库中的用户信息存到键为loginUser中
                request.session["loginUser"] = user.username
                # 获取键为loginUser的值 赋给变量msg
                msg = request.session.get('loginUser')
                # 如果相同返回首页
                return render(request, "index.html", {"msg": msg})
        except:
            # 必须执行设置提示错误 key:values)
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
        # 最后路由返回登录页面
    return render(request, "login.html")


def regist(request):
    """
    :param request:
    :return:
    :author:何晓辉
    :time:2023/6/14
    :function: 注册功能
    """
    # 代码功能上同
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = models.User.objects.get(username=username)
            if user.username == username:
                return render(request, 'regist.html', {"error_msg": "用户名已存在"})

        except:
            # 创建新的数据信息
            new_user = models.User.objects.create()
            new_user.username = username
            new_user.password = password
            new_user.save()
            return render(request, 'regist.html', {"success_msg": "注册成功"})

    return render(request, "regist.html")


def loginout(request):
    """
    :param request:
    :return:
    :author:何晓辉
    :time:2023/6/23
    :function: 退出功能
    """
    # 获取键为loginUser的值
    if request.session.get("loginUser"):
        # 清除服务器中的用户信息
        del request.session["loginUser"]
    return render(request, 'index.html')


@csrf_exempt  # 取消跨站请求伪造（CSRF）防护。
def face_login(request):
    """
    :param request:
    :return: result:
    :author:何晓辉
    :time:2023/10/27
    :function: 人脸登录
    """
    appId = "34607829"
    apiKey = "fpTIlzsvLc1nSgOBhluhuyM1"
    secretKey = "GV4AHDUy4hFSfOT8QVNYe8sHrsNuW5es"
    imageType = "BASE64"
    # 前期用户申请的百度API的关键码
    client = AipFace(appId, apiKey, secretKey)
    # 初始化AipFace对象
    imageData = request.POST.get("imageData")  # 获取前端AJAX的图像数据
    # print(imageData)
    options = {"max_face_num": 1, "face_field": 'age,beauty,gender,emotion'}  # 设置请求参数
    result = client.detect(imageData, imageType, options)  # 调用人脸检测函数 有参:options
    print(result)
    # print("年龄为:{}".format(result["result"]["face_list"][0]["age"]))
    # print("颜值打分:{}".format(result["result"]["face_list"][0]["beauty"]))
    # print("性别:{}".format(result["result"]["face_list"][0]["gender"]["type"]))
    # print("情绪:{}".format(result["result"]["face_list"][0]["emotion"]["type"]))
    if result["error_msg"] in "SUCCESS":
        mr = models.Group.objects.all()  # 获取数据库中的用户信息
        for i in range(models.Group.objects.count()):
            user_obj = mr[i]
            face_list = user_obj.userFace
            mr1 = {'image': face_list, 'image_type': imageType}
            mr2 = {'image': imageData, 'image_type': imageType}
            faceList = [mr1, mr2]
            matchResult = client.match(faceList)
            print(matchResult)
            if matchResult["error_msg"] in "SUCCESS":
                score = matchResult['result']['score']

                if score > 60:
                    result["face_login"] = "SUCCESS"
                    result["match_success_username"] = user_obj.username
                    result["user_age"] = result["result"]["face_list"][0]["age"]
                    result["user_beauty"] = result["result"]["face_list"][0]["beauty"]
                    result["user_gender"] = result["result"]["face_list"][0]["gender"]["type"]
                    result["user_emotion"] = result["result"]["face_list"][0]["emotion"]["type"]
                    break

    return JsonResponse(result)


def faceReg(request):
    return render(request, 'face/face_regist.html')


@csrf_exempt
def face_reg(request):
    """
       :param request:
       :return: result:
       :author:何晓辉
       :time:2023/10/27
       :function: 人脸录入
    """
    appId = "34607829"
    apiKey = "fpTIlzsvLc1nSgOBhluhuyM1"
    secretKey = "GV4AHDUy4hFSfOT8QVNYe8sHrsNuW5es"
    imageType = "BASE64"
    client = AipFace(appId, apiKey, secretKey)
    reg_message = models.Group.objects.all()
    user_message = models.User.objects.last()
    username = user_message.username
    password = user_message.password
    all_message = models.User.objects.all()
    group_id = str(reg_message.count() // 5)
    user_id = str(all_message.count())
    imageData = request.POST.get("imageData")
    options = {"max_face_num": 10}
    result = client.detect(imageData, imageType, options)
    print(result)
    if result["error_msg"] in "SUCCESS":
        reg = client.addUser(imageData, imageType, group_id, user_id)
        # print(reg)
        if reg['error_code'] == 0:
            result["face_reg"] = "SUCCESS"
            models.Group.objects.create(user_id=user_id, username=username, password=password,
                                        group_id=group_id, count=reg_message.count() + 1, userFace=imageData)
    return JsonResponse(result)


def user_list(request):
    return render(request, 'user/user_list.html')
