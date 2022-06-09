from rest_framework import serializers
from kelimeler.models import Kelime


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kelime
        fields = '__all__'
