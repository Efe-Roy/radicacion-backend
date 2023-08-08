from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import UserSerializer, SignupSerializer, UserSerializer2, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.models import User, FailedLogin

# from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
import os
from django.core.mail import send_mail
from django.conf import settings



class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']

# @receiver(user_logged_in)
# def user_logged_recv(sender, request, user, **kwargs):
#     FailedLogin.objects.filter(user=user).delete()

# @receiver(user_login_failed)
# def user_login_failed_recv(sender, credentials, request, **kwargs):
#     # User = get_user_model()
#     try:
#         u = User.objects.get(username = credentials.get('username'))
#         # there is a user with the given username
#         FailedLogin.objects.create(user=u)
#         if FailedLogin.objects.filter(user=u).count() >= 3:
#             # three tries or more, disactivate the user
#             u.is_active = False
#             u.save()
#     except User.DoesNotExist:
#         # user not found, we can not do anything
#         pass



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


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        # serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            # current_site = get_current_site(
            #     request=request).domain
            # relativeLink = reverse(
            #     'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            # redirect_url = request.data.get('redirect_url', '')
            # absurl = 'http://'+current_site + relativeLink
            absurl2 = 'https://licenciasurbanisticas.com/reset-password/'+ uidb64 + '/' + token
            # email_body = 'Hello, \n Use link below to reset your password  \n' + \
            #     absurl+"?redirect_url="+redirect_url + "\n" + \
            #     absurl2
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl2
            # from_email= settings.EMAIL_HOST_USER
            data = {'email_body': email_body, 'to_email': user.email,
                    'from_email': settings.EMAIL_HOST_USER ,'email_subject': 'Reset your passsword'}
            send_mail(subject=data['email_subject'], message=data['email_body'], from_email=data['from_email'], recipient_list=[data['to_email']])
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'succes': True, 'Message': 'Credential Valid', 'uid64': uidb64, 'token': token}, status=status.HTTP_200_OK)
            
                # if len(redirect_url) > 3:
                #     return CustomRedirect(redirect_url+'?token_valid=False')
                # else:
                #     return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')

            # if redirect_url and len(redirect_url) > 3:
            #     return CustomRedirect(redirect_url+'?token_valid=True&message=Credentials Valid&uidb64='+uidb64+'&token='+token)
            # else:
            #     return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
            # try:
            #     if not PasswordResetTokenGenerator().check_token(user):
            #         return CustomRedirect(redirect_url+'?token_valid=False')
                    
            # except UnboundLocalError as e:
            #     return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)