from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import UserSerializer, SignupSerializer, UserSerializer2, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer, ListUserProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.models import User, UserProfile

from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.views import APIView
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })

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

        if not user.is_active:
            return Response({'message': 'Account is not active.'}, status=status.HTTP_401_UNAUTHORIZED)

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

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            # auth.logout(request)
            request.auth.delete()
            return Response({ 'success': 'Loggout Out' })
        except:
            return Response({ 'error': 'Something went wrong when logging out' })
        
class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            User.objects.filter(id=user.id).delete()

            return Response({ 'success': 'User deleted successfully' })
        except:
            return Response({ 'error': 'Something went wrong when trying to delete user' })
        
class ActivateDeactivateUser(APIView):
    permission_classes = [IsAuthenticated]

    def get_user(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def post(self, request, *args, **kwargs):
        id = request.data.get('id')
        action = request.data.get('action')  # 'activate' or 'deactivate'

        user = self.get_user(id)

        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if action == 'activate':
            user.is_active = True
        elif action == 'deactivate':
            user.is_active = False
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

        user.save()

        return Response({'message': f'User {user.username} successfully {action}d'}, status=status.HTTP_200_OK)
    

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'PageSize'

class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = User.objects.all().order_by('-date_joined')

        # Filter based on request parameters
        is_agent = self.request.query_params.get('is_agent', None)
        if is_agent is not None:
            queryset = queryset.filter(agent__isnull=not bool(is_agent))

        return queryset

class UserProfileListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)
    serializer_class = ListUserProfileSerializer
    queryset = UserProfile.objects.all()

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer2

class UserDetailEditView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer2
    queryset = User.objects.all()
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


class ChangePasswordView(APIView):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        # current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        # Check if the current password is correct
        # if not user.check_password(current_password):
        #     return Response({'error': 'Current password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password and save the user
        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password successfully changed.'}, status=status.HTTP_200_OK)
    
class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
           
            absurl2 = 'https://licenciasurbanisticas.com/reset-password/'+ uidb64 + '/' + token
            
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

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'succes': True, 'Message': 'Credential Valid', 'uid64': uidb64, 'token': token}, status=status.HTTP_200_OK)
            

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
      

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)