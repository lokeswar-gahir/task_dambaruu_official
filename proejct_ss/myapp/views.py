from django.utils import timezone
from typing import Any
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from authentication.forms import *
from .models import VideoModel
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.

def admin_and_super_admin_only(func):
    def inner(request):
        if request.user.type=='ADMIN' or request.user.type=='SUPER_ADMIN':
            return func(request)
        else:
            return HttpResponse(f'<h2><pre>Access Denied for non-ADMIN and non-SUPER_ADMIN !!!</pre></h2><p>URL: <b>{request.path}</b></p><p>Username: <b>{request.user.username}</b></p><p>User Type: <b>{request.user.type}</b></p>Goto <a href="/myapp/dashboard">Home page</a>')
    return inner

def super_admin_only(func):
    def inner(request):
        if request.user.type=='SUPER_ADMIN':
            return func(request)
        else:
            return HttpResponse(f'<h2><pre>Access Denied for non-SUPER_ADMIN !!!</pre></h2><p>URL: <b>{request.path}</b></p><p>Username: <b>{request.user.username}</b></p><p>User Type: <b>{request.user.type}</b></p>Goto <a href="/myapp/dashboard">Home page</a>')
    return inner

def admin_and_super_admin_only_for_method(func):
    def inner(self, request):
        if request.user.type=='ADMIN' or request.user.type=='SUPER_ADMIN':
            return func(self, request)
        else:
            return HttpResponse(f'<h2><pre>Access Denied for non-ADMIN and non-SUPER_ADMIN !!!</pre></h2><p>URL: <b>{request.path}</b></p><p>Username: <b>{request.user.username}</b></p><p>User Type: <b>{request.user.type}</b></p>Goto <a href="/myapp/dashboard">Home page</a>')
    return inner

def super_admin_only_for_method(func):
    def inner(self, request):
        if request.user.type=='SUPER_ADMIN':
            return func(self, request)
        else:
            return HttpResponse(f'<h2><pre>Access Denied for non-SUPER_ADMIN !!!</pre></h2><p>URL: <b>{request.path}</b></p><p>Username: <b>{request.user.username}</b></p><p>User Type: <b>{request.user.type}</b></p>Goto <a href="/myapp/dashboard">Home page</a>')
    return inner




@login_required(login_url='/auth/login/')
def dashboard(request):
    videos = VideoModel.objects.all()
    return render(request, 'dashboard.html', {'videos': videos})




@login_required(login_url='/auth/login/')
@admin_and_super_admin_only
def user_ops_view(request):
    default_users = User.default_user.all()
    return render(request, 'user_ops.html', {'default_users': default_users})

@login_required(login_url='/auth/login/')
@admin_and_super_admin_only
def admin_ops_view(request):
    admins = User.admin.all()
    return render(request, 'admin_ops.html', {'admins': admins})

@login_required(login_url='/auth/login/')
@super_admin_only
def super_admin_ops_view(request):
    super_admins = User.super_admin.all()
    return render(request, 'super_admin_ops.html', {'super_admins': super_admins})




class Create_user_view(View):
    @admin_and_super_admin_only_for_method
    def get(self, request):
            form = DefaultUserRegisterForm()
            return render(request, 'create_user.html', {'form': form})

    @admin_and_super_admin_only_for_method
    def post(self, request):
        form = DefaultUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f'New User created successfully (\'{form.instance.username}\')')
            return redirect('/myapp/users/')
        
        return render(request, 'create_user.html', {'form': form})
        
class Create_admin_view(View):
    @super_admin_only_for_method
    def get(self, request):
        form = AdminRegisterForm()
        return render(request, 'create_admin.html', {'form': form})
      
    @super_admin_only_for_method
    def post(self, request):
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f'New Admin created successfully (\'{form.instance.username}\')')
            return redirect('admins')
        else:
            return render(request, 'create_admin.html', {'form': form})
            
class Create_super_admin_view(View):
    @super_admin_only_for_method
    def get(self, request):
        form = SuperAdminRegistrationForm()
        return render(request, 'create_super_admin.html', {'form': form})
            
    @super_admin_only_for_method
    def post(self, request):
        form = SuperAdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f'New Super Admin created successfully (\'{form.instance.username}\')')
            return redirect('super_admins')
        else:
            return render(request, 'create_super_admin.html', {'form': form})




@login_required(login_url='/auth/login/')
@admin_and_super_admin_only
def delete_user(request):
    if request.method=='POST':
        delete_user_id = request.POST.get('delete_id')
        found_user = User.default_user.filter(id=delete_user_id).first()
        found_user.delete()
        messages.info(request, f'User deleted (\'{found_user.username}\')')
        return redirect('/myapp/users/')
    else:
        return HttpResponse(f'<h2><pre>non-POST methods are not allowed !!!</pre></h2>Goto <a href="/myapp/dashboard">Home page</a>')

@login_required(login_url='/auth/login/')
@super_admin_only
def delete_admin(request):
    if request.method=='POST':
        delete_admin_id = request.POST.get('delete_id')
        found_admin = User.admin.filter(id=delete_admin_id).first()
        found_admin.delete()
        messages.info(request, f'Admin deleted (\'{found_admin.username}\')')
        return redirect('/myapp/admins/')
    else:
        return HttpResponse(f'<h2><pre>non-POST methods are not allowed !!!</pre></h2>Goto <a href="/myapp/dashboard">Home page</a>')

@login_required(login_url='/auth/login/')
@super_admin_only
def delete_super_admin(request):
    if request.method=='POST':
        delete_super_admin_id = request.POST.get('delete_id')
        found_super_admin = User.super_admin.filter(id=delete_super_admin_id).first()
        found_super_admin.delete()
        messages.info(request, f'Super admin deleted (\'{found_super_admin.username}\')')
        return redirect('/myapp/super-admins/')    
    else:
        return HttpResponse(f'<h2><pre>non-POST methods are not allowed !!!</pre></h2>Goto <a href="/myapp/dashboard">Home page</a>')




@login_required(login_url='/auth/login/')
@admin_and_super_admin_only
def update_user_view(request):
    update_user_id = request.POST.get('update_id')
    found_user = User.default_user.filter(id=update_user_id).first()
    form = DefaultUserUpdateForm(instance=found_user)
    return render(request, 'update_user.html', {'form': form})

@login_required(login_url='/auth/login/')
@super_admin_only
def update_admin_view(request):
    update_admin_id = request.POST.get('update_id')
    found_admin = User.admin.filter(id=update_admin_id).first()
    form = AdminUpdateForm(instance=found_admin)
    return render(request, 'update_admin.html', {'form':form})

@login_required(login_url='/auth/login/')
@super_admin_only
def update_super_admin_view(request):
    update_super_admin_id = request.POST.get('update_id')
    found_super_admin = User.super_admin.filter(id=update_super_admin_id).first()
    form = SuperAdminUpdateForm(instance=found_super_admin)
    return render(request, 'update_super_admin.html', {'form':form})

@login_required(login_url='/auth/login/')
@admin_and_super_admin_only
def update_video_view(request):
    update_video_id = request.POST.get('update_video_id')
    request.session['update_video_id'] = update_video_id
    video = VideoModel.objects.filter(id=update_video_id).first()
    form = UpdateVideoForm(instance=video)
    return render(request, 'update_video.html', {'form': form})




@login_required(login_url='/auth/login/')
@admin_and_super_admin_only
def update_user(request):
    username = request.POST.get('username')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')
    type=request.POST.get('type')
    updated = User.objects.filter(username=username).update(first_name = first_name, last_name = last_name, email = email, type=type)
    if updated:
        messages.info(request, f'User updated (\'{username}\')')
        return redirect('/myapp/users/')
    else:
        return HttpResponse('<h2><pre>Something went wrong !!!</pre></h2> Goto <a href="/myapp/dashboard">Home page</a>')

@login_required(login_url='/auth/login/')
@super_admin_only
def update_admin(request):
    username = request.POST.get('username')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')
    type=request.POST.get('type')
    updated = User.admin.filter(username=username).update(first_name=first_name, last_name=last_name, email=email, type=type)
    if updated:
        messages.info(request, f'Admin updated (\'{username}\')')
        return redirect('/myapp/admins/')
    else:
        return HttpResponse(f'<h2><pre>Something went wrong !!!</pre></h2> Goto <a href="/myapp/dashboard">Home page</a>')

@login_required(login_url='/auth/login/')
@super_admin_only
def update_super_admin(request):
    username = request.POST.get('username')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')
    type=request.POST.get('type')
    updated = User.super_admin.filter(username=username).update(first_name=first_name, last_name=last_name, email=email, type=type)
    if updated:
        messages.info(request, f'Super admin updated (\'{username}\')')
        return redirect('/myapp/super-admins/')
    else:
        return HttpResponse(f'<h2><pre>Something went wrong !!!</pre></h2> Goto <a href="/myapp/dashboard">Home page</a>')

@login_required(login_url='/auth/login/')
@admin_and_super_admin_only
def update_video(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if 'update_video_id' in request.session:
        video_id = request.session['update_video_id']
        updated = VideoModel.objects.filter(id=video_id).update(title=title, description=description, modified_at=timezone.now())
        if updated:
            messages.info(request, f'Video details updated (\'{title}\')')
            return redirect('video_manager')
    else:
        return HttpResponse(f'<h2><pre>Something went wrong !!!</pre></h2> Goto <a href="/myapp/dashboard">Home page</a>')




class Video_upload(View):
    @admin_and_super_admin_only_for_method
    def get(self, request):
        form = VideoUploaderForm()
        return render(request, 'video_uploader.html', {'form':form})
    
    @admin_and_super_admin_only_for_method
    def post(self, request):
        form = VideoUploaderForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.uploader = request.user
            new_video.save()
            messages.info(request, f'New video uploaded (\'{new_video.title}\').')
            return redirect('video_manager')
        else:
            return render(request, 'video_uploader.html', {'form':form})




@login_required(login_url='/auth/login')
@admin_and_super_admin_only
def video_manager_view(request):
    videos = VideoModel.objects.all()
    return render(request, 'video_manager.html', {'videos': videos})

def delete_video(request):
    video_id = request.POST.get('delete_video_id')
    video = VideoModel.objects.get(id = video_id)
    fs = FileSystemStorage()
    fs.delete(str(video.content))
    video.delete()
    messages.info(request, f'Video deleted (\'{video.title}\')')
    return redirect('video_manager')
