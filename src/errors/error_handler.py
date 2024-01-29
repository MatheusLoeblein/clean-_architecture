from src.presentation.http_types.http_response import HttpResponse
from .types import HttpBadRequestError, HttpNotFoundError

def handle_errors(error: Exception) -> HttpResponse:

    if isinstance(error, (HttpBadRequestError, HttpNotFoundError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
            status_code=500,
            body={
                "errors": [{
                    "title": "server error",
                    "detail": str(error)
                }]
            }
        )
