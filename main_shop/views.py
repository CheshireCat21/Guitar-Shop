from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import GuitarExamples


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

    guitar = GuitarExamples.objects.all()

    guitar_ex = 'guitar model 1'


    data = {
        'form': form,
        'error': error,
        'guitar': guitar,
        'guitar_ex': guitar_ex
    }

    return render(request, 'main_shop/guitar_in_stock.html', data)



def GuitarEx(request):
    guitar = GuitarExamples.objects.all()
    return render(request, 'main_shop/show_guitar.html', {'guitar': guitar })