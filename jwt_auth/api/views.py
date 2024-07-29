from django.shortcuts import render, get_list_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Homeview(APIView):
    def get(self, request):
        return Response({'message:':'Hi, Welcome to Jwt Auth...'})
    