from rest_framework import serializers
from django.core.files import File
from account.models import User, UserProfile
from filed.models import Agent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'first_name', 'last_name', 'email', 'phone_num', 'is_organisor', 'is_agent', 'is_support']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['photo']

    def update(self, instance, validated_data):
        photo_file = self.context['request'].data.get('photo')
        if photo_file:
            instance.photo.save(photo_file.name, File(photo_file))

        return instance

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

