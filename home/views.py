from django.shortcuts import render
from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def home(request):
    return Response({"message": "Hello this side vyoma"})