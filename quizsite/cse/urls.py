from django.contrib import admin
from django.urls import path
from .import views
from account import views as v
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'cse'
admin.site.name = "MCQhero"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', v.signup, name='signup'),
    path('signin/', v.signin, name='signin'),
    path('signout/', v.signout, name='signout'),
    path('profile/', v.profileview, name='profileview'),
    path('editprofile/', v.editprofile, name='editprofile'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('cse:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('cse:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('activate/<uidb64>/<token>', v.activate, name='activate'),

]
