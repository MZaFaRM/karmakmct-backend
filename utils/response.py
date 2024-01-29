from rest_framework.response import Response
from rest_framework import status


class CustomResponse(Response):
    def __init__(
        self,
        message,
        data={},
        errors="",
        status=status.HTTP_400_BAD_REQUEST,
    ):
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
