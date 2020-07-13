from django.shortcuts import render
from .forms import TarefaForms

# Create your views here.

def listar_tarefas(request):
    nome_tarefa = 'Minha segunda condição em python'
    return render(request, 'tarefas/listar_tarefas.html', {'nome_tarefa': nome_tarefa})

def cadastrar_tarefa(request):
    form_tarefa = TarefaForms()
    return render(request, 'tarefas/form_tarefas.html')