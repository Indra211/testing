from .models import Details,Slots
from .serializers import DetailsSerializer,SlotSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class DetialsList(APIView):
    def get(self, request, format=None):
        snippets = Details.objects.all()
        serializer = DetailsSerializer(snippets, many=True)
        return Response({'data': serializer.data})

    def post(self, request, format=None):
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_slots(request):
        slots = Slots.objects.all()
        serializer = SlotSerializer(slots, many=True)

        return Response({'message':"Succes","data":serializer.data})
