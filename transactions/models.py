from django.db import models


class Transaction(models.Model):
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono = models.CharField(max_length=14)
    nomedaloja = models.CharField(max_length=18)
