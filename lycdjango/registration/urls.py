from django.urls import path
from .views import SignUpView 
#, PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

from django.contrib.auth.views import (
    #SignUpView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView,
 )
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/', PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name='password-reset'),
    #path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/confirm/', PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name='password_reset_complete'),
]
