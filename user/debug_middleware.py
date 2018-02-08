# -*- coding: UTF8 -*-
from django.utils.deprecation import MiddlewareMixin
from xxj_EB.settings import DEBUG
from user.models import User


class DebugMiddleWare(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        """

        :param request:
        :return:
        """
        if DEBUG:
            # request.user = User.objects.first()
            pass
