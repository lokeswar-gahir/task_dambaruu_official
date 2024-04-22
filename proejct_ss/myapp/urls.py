from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
     path('dashboard/', dashboard, name='dashboard'),


     path('users/', user_ops_view, name='users'),
     path('admins/', admin_ops_view, name='admins'),
     path('super-admins/', super_admin_ops_view, name='super_admins'),


     path('create-user/', login_required(Create_user_view.as_view(), login_url='/auth/login/'), name='create_user'),
     path('create-admin/', login_required(Create_admin_view.as_view(), login_url='/auth/login/'), name='create_admin'),
     path('create-super-admin/', login_required(Create_super_admin_view.as_view(), login_url='/auth/login/'), name='create_super_admin'),


     path('delete-user/', delete_user, name='delete_user'),
     path('delete-admin/', delete_admin, name='delete_admin'),
     path('delete-super-admin/', delete_super_admin, name='delete_super_admin'),
     
     
     path('update-user-form/', update_user_view, name='update_user_form'),
     path('update-admin-form/', update_admin_view, name='update_admin_form'),
     path('update-super-admin-form/', update_super_admin_view, name='update_super_admin_form'),
     path('update-video-form/', update_video_view, name='update_video_form'),


     path('update-user/', update_user, name='update_user'),
     path('update-admin/', update_admin, name='update_admin'),
     path('update-super-admin/', update_super_admin, name='update_super_admin'),
     path('update-video/', update_video, name='update_video'),


     path('video-upload/', login_required(Video_upload.as_view(), login_url='/auth/login/'), name='video_upload'),
     path('video-manager/', video_manager_view, name='video_manager'),
     path('delete-video/', delete_video, name='delete_video'),
]
