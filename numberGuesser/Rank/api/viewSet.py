from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from ..models import Rank
from .serializer import RankSerializer


class RankViewSet(ModelViewSet):

    serializer_class = RankSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name',)
    ordering_fields = ('time',)

    def get_queryset(self):
        queryset = Rank.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            return queryset.filter(name=name)

    def list(self, request, *args, **kwargs):
        return super(RankViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(RankViewSet, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(RankViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(RankViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(RankViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(RankViewSet, self).destroy(request, *args, **kwargs)
