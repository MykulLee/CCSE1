from django.contrib import admin
from .models import CustomUser, Order, Volleyball
from django.contrib.auth.admin import UserAdmin


class VolleyballAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','quantity')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_superuser', 'security_answer')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('security_answer',)}),
    )

admin.site.register(Order)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Volleyball, VolleyballAdmin)