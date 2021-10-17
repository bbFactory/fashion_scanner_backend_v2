from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# from .api_docs import schema_view
from health_check import urls as health_urls

urlpatterns = [
    # path("swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    # path(
    #     settings.SWAGGER_URL,
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    # path(
    #     settings.REDOC_URL,
    #     schema_view.with_ui("redoc", cache_timeout=0),
    #     name="schema-redoc",
    # ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    # path("api/users/login", obtain_auth_token),
    path("api/v1/", include("config.api_router")),
    # Health checks:
    path("health/", include(health_urls)),  # noqa: DJ05
    # DRF login
]

if settings.DEBUG:

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
