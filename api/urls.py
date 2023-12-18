from django.urls import path
from api import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product-api', views.ProductViewSet)
router.register(r'category-api', views.CategoryViewSet)
router.register(r'tag-api', views.TagViewSet)
router.register(r'order-api', views.OrderViewSet)
router.register(r'order_position-api', views.OrderItemViewSet)


urlpatterns = [
    path('api/product/', views.product_api),
    path('api/product/<int:pk>', views.product_api_detail),
    path('api/category/', views.category_api),
    path('api/category/<int:pk>', views.category_api_detail),
    path('api/tag/', views.tag_api),
    path('api/tag/<int:pk>', views.tag_api_detail),
    path('api/order/', views.order_api),
    path('api/order/<int:pk>', views.order_api_detail),
    path('api/order_pos/', views.order_pos_api),
    path('api/order_pos/<int:pk>', views.order_pos_api_detail),
]