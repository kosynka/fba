from product.views import ProductList, ProductDetail
from django.contrib import admin
import django.urls as urls
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(
    title="Sayat's FBA project API",
    public=True,
    permission_classes=(permissions.AllowAny),
    )

urlpatterns = [
    urls.path('admin/', admin.site.urls),

    urls.path('supplier/', urls.include('fba.urls.supplier')),
    urls.path('customer/', urls.include('fba.urls.customer')),

    urls.path('api/v1/', urls.include(
        urls.path('products/', ProductList.as_view(), name='product-list'),
        urls.path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
        # ...
        # api with drf
        # ...
    )),

    urls.path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
]
