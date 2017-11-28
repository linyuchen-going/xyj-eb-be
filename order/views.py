from rest_api.rest_api_views import LycApiBaseView
from .serializers import ProductOrderSerializer
from .models import ProductOrder


class ProductOrdersApi(LycApiBaseView):
    model_class = ProductOrder
    serializer_class = ProductOrderSerializer
    http_method_names = ["get"]
    auth_http_method_names = ["get"]

    def get_queryset(self):
        user = self.request.user
        queryset = self.model_class.objects.filter(user=user)
        return queryset
