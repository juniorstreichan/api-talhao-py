from django.db import models

# Create your models here.
CULTURAS_DISPONIVEIS = (
    ("SOJA", "Produção de soja"),
    ("ALGODAO", "Produção de algodão"),
    ("MILHO", "Produção de milho")
)


class Talhao(models.Model):
    descricao = models.CharField(max_length=30, null=False)
    fazenda = models.CharField(null=False, max_length=30)
    hectares = models.FloatField(null=False)
    cultura = models.CharField(choices=CULTURAS_DISPONIVEIS, null=False, max_length=50)
    disponivel = models.BooleanField(null=False, default=1)

    def __str__(self):
        return "{} / {}".format(self.descricao,self.cultura)
