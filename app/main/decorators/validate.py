from functools import wraps
import json
from django.http import JsonResponse
from pydantic import ValidationError

def validate(schema_class):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            request = args[1] if len(args) > 1 else kwargs.get('request')

            try:
                raw_body = request.body.decode('utf-8')
                data = json.loads(raw_body) if raw_body else {}
                parsed = schema_class(**data)
                request.validated_data = parsed

                return view_func(*args, **kwargs)

            except ValidationError as e:
                errors = [
                    {
                        "field": ".".join(str(x) for x in err['loc']),
                        "message": err['msg']
                    }
                    for err in e.errors()
                ]
                return JsonResponse({
                    "error": "Validation failed",
                    "details": errors
                }, status=400)

            except Exception as e:
                return JsonResponse({
                    "error": "Server error",
                    "message": str(e)
                }, status=500)

        return wrapper
    return decorator
