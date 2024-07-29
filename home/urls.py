from django.contrib import admin
from django.urls import path,include, re_path
from django.contrib.auth import views as auth_views
from home import views


urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("admin_login", views.admin_login, name='admin_login'),
    path("blog", views.blog, name='blog'),
    path("change_password", views.change_password, name='change_password'),
    path("contact", views.contact, name='contact'),
    path("forget_password", views.forget_password, name='forget_password'),
    path("gallery", views.gallery, name='gallery'),
    path("home", views.home, name='home'),
    path("login/", views.login_view, name='login'),
    path("main_register", views.main_register, name='main_register'),
    # path("register", views.register, name='register'),
    path("reset_password", views.reset_password, name='reset_password'),
    path("team", views.team, name='team'),
    path("volunteer", views.volunteer, name='volunteer'),
    path("profile", views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    
    path("password_reset_confirm", views.password_reset_confirm, name='password_reset_confirm'),
    path("password_reset_complete", views.password_reset_complete, name='password_reset_complete'),
    path("password_reset_done", views.password_reset_done, name='password_reset_done'),
    path("password_reset", views.password_reset, name='password_reset'),
    path("register_1", views.register_1, name='register_1'),
    
    path('home/', include('django.contrib.auth.urls')),
    # path('enroll/<int:event_id>/', views.enroll, name='enroll'),
    # re_path(r'^enroll/(?P<event_id>[0-9])', views.enroll, name='enroll'),
    
    path('enroll/<int:e_id>/', views.enroll, name='enroll'),
    path('logout/', views.logout_view, name='logout'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('attendance/<int:e_id>/', views.attendance, name='attendance'),
    
    path("send_email",views.send_email, name='send_email'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('save_profile_changes', views.save_profile_changes, name='save_profile_changes'),
    
    
]