from django.views.generic import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .util import ImageCodeUtil
from .config import IMG_CODE_SESSION_KEY
# Create your views here.


class ImgCodeApi(View):

    def get(self, request, *args, **kwargs):
        code, image = ImageCodeUtil().gene_code()
        request.session[IMG_CODE_SESSION_KEY] = code.lower()
        return HttpResponse(image, "image/png")
