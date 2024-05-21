from django.shortcuts import render, redirect, get_object_or_404
from basic_app.forms import UserForm, UserProfileInfoForm, BookForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from .models import Book, Cart, CartItem
from .forms import LoginForm, AddToCartForm, ReviewForm

def index(request):
    latest_books = Book.objects.order_by('-publication_date')[:10]
    return render(request, 'basic_app/index.html', {'latest_books': latest_books})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            return redirect(reverse('basic_app:user_login')) 
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def user_login(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))  # Redirect to the index page
            else:
                error_message = "Invalid login credentials."
        else:
            error_message = "Invalid login credentials."
    else:
        form = LoginForm()
    
    return render(request, 'basic_app/login.html', {
        'login_form': form,
        'error_message': error_message
    })

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                return redirect('basic_app:book_detail', book_id=book.id)
        else:
            return redirect('basic_app:user_login')
    else:
        form = ReviewForm()

    return render(request, 'basic_app/book_detail.html', {'book': book, 'reviews': reviews, 'form': form})

def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        books = []
    return render(request, 'basic_app/book_search.html', {'books': books, 'query': query})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))  # Redirect to the index page
    else:
        form = BookForm()
    
    return render(request, 'basic_app/add_book.html', {'form': form})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))  # Redirect to the index page
    else:
        form = BookForm(instance=book)
    
    return render(request, 'basic_app/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect(reverse('index'))  # Redirect to the index page
    
    return render(request, 'basic_app/delete_book.html', {'book': book})

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            book = get_object_or_404(Book, id=form.cleaned_data['book_id'])
            quantity = form.cleaned_data['quantity']
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return redirect('basic_app:view_cart')
    return redirect(reverse('index'))

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_cost = sum(item.total_price() for item in cart_items)
    return render(request, 'basic_app/view_cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_cost = sum(item.total_price() for item in cart_items)
    if request.method == 'POST':
        # Here you would handle the payment process
        cart_items.delete()  # Clear the cart after checkout
        return redirect(reverse('index'))
    return render(request, 'basic_app/checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect(reverse('basic_app:view_cart'))
