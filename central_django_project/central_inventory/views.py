from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Site
from .serializer import SiteSerializer, iapSerializer, switchSerializer, orderSerializer
from central_inventory.models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

# def index(request):
#     return HttpResponse("Here I am at views")

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def site_list(request):
class site_list(APIView):
    
    def get(self, request, format=None):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        sites = request.data
        serializer = SiteSerializer(data=sites)
        if serializer.is_valid():
            serializer.save()
            return Response('successfully addded')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        pk = request.query_params.get('site_id', None)
        if pk:
            site = Site.objects.get(pk=pk)
            serializer = SiteSerializer(instance=site, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response('Unsuccessful')
        else:
            return Response('pk not fetched')

    def delete(self, request, format=None):
        pk = request.query_params.get('site_id', None)
        site = Site.objects.get(pk=pk).delete()
        return Response('sites Deleted')

    