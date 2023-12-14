from django.urls import path
from django.conf.urls.static import static
from EShopHub import settings
from store import views
from store.views import ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryListView, \
    CategoryDetailView, CategoryCreateView, TagListView

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('catalog/add/', ProductCreateView.as_view(), name='product_add'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products_by_category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('products_by_tag/<str:tag_name>/', views.products_by_tag, name='products_by_tag'),
    path('catalog/categories/', CategoryListView.as_view(), name='category_list'),
    path('catalog/categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('catalog/categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('catalog/tags/', TagListView.as_view(), name='tag_list'),
    path('catalog/tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('catalog/tags/add/', views.TagCreateView.as_view(), name='tag_add'),
    path('catalog/add_category/', views.add_category, name='add_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
