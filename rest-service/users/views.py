from rest_framework import generics # type: ignore
from .models import User
from rest_framework import serializers # type: ignore

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer