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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from asegurado.views import asegurado_list, crear_asegurado, actualizar_asegurado
from contrato.views import ContratoListView, planes_pago

urlpatterns = [
    path('', asegurado_list, name='asegurado-list'),
    path('asegurado-create/', crear_asegurado, name='asegurado-create'),
    path('asegurado-update/<int:asegurado_id>',
         actualizar_asegurado, name='asegurado-update'),
    path('contratos/', ContratoListView.as_view(), name='contrato-list'),
    path('planes-pago/', planes_pago, name='planes-pago'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
