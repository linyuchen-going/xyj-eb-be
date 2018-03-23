# -*- coding: UTF8 -*-
from django.http.response import HttpResponseRedirect


def main(request):
    # print(request.build_absolute_uri())
    return HttpResponseRedirect("/static/fe/index.html")
