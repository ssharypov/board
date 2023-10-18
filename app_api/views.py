from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import datetime
from pprint import pprint

from . import models

class CodeSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Code
        fields = ['code_string', 'generation_time']
        
class CodeView(APIView):
    def get(self, *args, **kwargs):
        code = models.Code.objects.get(pk=1)
        pprint(code)
        serialized_code = CodeSerializator(code, many=False)
        return Response(serialized_code.data)
        
