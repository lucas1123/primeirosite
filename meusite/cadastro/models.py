from django.db import models
from django.utils import timezone

class Veiculo(models.Model):
    descricao = models.CharField(max_length=50)
    chassi = models.DecimalField(max_digits=20, decimal_places=2)
    cor = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    motor = models.CharField(max_length=50)
    potência = models.CharField(max_length=50)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class Marca(models.Model):
    nomeMarca = models.CharField(max_length=25)

    def __str__(self):
        return self.nomeMarca


