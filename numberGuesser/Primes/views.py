from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Prime import Prime


class PrimesView(APIView):

    def get(self, _):
        prime = Prime(8000)
        primes = prime.crivo()
        size = prime.get_size()

        return Response({
            "size": size,
            "primes": primes,
        })

    def post(self, request):
        filter_type = request.query_params.get('filter', None)
        primes = request.data.get('primes')
        num = request.data.get('num')

        if filter_type is None:
            return Response({"primes": primes})

        elif filter_type.lower() == 'sum':
            prime = Prime(0, primes)
            new_primes = prime.filter_type_sum(num)
            size = prime.get_size()

            return Response({
                "size": size,
                "primes": new_primes
            })
        elif filter_type.lower() == 'mod':
            prime = Prime(0, primes)
            new_primes = prime.filter_type_mod(7)
            size = prime.get_size()

            return Response({
                "size": size,
                "primes": new_primes
            })
        elif filter_type.lower() == 'multi':
            prime = Prime(0, primes)
            new_primes = prime.filter_type_multi(num)
            size = prime.get_size()

            return Response({
                "size": size,
                "primes": new_primes
            })
        else:
            return Response({
                'error': 'Please, type a valid kind of filter',
            }, status=status.HTTP_400_BAD_REQUEST)



