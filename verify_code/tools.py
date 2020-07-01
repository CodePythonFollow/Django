# 随机颜色
from random import randint, randrange


def get_color():
    return randrange(256)


# 随机字母
def get_code():
    return chr(randint(65, 90))