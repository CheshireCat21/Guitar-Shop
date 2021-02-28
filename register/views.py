from django.shortcuts import render
from .forms import UserForm


def register(request):
    error = ''
    if request.method == "POST":
        if len(request.POST['password']) >= 8:
            if request.POST['password'] == request.POST['repeat_password']:
                form = UserForm(request.POST)
                form.save()
        else:
            error = "Wrong form!"

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'register/main_page.html', data)