from django.db import models

# Create your models here.


class Orders(models.Model):
    order_description = models.TextField("Текст заявки")
    date = models.DateField("Дата публикации")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
