from django.http import JsonResponse
from django.views import View

class GetUser(View):
    def get(self, request, *args, **kwargs):
        # Your logic here
        return JsonResponse({"message": "User info"})
