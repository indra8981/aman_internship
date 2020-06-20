from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer

import json


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return HttpResponse(json.dumps({"ok": True, "members": serializer.data}), content_type='application/json')
