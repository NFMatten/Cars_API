from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car


@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serialzer = CarSerializer(cars, many=True)
        return Response(serialzer.data)

    elif request.method == 'POST':
        serialzer = CarSerializer(data=request.data)
        if serialzer.is_valid() == True:
            serialzer.save()
            return Response(serialzer.data, status=201)
        else:
            return Response(serialzer.errors, status=400)