from django.db import models
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    first_pay_price = models.FloatField()  # 首付/定金金额
    # end_price = models.FloatField()  # 尾款金额
    stock = models.IntegerField()
    create_time = models.DateTimeField(default=timezone.now)
    describe = models.TextField()  # HTML代码
    cover = models.ForeignKey("image.Image")
    images = models.ManyToManyField("image.Image", related_name="images_product", blank=True)
