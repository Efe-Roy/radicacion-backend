from rest_framework import serializers
from django.core.files import File
from account.models import User, UserProfile
from filed.models import Agent

from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'first_name', 'last_name', 'email', 
                'phone_num', 'is_organisor', 'is_agent', 'is_support',
                'is_active'
                ]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['photo']

    def update(self, instance, validated_data):
        photo_file = self.context['request'].data.get('photo')
        if photo_file:
            instance.photo.save(photo_file.name, File(photo_file))

        return instance

class ListUserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('id', 'user')

    def get_user(self, obj):
        return UserSerializer(obj.user).data
    
class UserSerializer2(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_num', 'profile']

        def update(self, instance, validated_data):
            profile_data = validated_data.pop('profile', {})
            profile_serializer = self.fields['profile']
            profile = instance.profile

            for attr, value in profile_data.items():
                setattr(profile, attr, value)

            profile.save()

            return super().update(instance, validated_data)

        
class SignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_organisor= True
        user.is_agent= False
        user.is_support= False
        user.save()
        UserProfile.objects.create(user=user)
        # if user.is_organisor == True:
        # if user.is_support == True:
        #     UserProfile.objects.create(user=user)
        # if user.is_agent == True:
        #     Agent.objects.create(user=user)
        return user



class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)