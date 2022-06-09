from itsdangerous import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from kelimeler.models import Kelime
from .serializers import ItemSerializers


@api_view(['GET'])
def getData(request):
    # kisi = {'name': 'ali', 'age': 37}
    # return Response(kisi)
    items = Kelime.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
