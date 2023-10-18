from django.db import models

# Create your models here.



class Customers(models.Model):
    tlg_id = models.DecimalField(
        "Телеграм ID",
        blank=False,
        decimal_places=4,
        max_digits=25,
    )
    tlg_contact = models.DecimalField(
        "Номер телефона",
        blank=False,
        decimal_places=11,
        max_digits=15,
    )
    nickname = models.TextField(
        "Имя заказчика",
    )
    
    def __str__(self):
        return self.nickname
    
    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"
class Orders(models.Model):
    order_description = models.TextField(
        "Текст заявки",
        blank=False,
    )
    date = models.DateField(
        "Дата публикации",
    )
    approved = models.BooleanField(
        "Подтверждено",
        default=False,
        blank=False,
        null=False,
    )
    author = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_description

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"