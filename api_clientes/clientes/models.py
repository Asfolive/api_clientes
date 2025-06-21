from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome