from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Skills


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):

    users = UserProfileSerializer(many=True)

    def create(self, validated_data):
        s=Skills(title = validated_data['title'])
        s.save()
        if validated_data['users'] is not None:
            for each in validated_data['users']:
                s.users.add(each)
        return s

    class Meta:
        model = Skills
        fields = ('title', 'users')


class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')