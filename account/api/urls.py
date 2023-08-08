from .views import SignupView
from django.urls import path, include
from .views import (
     CustomAuthToken, UserListView, UserDetail, UserDetailEditView,
     RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView
)

urlpatterns = [
    path('rest-auth/registration/', SignupView.as_view()),
    path('rest-auth/login/', CustomAuthToken.as_view(), name ='auth-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('userlist', UserListView.as_view()),
    path('user/detail/<pk>/', UserDetail.as_view()),

    path('user/edit/<pk>/', UserDetailEditView.as_view()),
 

    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]

