from django.http import JsonResponse

class BaseException(Exception):
    def __init__(self, message, data, options, meta={}):
        self.message = message
        self.data = data
        self.options = options
        self.meta = meta

    def toResponse(self):
        payload = {
            'success': False,
            'message': self.message,
            'data': {
                'error': {
                    'name': self.options.get('name', 'Error'),
                }
            }
        }

        if self.meta:
            payload['meta'] = self.meta

        return JsonResponse(payload, status=self.options.get('status', 500))