from rest_framework import serializers
from .models import *


class TalhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talhao
        fields = ["id", "descricao", "fazenda", "hectares", "cultura", "disponivel"]

        # descricao
        # fazenda
        # hectares
        # cultura
        # disponivel
