from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_nested import routers

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'product', lookup='product')
# products_router.register('')

urlpatterns = router.urls
