from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
# Create your views here.

"""
Class based views, Basic CRUD operations
"""

class StudentApi(APIView):
    def get(self, request, pk=None,  format=None):
        id = pk
        if id is not None:
            specific_student = get_object_or_404(Student, pk=id)
            serialized_data = StudentSerializer(specific_student, partial=True)
            result = serialized_data.data
            return Response(result, status=status.HTTP_200_OK)
        else:
            all_student = Student.objects.all().order_by('-created_at')
            serializer = StudentSerializer(all_student, many=True)
            final_data = serializer.data
            return Response(final_data, status=status.HTTP_200_OK)
        
    
    def post(self, request, format=None):
        serialized = StudentSerializer(data=request.data)
        if request.method == 'POST':
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
            

    def delete(self, request, pk=None, format=None):
        try:            
            student_data = get_object_or_404(Student, id=pk)
            student_data.delete()
            return Response({'message':f'Student with ID:{pk} deleted.'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
    

    def patch(self, request, pk=None, format=None):
        try:
            std_data = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(std_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)