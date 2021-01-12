from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import run_async, run_sync


class TheFirstOnesView(APIView):
    def post(self, request):
        search_dict = {}
        if settings.ASYNC == "True":
            search_dict = run_async(request.data["body"])
        else:
            for query in request.data["body"]:
                search_dict[query] = run_sync(query)
        return Response([search_dict])
