# -*- coding: UTF8 -*-
from django.http.response import HttpResponseRedirect


def main(request):
    return HttpResponseRedirect("/static/fe/index.html")
