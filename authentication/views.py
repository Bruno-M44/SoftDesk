from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from authentication.serializers import SignupSerializer


class SignupView(APIView):
    def get(self, *args, **kwargs):
        users = User.objects.all()
        serializer = SignupSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        serializer = SignupSerializer()
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
