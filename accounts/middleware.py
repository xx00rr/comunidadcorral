class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.organization = None
        if request.user.is_authenticated and request.user.organization_id:
            request.organization = request.user.organization
        return self.get_response(request)
