from django.db import models

# Create your models here.

class Tarefa(models.Model):
    PRIODADE_CHOICES = [
        ("A", "Alta"),
        ("B", "Baixa"),
        ("N", "Normal")
    ]
    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIODADE_CHOICES, null=False, blank=False)