from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('product/<int:id>', views.product_details),
    path('collections/<int:pk>', views.collection_detail, name='collection-detail'),
]
