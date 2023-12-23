from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
import json

application = get_wsgi_application()

def handler(request, context):
    response = application(request, context)
    return {
        "statusCode": response.status_code,
        "headers": dict(response.items()),
        "body": response.content.decode("utf-8")
    }