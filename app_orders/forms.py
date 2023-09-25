from django.forms import ModelForm, Textarea, HiddenInput
from datetime import datetime
from .models import Orders


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = [
            "order_description",
            "date",
        ]
        widgets = {
            "order_description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Чтобы подать заявку выполните первый шаг.",
                    "rows": "5",
                }
            ),
            "date": HiddenInput(
                attrs={
                    "value": datetime.today().strftime("%Y-%m-%d"),
                }
            ),
        }
