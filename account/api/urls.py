from django.urls import path, include
from .views import (
     CustomAuthToken, SignupView, CheckAuthenticatedView,LogoutView, DeleteAccountView, 
     UserListView, UserDetail, UserDetailEditView, ChangePasswordView,
     RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView, UserProfileListView
)

urlpatterns = [
    path('authenticated', CheckAuthenticatedView.as_view()),
    path('register/', SignupView.as_view()),
    path('login/', CustomAuthToken.as_view(), name ='auth-token'),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),

#     path('rest-auth/', include('rest_auth.urls')),
    path('userlist/', UserListView.as_view()),
    path('userprofilelist', UserProfileListView.as_view()),
    path('user/detail/<pk>/', UserDetail.as_view()),

    path('user/edit/<pk>/', UserDetailEditView.as_view()),
 

    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]

