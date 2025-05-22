from django.utils.deprecation import MiddlewareMixin

class PermissionsPolicyMiddleware(MiddlewareMixin):
    POLICY = "camera=(), geolocation=(), microphone=()"     # deny selected browser APIs
    def process_response(self, request, response):
        response["Permissions-Policy"] = self.POLICY        # attach header to outgoing response
        return response

class StripServerHeaderMiddleware(MiddlewareMixin):
    """Remove Server banner that a proxy / gunicorn may add in prod."""
    def process_response(self, request, response):
        response["Server"] = "secure"                       # replace version-revealing banner
        return response
