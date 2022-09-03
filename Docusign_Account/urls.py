from django.urls import path
from .views import dashboard, login_user, register_user, log_out, change_password, change_password_done
from django.contrib.auth import views as auth_view

urlpatterns = [
    # login user urls
    path('login/', login_user, name="login"),
    path('logout/', log_out, name="logout"),
    path('register/', register_user, name="register"),
    # path('rules/', terms_of_service, name="rules"),
    path('dashboard/', dashboard, name="dashboard"),
    # .............................................
    # Note that we could just write    path('l', include(django.contrib.auth.urls)), instead of below urls
    # just we need to make directory called, registration and  our templates to it.Additionally, If we do it
    # we don't need to add template name in below code.Just we need to consider the name of our templates which are true
    # in this case.
    # ..............................................
    # change password urls
    path('password_change/', change_password, name='change_password'),
    path('password_change/done', change_password_done, name='change_password'),
    # reset password urls
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='accounts/password_reset_form.html')
         , name='password_reset'),

    path('password_reset/done', auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done'
                                                                                      '.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='accounts'
                                                                                             '/password_reset_confirm'
                                                                                             '.html'),
         name='password_reset_confirm'),
    path('reset/done',
         auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

]
