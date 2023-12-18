from django.test import TestCase
from django.http import JsonResponse


# Tests for the NotFoundMiddleware
class Custom404MiddlewareTestCase(TestCase):
    def test_middleware_handles_404(self):
        # Request a non-existent URL
        url = '/not-found/'
        response = self.client.get(url)

        # Check that the response is a JSON response with status code 404
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response, JsonResponse)
