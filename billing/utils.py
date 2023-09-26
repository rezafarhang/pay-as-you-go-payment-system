from .models import Cost, Price
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework import status





def calculate_request_cost(service_name):
    def decorator(function):
        def wrapper(*args, **kwargs):

            request = args[1]
            service_price = Price.objects.order_by('-created_at').filter(service_name=service_name).first().unit_price

            Cost.objects.create(
                request_cost=service_price,
                service_name=service_name,
                user=request.user
            )

            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator


def datetime_validation(request):
    start_date, end_date = request.GET.get('start_date', None), request.GET.get('end_date', None)  
    start_date_obj, end_date_obj = datetime.strptime(start_date, '%Y-%m-%d'), datetime.strptime(end_date, '%Y-%m-%d')

    if type(start_date_obj) is not datetime and type(end_date_obj) is not datetime:
        return Response('input date is not valid', status=status.HTTP_400_BAD_REQUEST)
    
    end_date_obj += timedelta(days=1)

    return start_date_obj, end_date_obj