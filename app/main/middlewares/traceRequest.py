import uuid
from django.http import HttpRequest

class TraceRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        trace_id = uuid.uuid4()
        request.headers.__setattr__('X-Trace-ID', str(trace_id))
        response = self.get_response(request)

        response['X-Trace-ID'] = str(trace_id)

        return response