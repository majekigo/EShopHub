from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls.static import static
from EShopHub import settings
from store import views
from store.views import ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryListView, \
    CategoryDetailView, CategoryCreateView, TagListView, register_user

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('catalog/add/', ProductCreateView, name='product_add'),
    path('catalog/<int:pk>/update/', ProductUpdateView, name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView, name='product_delete'),
    path('products_by_category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('products_by_tag/<str:tag_name>/', views.products_by_tag, name='products_by_tag'),
    path('catalog/categories/', CategoryListView.as_view(), name='category_list'),
    path('catalog/categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('catalog/categories/add/', CategoryCreateView, name='category_add'),
    path('catalog/tags/', TagListView.as_view(), name='tag_list'),
    path('catalog/tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('catalog/tags/add/', views.TagCreateView, name='tag_add'),
    path('catalog/add_category/', views.add_category, name='add_category'),
    path('orders/add/', views.OrderCreateView, name='create_order'),
    path('orders/', views.OrderListView, name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView, name='order_detail'),
    path('orders/<int:pk>/update/', views.OrderUpdateView, name='order_update'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView, name='order_delete'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
