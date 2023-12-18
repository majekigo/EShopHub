from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from store.forms import CategoryForm, ProductForm, TagForm, OrderForm, OrderPositionFormSet
from store.models import Product, Tag, Category, Order
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


@permission_required('add_category')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@login_required
def products_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    products_with_tag = Product.objects.filter(tags=tag)
    return render(request, 'products_by_tag.html', {'products': products_with_tag, 'tag': tag})


@login_required
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


@permission_required('add_product')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'ProductView/product_add.html'
    success_url = reverse_lazy('catalog')


@permission_required('change_product')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'ProductView/product_update.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog')


@permission_required('delete_product')
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


@permission_required('add_category')
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


@permission_required('add_tag')
class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'TagView/tag_add.html'
    success_url = reverse_lazy('tag_list')


@login_required
#Order
class OrderListView(ListView):
    model = Order
    template_name = 'OrderView/order_list.html'
    context_object_name = 'orders'
    paginate_by = 3


@login_required
class OrderDetailView(DetailView):
    model = Order
    template_name = 'OrderView/order_detail.html'
    context_object_name = 'order'


@permission_required('add_order')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'OrderView/order_add.html'
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OrderPositionFormSet(self.request.POST, prefix='order_positions')
        else:
            context['formset'] = OrderPositionFormSet(prefix='order_positions')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(reverse_lazy('order_list'))
        else:
            return redirect(reverse_lazy('create_order'))


@permission_required('change_order')
class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'OrderView/order_update.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OrderPositionFormSet(
                self.request.POST, instance=self.object)
        else:
            context['formset'] = OrderPositionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


@permission_required('delete_order')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'OrderView/order_delete.html'
    context_object_name = 'order'
    success_url = reverse_lazy('order_list')
