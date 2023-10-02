from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProdSerializer
from .models import Copies
from .serializers import CopySerializer
from .products import products


@api_view(['GET'])
def Routes(request):
    routes=[
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]
    return Response(routes,)

@api_view(['GET'])
def getPrds(request):
    products = Product.objects.all()
    serializer = ProdSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getPrd(request,product_id):

    product = Product.objects.get(_id=product_id)
    serializer = ProdSerializer(product,many = False)
    '''product = None
    for i in products:
        if i['_id'] == product_id:
            product = i
            break
        '''

    return Response(serializer.data)

@api_view(['GET'])
def getCps(request,product_id):

    #copies = Copies.objects.filter(_id = product_id)
    #copies = Copies.objects.all()
    #serializer = CopySerializer(copies,many = False)
    #return Response(serializer.data)
    copies = Copies.objects.filter(_id=product_id)
    serializer = CopySerializer(copies, many=True)
    return Response(serializer.data)