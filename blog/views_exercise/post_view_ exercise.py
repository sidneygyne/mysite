from django.http import HttpResponse
from django.views import generic

class PostViewExercice(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Olá, seja bem vindo!')