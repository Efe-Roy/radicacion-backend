from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('account.urls')),
    # path('files/', include('filed.urls', namespace="files")),
    # path('agents/',  include('agents.urls', namespace="agents")),

    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),

    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),

    # Api Banger Boos
    path('api/', include("filed.api.urls")),
    path('api/auth/', include("account.api.urls")),
    path('api/agent/', include("agents.api.urls")),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)