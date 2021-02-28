from django.core.serializers import serialize
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm
from .models import GuitarExamples


# ну і оцю вьюху нада розділить
@csrf_exempt
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

    guitars = GuitarExamples.objects.all()

    guitar_ex = 'guitar model 1'


    data = {
        'form': form,
        'error': error,
        'guitar': guitars,
        # оця штука вертає тобі жсон, тоїсть дікт, який нормально обрабатує жс
        # вобщє желатєльно зробить отдєльну вьюху, яка буде вертать тобі картінку
        'guitars_json': serialize('json', guitars),
        'guitar_ex': guitar_ex
    }

    return render(request, 'main_shop/guitar_in_stock.html', data)


@csrf_exempt
def GuitarEx(request):
    guitar = GuitarExamples.objects.all()
    return render(request, 'main_shop/show_guitar.html', {'guitar': guitar })
# отут нада отрєфакторить назви і всякі отступи, пробєли і т.п.
# прочитай pep8