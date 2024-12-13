from rest_framework import serializers
# from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from .models import User


# User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'center_name',
                  'city',
                  'username',
                  'email',
                  'password',
                  ]
        extra_kwargs = {"password":
                            {"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        center_name = validated_data['center_name']
        city = validated_data['city']
        user_obj = User(username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        center_name=center_name,
                        city=city)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}}

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login")
        user = User.objects.filter(
            Q(email=email) | Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True)
        print(user)
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Incorrect credentials please try again in email")
        if user_obj:
            print(password)
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again in password")

        data["token"] = "token"
        return data
