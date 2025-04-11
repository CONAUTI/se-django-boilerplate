from main.errors.base import BaseException

class BadRequestException(BaseException):
    def __init__(self, message):
        super().__init__(message, {}, {
            'name': 'BadRequestException',
            'status': 400,
        })
