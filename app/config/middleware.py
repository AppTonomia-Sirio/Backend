from django.http import JsonResponse


# Middleware to handle 404 errors
class NotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return JsonResponse({'error': 'Not found'}, status=404)
        return response


class InternalServerError:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
        return response
