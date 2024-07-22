import logger
from django.http import JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import OfficialSerializer
# Create your views here.


def home(request):
    return HttpResponse("Welcome!!, World.")


@api_view(['GET'])  #display all data
def official_name(request):
    print("Incoming Request")
    official_data = OfficialName.objects.order_by('-added_at')
    serialized_data = OfficialSerializer(official_data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['GET']) #specific data
def specific_data(request, id):
    try:
        individual_data = get_object_or_404(OfficialName, pk=id)
        serializer = OfficialSerializer(individual_data, partial=True)
        result = serializer.data
        return Response(result, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error':f'Data with ID: {id} not found..'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST']) #add data
def add_official(request):
        if request.method == 'POST':
            try:
                serialized_data = OfficialSerializer(data=request.data)
                if serialized_data.is_valid():
                    serialized_data.save()
                    return Response(serialized_data.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error':'Interval server Error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE']) #delete specific data
def remove_official(request, id):
    official_data = get_object_or_404(OfficialName, pk=id)    
    official_data.delete()
    return Response("Deleted..", status=status.HTTP_200_OK)


@api_view(['PATCH']) #update specific data
def update_official(request, id):
    official_data = get_object_or_404(OfficialName, pk=id)
    serialized_data = OfficialSerializer(official_data, data=request.data, partial=True)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
