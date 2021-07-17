from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome