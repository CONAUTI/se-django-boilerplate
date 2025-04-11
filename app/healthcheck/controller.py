from .services.healthcheck_service import HealthcheckService
from main.utils.response import Response, HttpRequest

class HealthcheckController:
    def __init__(self, healthcheckService: HealthcheckService):
        self.healtcheckService = healthcheckService
        
    def get_healthcheck(self, request: HttpRequest):
        result = self.healtcheckService.check()
        return Response.ok(
            result,
            'Healthcheck successful'
        )