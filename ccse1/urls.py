from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import TemplateView   

urlpatterns = [
    # Redirect root to volleyball/
    path("", lambda request: redirect("volleyball/"), name="root_redirect"),

    path("admin/", admin.site.urls),
    path("volleyball/", include("volleyball.urls")),

    # robots.txt and sitemap.xml served via templates so CSP middleware runs
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots_txt",
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(
            template_name="sitemap.xml",
            content_type="application/xml",
        ),
        name="sitemap_xml",
    ),
]