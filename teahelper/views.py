from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegistrationForm, UserLoginForm, RequestForm
from .models import Request
from django.contrib import messages  # Для отображения сообщений об ошибках или успешных действиях

# Create your views here.
def home(request):
    return render(request, 'teahelper/home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('create_request')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('create_request')
    else:
        form = UserRegistrationForm()
    return render(request, 'teahelper/register.html', {'form': form})

# Авторизация пользователя
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_panel')
                return redirect('home')
            else:
                messages.error(request, "Пользователя с таким логином или паролем не существует.")
    else:
        form = UserLoginForm()

    return render(request, 'teahelper/login.html', {'form': form})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user
            request_obj.save()
            messages.success(request, "Заказ успешно создан")
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'teahelper/create_request.html', {'form': form})

@login_required
def request_list(request):
    requests = Request.objects.filter(user=request.user)
    return render(request, 'teahelper/request_list.html', {'requests': requests})

def logout_view(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы.")
    return redirect('home')

@user_passes_test(lambda u: u.is_superuser)
def admin_panel(request):
    requests = Request.objects.all()
    return render(request, 'teahelper/admin_panel.html', {'requests': requests})

@user_passes_test(lambda u: u.is_superuser)
def update_request_status(request, request_id):
    if request.method == 'POST':
        request_obj = get_object_or_404(Request, id=request_id)
        request_obj.save()
        messages.success(request, "Статус чая успешно обновлен.")
    return redirect('admin_panel')

@user_passes_test(lambda u: u.is_superuser)
def delete_request(request, request_id):
    if request.method == 'POST':
        request_obj = get_object_or_404(Request, id=request_id)
        request_obj.delete()
        messages.success(request, "Чай успешно удален.")
    return redirect('admin_panel')