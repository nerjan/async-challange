from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import run_async, run_sync
import shutil
import pathlib


class TheFirstOnesView(APIView):
    def post(self, request):
        # delete cache folder
        path = pathlib.Path(__file__).parent.parent.absolute()
        try:
            shutil.rmtree(f"{path}/cache")
        except OSError as e:
            print("Cannot delete cache folder")

        search_dict = {}
        if settings.ASYNC == "True":
            search_dict = run_async(request.data["body"])
        else:
            for query in request.data["body"]:
                search_dict[query] = run_sync(query)
        return Response([search_dict])
