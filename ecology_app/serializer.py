from rest_framework import serializers
from .models import Animal, NaturalResources, Plant, Utilize


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'description', 'type', 'image', 'background_image', 'link']


class AnimalSerializerRu(serializers.ModelSerializer):
    name = serializers.CharField(source='name_ru')
    description = serializers.CharField(source='description_ru')
    type = serializers.CharField(source='type_ru')

    class Meta:
        model = Animal
        fields = ['id', 'name', 'description', 'type', 'image', 'background_image', 'link']


class AnimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'image']


class AnimalListSerializerRu(serializers.ModelSerializer):
    name = serializers.CharField(source='name_ru')

    class Meta:
        model = Animal
        fields = ['id', 'name', 'image']


class NaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalResources
        fields = ['id', 'title', 'about', 'pdf_file']


class NaturalSerializerRu(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ru')
    about = serializers.CharField(source='about_ru')

    class Meta:
        model = NaturalResources
        fields = ['id', 'title', 'about', 'pdf_file']


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'title', 'description', 'type', 'image', 'background_image', 'link', 'youtube_url']


class PlantSerializerRu(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ru')
    description = serializers.CharField(source='description_ru')
    type = serializers.CharField(source='type_ru')

    class Meta:
        model = Plant
        fields = ['id', 'title', 'description', 'type', 'image', 'background_image', 'link', 'youtube_url']


class PlantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'title', 'image']


class PlantListSerializerRu(serializers.ModelSerializer):
    title = serializers.CharField(source='title_ru')

    class Meta:
        model = Plant
        fields = ['id', 'title', 'image']


class UtilizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilize
        fields = '__all__'


class UtilizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilize
        fields = ['id', 'title', 'image']
