from django.shortcuts import render
from django.http import HttpResponse
from .models import Volleyball
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import CustomUser
from .models import CartItem
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
User = get_user_model()
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order




def home_view(request):
    volleyball = Volleyball.objects.all()
    return render(request, 'home.html', {'volleyball' : volleyball})

def role_selection_view(request):
    if request.method == 'POST':
        selected_role = request.POST.get('role')
        if selected_role == 'admin':
            return redirect('/admin/login/?next=/admin/')
        elif selected_role == 'customer':
            return redirect('customer_options')
    return render(request, 'role_selection.html')


def admin_redirect_view(request):
    return redirect('/admin')

def customer_options_view(request):
    return render(request, 'customer_options.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        security_answer = request.POST.get('security_question')
        user = User.objects.create_user(username=username, password=password, security_answer=security_answer)


        if username and password and security_answer:
            user = User.objects.create_user(username=username, password=password, security_answer=security_answer)
            user.save()
            return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        security_answer = request.POST.get('security_question')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.security_answer == security_answer:
            login(request, user)
            return redirect('volleyball_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or security answer.'})
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def landing_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'landing.html')

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    from .models import Volleyball
    volleyball = Volleyball.objects.all()
    return render(request, 'home.html', {'volleyball': volleyball})

def role_selection(request):
    return render(request, 'role_selection.html')

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    product = Volleyball.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def remove_from_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
    if cart_item:
        cart_item.delete()
    return redirect('view_cart')

def clear_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    CartItem.objects.filter(user=request.user).delete()
    return redirect('view_cart')

def checkout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart_items = CartItem.objects.filter(user=request.user)
    products = [item.product for item in cart_items]

    if request.method == 'POST':
        messages.success(request, "Order placed successfully")
        CartItem.objects.filter(user=request.user).delete()
        return redirect('volleyball_home')
    
    return render(request, 'checkout.html', {'products': products})

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')
        new_security_answer = request.POST.get('security_answer')

        user = request.user
        if new_username:
            user.username = new_username
        if new_password:
            user.set_password(new_password)
        if new_security_answer:
            user.security_answer = new_security_answer
        user.save()

        update_session_auth_hash(request, user)

        return redirect('account')

    return render(request, 'account.html', {'user': request.user, 'security_question': 'What is the name of your first pet?'})



@csrf_exempt
def place_order(request):
    if request.method == "POST":
        user = request.user
        product_ids = request.POST.getlist('product_id')
        quantities = request.POST.getlist('quantity')
        delivery_address = request.POST.get('delivery_address')
        payment_details = request.POST.get('payment_details')

        for product_id, quantity in zip(product_ids, quantities):
            product = Volleyball.objects.get(id=product_id)
            Order.objects.create(user=user, product=product, quantity=int(quantity))

        messages.success(request, "Order placed successfully")
        CartItem.objects.filter(user=request.user).delete()
        return redirect('volleyball_home')

    return JsonResponse({"error": "Invalid request."}, status=400)

