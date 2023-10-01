from django.db import models

# Create your models here.


class Orders(models.Model):
    order_description = models.TextField("Текст заявки", blank=False)
    date = models.DateField("Дата публикации")

    def __str__(self):
        return self.order_description

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
