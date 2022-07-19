from shutil import disk_usage, which
from subprocess import run

from django.conf import settings
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import StatusSerializer, VersionSerializer


class StatusView(APIView):
    permission_classes = [AllowAny]
    serializer_class = StatusSerializer

    def get(self, request):
        result = {}

        if which("systemctl") is not None:
            result["services"] = {}
            for service in [
                "libretime-api",
                "libretime-celery",
                "libretime-analyzer",
                "libretime-playout",
                "libretime-liquidsoap",
            ]:
                # pylint: disable=subprocess-run-check
                cmd = run(["systemctl", "--quiet", "is-active", service])
                result["services"][service] = cmd.returncode == 0

        storage_usage = disk_usage(settings.CONFIG.storage.path)
        result["storage_usage"] = {
            "total": storage_usage.total,
            "used": storage_usage.used,
            "free": storage_usage.free,
        }

        return Response(result)


class VersionView(APIView):
    permission_classes = [AllowAny]
    serializer_class = VersionSerializer

    def get(self, request):
        return Response({"api_version": settings.API_VERSION})


class InfoView(APIView):
    permission_classes = [AllowAny]
    serializer_class = InfoSerializer

    def get(self, request):
        data = Preference.get_site_preferences()
        return Response(
            data.dict(
                include={
                    "station_name",
                }
            )
        )
