from django.db import models

# Create your models here.

class Code(models.Model):
    code_string = models.TextField(
        "Код",
        blank=False,
    )
    generation_time = models.DateTimeField(
        "Когда создан",
        blank=False,
    )
    
    def __str__(self):
        return self.code_string
    
    class Meta:
        verbose_name="Проверочный код"
        verbose_name_plural = "Проверочные коды"