from django.urls import path

from .controller import HealthcheckController
from .services.implements.healthcheck_service_impl import HeatlhcheckServiceImpl

controller = HealthcheckController(HeatlhcheckServiceImpl())

urlpatterns = [
    path('healthcheck/', controller.get_healthcheck, name='healthcheck'),
]