from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import serializers, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import  APIView
from rest_framework.response import Response

from .models import *

# Create your views here.

class ClientPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'pageSize'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
"""
class ClientListView(generic.ListView):
    model = Client
    def get_context_data(self, **kwargs):
            context = super(ClientListView, self).get_context_data(**kwargs)
            return context
"""

class ClientListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "mainApp/client_list.html")


class ClientJsonView(generics.ListAPIView):

    print('Reaching inside clientJson view')
    serializer_class = ClientSerializer
    pagination_class = ClientPageNumberPagination

    print('after serializer class initialization')
    def get_queryset(self, *args, **kwargs):
        clients = Client.objects.all()

        print('inside get query set clients are:' , clients)

        direction = ''
        field     = ''

        try:
            direction = self.request.GET['sort[0][dir]']
            field     =  self.request.GET['sort[0][field]']

        except:
            pass

        if direction == 'asc':
            clients = clients.order_by(field)
        elif  direction == 'desc':
            clients = clients.order_by('-'+ field)

        return clients


