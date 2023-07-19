"""
URL configuration for santamaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from contrato.views import planes_pago, generar_plan_pago
from django.views.generic import RedirectView


class AseguradoRedirect(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'asegurado-list'


urlpatterns = [
    path('generar-plan/<int:pk>/', generar_plan_pago, name='generar-plan'),
    path('plan-pago/', planes_pago, name='plan-pago'),
    path('admin/', admin.site.urls),
    path('asegurado/', include('asegurado.urls')),
    path('contrato/', include('contrato.urls')),
    path('', AseguradoRedirect.as_view(), name='index'),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)