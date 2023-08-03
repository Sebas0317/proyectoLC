from django.urls import path
from .views import SignUpView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
#     path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('password_reset/', PasswordResetView.as_view(), name='password-reset'),
#     #path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
