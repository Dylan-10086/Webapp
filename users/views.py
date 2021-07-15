from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    """注册新用户"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)  # 用于用户正确填写表单后自动登录
            return redirect('learn_log:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
