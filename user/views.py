from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CreateUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)

def logout_view(request):
    logout(request)
    return render(request, "user/logout.html")
