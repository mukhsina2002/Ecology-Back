from django.urls import path

from ecology_app.views import AnimalListView, AnimalDetailView, PlantListView, PlantDetailView, NatureListView, \
    UtilizeListView, UtilizeDetailView, UtilizeViewByType

urlpatterns = [
    path('animals/', AnimalListView.as_view(), name='animal-list'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
    path('plants/', PlantListView.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('nature/', NatureListView.as_view(), name='product-list'),
    path('utilizes/', UtilizeListView.as_view(), name='utilizes-list'),
    path('utilizes/by', UtilizeViewByType.as_view()),
    path('utilizes/<int:pk>/', UtilizeDetailView.as_view(), name='utilizes-detail'),
    # path('send/', ShopInfoView.as_view(), name='telegram-send'),
]
