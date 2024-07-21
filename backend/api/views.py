from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import OfficialSerializer
# Create your views here.


def home(request):
    return HttpResponse("Hello, World.")


@api_view(['GET'])
def official_name(request):
    official_data = OfficialName.objects.order_by('-added_at')
    serialized_data = OfficialSerializer(official_data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_official(request):
    
    if request.method == 'POST':
        serialized_data = OfficialSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_official(request, id):
    official_data = get_object_or_404(OfficialName, pk=id)    
    official_data.delete()
    return Response("Deleted..", status=status.HTTP_200_OK)