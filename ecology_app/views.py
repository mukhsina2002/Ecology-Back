import requests
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from telegram.constants import ParseMode

from config import settings
from .models import Animal, Plant, NaturalResources, Utilize
from .serializer import AnimalListSerializer, AnimalSerializer, PlantListSerializer, PlantSerializer, NaturalSerializer, \
    UtilizeListSerializer, UtilizeSerializer, AnimalListSerializerRu, AnimalSerializerRu, PlantListSerializerRu, \
    PlantSerializerRu, NaturalSerializerRu


class AnimalListView(APIView):
    @staticmethod
    def get(request):
        lang = request.query_params.get('lang')

        if lang == 'en':
            animals = Animal.objects.all()
            serializer = AnimalListSerializer(animals, many=True)
            return Response(serializer.data)
        else:
            animals = Animal.objects.all()
            serializer = AnimalListSerializerRu(animals, many=True)
            return Response(serializer.data)


class AnimalDetailView(APIView):
    @staticmethod
    def get(request, pk):
        lang = request.query_params.get('lang')

        try:
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response({"message": "Animal not found"}, status=status.HTTP_404_NOT_FOUND)

        if lang == 'en':
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        else:
            serializer = AnimalSerializerRu(animal)
            return Response(serializer.data)


class PlantListView(APIView):
    @staticmethod
    def get(request):
        lang = request.query_params.get('lang')
        plants = Plant.objects.all()

        if lang == 'en':
            serializer = PlantListSerializer(plants, many=True)
            return Response(serializer.data)
        else:
            serializer = PlantListSerializerRu(plants, many=True)
            return Response(serializer.data)


class PlantDetailView(APIView):
    @staticmethod
    def get(request, pk):
        lang = request.query_params.get('lang')

        try:
            plant = Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            return Response({"message": "Plant not found"}, status=status.HTTP_404_NOT_FOUND)

        if lang == 'en':
            serializer = PlantSerializer(plant)
            return Response(serializer.data)
        else:
            serializer = PlantSerializerRu(plant)
            return Response(serializer.data)


class NatureListView(APIView):
    @staticmethod
    def get(request):
        lang = request.query_params.get('lang')
        product = NaturalResources.objects.all()

        if lang == 'en':
            serializer = NaturalSerializer(product, many=True)
            return Response(serializer.data)
        else:
            serializer = NaturalSerializerRu(product, many=True)
            return Response(serializer.data)


class UtilizeListView(APIView):
    @staticmethod
    def get(request):
        utilize = Utilize.objects.all()
        serializer = UtilizeListSerializer(utilize, many=True)
        return Response(serializer.data)


class UtilizeDetailView(APIView):
    @staticmethod
    def get(request, pk):
        try:
            utilize = Utilize.objects.get(pk=pk)
        except Utilize.DoesNotExist:
            return Response({"message": "Utilize not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UtilizeSerializer(utilize)
        return Response(serializer.data)


class UtilizeViewByType(generics.ListAPIView):
    serializer_class = UtilizeListSerializer

    def get_queryset(self):
        type = self.request.query_params.get('type')
        if type:
            return Utilize.objects.filter(type=type)
