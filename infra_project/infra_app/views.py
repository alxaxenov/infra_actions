from django.http import HttpResponse


def index(request):
    return HttpResponse('Ты победитель!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
