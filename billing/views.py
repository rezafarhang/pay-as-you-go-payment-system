from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Sum, Count
from .models import Price, Cost
from .serializers import PriceSerializer, TotalCostSerializer
from .utils import calculate_request_cost, datetime_validation

class PriceView(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PorsServiceView(APIView):

    @calculate_request_cost(service_name='pors')
    def get(self, request):

        # DO Service-Related Operations

        return Response('Request is successfully received.', status=status.HTTP_201_CREATED) 


class LineServiceView(APIView):
    
    @calculate_request_cost(service_name='line')
    def get(self, request):

        # DO Service-Related Operations

        return Response('Request is successfully received.', status=status.HTTP_201_CREATED) 
    

class TotalCostReceiptView(RetrieveAPIView):
    
    def get(self, request):
        start_date_obj, end_date_obj = datetime_validation(request)

        instance = Cost.objects.filter(
            Q(created_at__gte=start_date_obj) and 
            Q(created_at__lt=end_date_obj) and
            Q(user=request.user.id)
        ).aggregate(total_request_cost=Sum('request_cost'), total_request_count=Count('request_cost'))


        serializer = TotalCostSerializer(instance)

        return Response(serializer.validated_data)
    

class TotalCostReceiptPerServiceView(RetrieveAPIView):
    
    def get(self, request, service_name):
        start_date_obj, end_date_obj = datetime_validation(request)

        instance = Cost.objects.filter(
                                    Q(created_at__gte=start_date_obj) & 
                                    Q(created_at__lt=end_date_obj) &
                                    Q(service_name=service_name)&
                                    Q(user=request.user.id)
                                ).aggregate(total_request_cost=Sum('request_cost'), total_request_count=Count('request_cost'))
        
        serializer = TotalCostSerializer(instance)

        return Response(serializer.validated_data)
        

