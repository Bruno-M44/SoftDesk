from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from authentication.serializers import SignupSerializer


class SignupViewset(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]

    def get_queryset(self):
        return User.objects.all()
