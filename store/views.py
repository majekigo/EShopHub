from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from store.forms import CategoryForm, ProductForm, TagForm
from store.models import Product, Tag, Category
from django.urls import reverse_lazy


# Create your views here.

#Начало функций
def index(request):
    return render(request, template_name='index.html')


def catalog(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 1)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'catalog.html', {'products': products})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


def products_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    products_with_tag = Product.objects.filter(tags=tag)
    return render(request, 'products_by_tag.html', {'products': products_with_tag, 'tag': tag})


def products_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products_in_category = Product.objects.filter(categories=category)
    return render(request, 'products_by_category.html', {'products': products_in_category, 'category': category})


#Product
class ProductListView(ListView):
    model = Product
    template_name = 'ProductView/product_list.html'
    context_object_name = 'products'
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ProductView/product_about.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'ProductView/product_add.html'
    success_url = reverse_lazy('catalog')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'ProductView/product_update.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'ProductView/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog')


#Category
class CategoryListView(ListView):
    model = Category
    template_name = 'CategoryView/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'CategoryView/category_detail.html'
    context_object_name = 'category'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'CategoryView/category_add.html'
    success_url = reverse_lazy('category_list')


#Tag
class TagListView(ListView):
    model = Tag
    template_name = 'TagView/tag_list.html'
    context_object_name = 'tags'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'TagView/tag_detail.html'
    context_object_name = 'tag'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'TagView/tag_add.html'
    success_url = reverse_lazy('tag_list')
