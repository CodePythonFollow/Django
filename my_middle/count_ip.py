import time

from django.core.cache import caches
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class CountIp(MiddlewareMixin):
    def process_request(self, request):
        # for key in request.META:
        #     print(key, request.META[key])
        ip = request.META.get("REMOTE_ADDR", "错误")
        now_time = self.get_time()
        arr = caches['default'].get(ip, [])
        arr.append(now_time)
        caches['default'].set(ip, arr)

        if len(arr) >= 10:
            if now_time - arr[-10] < 60:
                return HttpResponse("小爬虫你被封了", status=300)







        # print(arr)
        # if now_time - arr[-10] <
        #     return HttpResponse("小爬虫你被封了")
        # print('正常')

    def get_time(self):
        return time.time()

