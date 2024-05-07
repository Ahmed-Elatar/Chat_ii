from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import *
from .models import *
from .serializers import *
# Create your views here.







def index(request):
    return HttpResponse("HOME................")