from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import run_async, run_sync


class TheFirstOnesView(APIView):
    def get(self, request):
        return Response(
            {
                "Example post request": "{'async': 'True', 'sync': 'False', 'search_term': 'google'}"
            }
        )

    def post(self, request):
        search_dict = {}
        for query in request.data["body"]:
            if settings.ASYNC == "True":
                search_dict[query] = run_async(query)
            else:
                search_dict[query] = run_sync(query)
        return Response([search_dict])
