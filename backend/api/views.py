from rest_framework import generics
from .models import Vnet
from .serializers import VnetSerializer

class VnetCreateView(generics.CreateAPIView):
    queryset = Vnet.objects.all()
    serializer_class = VnetSerializer