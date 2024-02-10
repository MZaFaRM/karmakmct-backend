from rest_framework.response import Response
from rest_framework import status


class CustomResponse(Response):
    def __init__(
        self, message, data=None, errors=None, status=status.HTTP_400_BAD_REQUEST
    ):
        if errors is None:
            errors = []
        if data is None:
            data = {}
            
        super().__init__(
            status=status,
            data={
                "message": message,
                "status": status,
                "response": {
                    "errors": errors,
                    "data": data,
                },
            },
        )
