from django.urls import path
from . import views  # Ensure this import exists


urlpatterns = [
    path('', views.role_selection_view, name='role_selection'),  # Use views.role_selection
    path('admin_redirect/', views.admin_redirect_view, name='admin_redirect'),
    path('customer_options/', views.customer_options_view, name='customer_options'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('landing/', views.landing_page, name='landing'),
    path('home/', views.home_view, name='volleyball_home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('account/', views.account_view, name='account'),
    path('place_order/', views.place_order, name='place_order'),
]
