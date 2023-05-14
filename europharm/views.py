from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from .models import *
from .forms import AddProductForm, AddUserForm, EditUserForm, AddProductFormUser


class index(View):
    def get(self, request):
        products = Product.objects.order_by('-last_viewed')
        message = "Последние просмотренные"
        context = {
            'products': products,
            'message': message
        }
        return render(request, '../template/main/index.html', context)


class up(View):
    def get(self, request):
        products = Product.objects.order_by('price')
        message = "Сначала дешевые"
        context = {
            'products': products,
            'message': message
        }
        return render(request, '../template/main/index.html', context)


class down(View):
    def get(self, request):
        products = Product.objects.order_by('-price')
        message = "Сначало дорогие"
        context = {
            'products': products,
            'message': message
        }
        return render(request, '../template/main/index.html', context)


class alphabet(View):
    def get(self, request):
        products = Product.objects.order_by('title')
        message = "По алфавиту"
        context = {
            'products': products,
            'message': message
        }
        return render(request, '../template/main/index.html', context)


class acc(View):
    def get(self, request):
        return render(request, '../template/account/dashboard.html')


class basket(View):
    def get(self, request):
        return render(request, '../template/main/basket.html')


class detail(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug, in_stock=True)
        product.last_viewed = datetime.now()
        product.save()
        return render(request, '../template/main/items.html', {'product': product})


class log(View):
    def get(self, request):
        return render(request, '../template/registration/login.html')


class register(View):
    def get(self, request):
        form = UserCreationForm(request.POST)
        return render(request, '../template/registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password1 = request.POST['password1']
            form.save()
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('log')
        return render(request, '../template/registration/register.html', {'form': form})


class admin_page(View):
    def get(self, request):
        users = User.objects.all()
        products = Product.objects.all()
        context = {'products': products, 'users': users}
        return render(request, '../template/main/admin-page.html', context)


class add_product_admin(View):
    def get(self, request):
        form = AddProductForm()
        return render(request, '../template/main/product.html', {'form': form})

    def post(self, request):
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.save()
            return redirect('/acc/')
        else:
            return render(request, '../template/main/product.html', {'form': form})


class add_product_user(View):
    def get(self, request):
        form = AddProductFormUser()
        return render(request, '../template/main/product.html', {'form': form})

    def post(self, request):
        form = AddProductFormUser(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.is_active = False
            item.save()
            return redirect('/acc/')
        else:
            return render(request, '../template/main/product.html', {'form': form})


class add_user(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, '../template/main/user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_page/')
        else:
            return render(request, '../template/main/user.html', {'form': form})


class delete_product(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('/admin_page/')


class delete_user(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        user = User.objects.get(id=id)
        user.delete()
        return redirect('/admin_page/')


class edit_product(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = AddProductForm(instance=product)
        return render(request, '../template/main/edit-product.html', {'form': form})

    def post(self, request, id):
        product = Product.objects.get(id=id)
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/admin_page/')


class edit_user(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        form = EditUserForm(instance=user)
        return render(request, '../template/main/edit-user.html', {'form': form})

    def post(self, request, id):
        user = User.objects.get(id=id)
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/acc/')


class Search(ListView):
    template_name = '../template/main/index.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search')
        return context

