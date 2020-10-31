from rest_framework.views import APIView
from rest_framework.response import Response
from .Prime import Prime


class PrimesView(APIView):

    def get(self, _):
        primes = Prime(8000).crivo()
        return Response({"primes": primes})

    def post(self, request):
        filter_type = request.query_params.get('filter', None)
        primes = request.data.get('primes')
        num = request.data.get('num')

        if filter_type is None:
            return Response({"primes": primes})

        elif filter_type.lower() == 'sum':
            new_primes = Prime(0, primes).filter_type_sum(num)

            return Response({"primes": new_primes})
        elif filter_type.lower() == 'mod':
            new_primes = Prime(0, primes).filter_type_mod(7)

            return Response({"primes": new_primes})
        elif filter_type.lower() == 'multi':
            new_primes = Prime(0, primes).filter_type_multi(num)

            return Response({"primes": new_primes})



