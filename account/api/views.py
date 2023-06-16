from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import UserSerializer, SignupSerializer, UserSerializer2
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.models import User, FailedLogin

# from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from rest_framework.parsers import MultiPartParser, FormParser

@receiver(user_logged_in)
def user_logged_recv(sender, request, user, **kwargs):
    FailedLogin.objects.filter(user=user).delete()

@receiver(user_login_failed)
def user_login_failed_recv(sender, credentials, request, **kwargs):
    # User = get_user_model()
    try:
        u = User.objects.get(username = credentials.get('username'))
        # there is a user with the given username
        FailedLogin.objects.create(user=u)
        if FailedLogin.objects.filter(user=u).count() >= 3:
            # three tries or more, disactivate the user
            u.is_active = False
            u.save()
    except User.DoesNotExist:
        # user not found, we can not do anything
        pass



class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # "token": Token.objects.get(user=user).key,
            "message": "account create successfully"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user= serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token":token.key,
            "user_id": user.pk,
            "is_organisor": user.is_organisor,
            "is_agent": user.is_agent,
            "is_support": user.is_support,
            "username": user.username,
            "email": user.email,
        })


class UserListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer2


class UserDetailEditView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer2
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        user = self.get_object()

        photo = request.FILES.get('photo')
        if photo:
            print("Found photo")


        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        profile_serializer = serializer.fields['profile']
        profile_instance = serializer.instance.profile if hasattr(serializer.instance, 'profile') else None
        profile_data = self.request.data.get('profile')

        if profile_data and profile_instance:
            profile_serializer = profile_serializer(profile_instance, data=profile_data, partial=True)
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()
        elif profile_data and not profile_instance:
            profile_serializer = profile_serializer(data=profile_data)
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save(user=serializer.instance)

        serializer.save()