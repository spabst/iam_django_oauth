from oauth2_provider.decorators import protected_resource
from django.http import JsonResponse


@protected_resource()
def secret_page(request):
    user = request.user  # The user authenticated by the access token
    return JsonResponse({"message": f"Hello, {user}"})