from rest_framework import serializers

from .models import Tanya


class TanyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanya
        fields = [
            'pertanyaan',
            'jawaban'
        ]