from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile, Contact
from .forms import ProfileEditForm
from django.contrib import messages
from django.views import generic
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# from common.decorators import ajax_required


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})
    
def home(request):
    context = {
        'login_form': AuthenticationForm(),
        'register_form': UserCreationForm(),
    }
    return render(request, 'registration/home.html',context)



def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            # ^creates an empty profile
            return render(request, 'registration/register_done.html',{'new_user':new_user})
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/register.html',{'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,'Error updating your profile')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'profile_form':profile_form})

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html',{'section':'people','users':users})

@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people',
                                                        'user': user})
# @ajax_required
# @require_POST
# @login_required
# def user_follow(request):
#     user_id = request.POST.get('id')
#     action = request.POST.get('action')
#     if user_id and action:
#         try:
#             user = User.objects.get(id=user_id)
#             if action == 'follow':
#                 Contact.objects.get_or_create(user_from=request.user, user_to=user)
#             else:
#                 Contact.objects.filter(user_from=request.user, user_to=user).delete()
#             return JsonResponse({'status':'ok'})
#         except User.DoesNotExist:
#             return JsonResponse({'status':'ko'})
#     return JsonResponse({'status':'ko'})
