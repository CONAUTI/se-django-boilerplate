from functools import wraps
from main.utils.response import Response
from main.errors.base import BaseException

def handle_request(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except BaseException as e:
            return e.toResponse()
        except Exception as e:
            return Response.error(str(e))
    return wrapper