# import json
from random import randrange, randint
from io import BytesIO

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
# from Jango import settings


def hello(request):

    return HttpResponse("hello verify")


def get_verify(request):
    # 创建画布
    image = Image.new(mode="RGB", size=(200, 100), color=(get_color(), get_color(), get_color()))
    # 创建画笔
    pen = ImageDraw.Draw(image)

    code = [get_code() for _ in range(4)]

    # 绘制验证码
    for i in range(len(code)):
        fill = (get_color(), get_color(), get_color())
        # 随机大小
        font = ImageFont.truetype(font='statics/fonts/consola.ttf', size=randint(70, 130))
        # font = ImageFont.truetype(font=settings.FONT_PATH)
        pen.text(xy=(50*i, 0), text=code[i], font=font, fill=fill)

    # 增加复杂度颜色
    for i in range(8000):
        fill = (get_color(), get_color(), get_color())
        pen.point(xy=(randrange(200), randrange(100)), fill=fill)

    fp = BytesIO()
    image.save(fp, 'png')
    return JsonResponse({'data': fp.getvalue()}, content_type="image/png")


# 随机颜色
def get_color():
    return randrange(256)


# 随机字母
def get_code():
    return chr(randint(65, 90))


def login(request):
    if request.method == "POST":
        pass
    return render(request, 'login.html')
