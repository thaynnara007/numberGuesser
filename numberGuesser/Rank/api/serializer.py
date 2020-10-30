from rest_framework.serializers import ModelSerializer
from ..models import Rank


class RankSerializer(ModelSerializer):
    class Meta:
        model = Rank
        fields = [
            'name',
            'attempts',
            'time',
            'number_guessed'
        ]
