from django.http import HttpResponse
from django.views import generic, View


class PostViewExercise(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Olá, seja bem vindo!')