from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('volleyball/'), name='root_redirect'),
    path('admin/', admin.site.urls),
    path('volleyball/', include('volleyball.urls'))
]

