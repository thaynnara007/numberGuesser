from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.paginator import Paginator
from ..models import Rank
from .serializer import RankSerializer


class RankViewSet(ModelViewSet):

    serializer_class = RankSerializer

    def get_queryset(self):
        queryset = Rank.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            return queryset.filter(name=name)

    def list(self, request, *args, **kwargs):
        page_size = request.query_params.get('page_size', None)
        ranks = Rank.objects.all().order_by('time')

        if page_size is not None:
            paginator = Paginator(ranks, page_size)
            all_ranks = RankSerializer(paginator.get_page(1), many=True)

            return Response({"all_ranks": all_ranks.data})
        else:
            all_ranks = RankSerializer(ranks, many=True)

            return Response({"all_ranks": all_ranks.data})

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
