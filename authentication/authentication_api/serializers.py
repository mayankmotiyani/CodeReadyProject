
import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.validators import UniqueValidator
from authentication.models import Profile


reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
passObj = re.compile(reg)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)
        try:
            user_instance = User.objects.get(email__iexact=email)
        except Exception as exception:
            data = dict()
            data['status'] = status.HTTP_401_UNAUTHORIZED
            data['response'] = "User is not exists.Please Register first!"
            return data
        user = authenticate(username=user_instance.username, password=password)
        if user is not None:
            refresh = self.get_token(user)
            data = dict()
            data['status'] = status.HTTP_200_OK
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            data['username'] = user_instance.username
            return data
        elif user is None:
            data = dict()
            data['status'] = status.HTTP_401_UNAUTHORIZED
            data['response'] = "Incorrect Password!"
            return data
            
            
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username','first_name','last_name','password','email')

    def validate(self, attrs):
        pass_regex1 = re.search(passObj, attrs['password'])
        if not pass_regex1:
            raise serializers.ValidationError({"password": "Invalid Password!"})
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(
            user = user,
        )
        profile.save()
        print(type(user))
        print(user)
        return user