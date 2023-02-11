from secrets import compare_digest

from rest_framework import exceptions, status, views
from rest_framework.response import Response

from ...permissions import IsSystemTokenOrUser
from ...schedule.models import ShowInstance
from ..models import Preference
from ..serializers import (
    StreamAuthSerializer,
    StreamPreferencesSerializer,
    StreamStateSerializer,
)


class StreamPreferencesView(views.APIView):
    permission_classes = [IsSystemTokenOrUser]
    serializer_class = StreamPreferencesSerializer
    model_permission_name = "streamsetting"

    def get(self, request):
        data = Preference.get_stream_preferences()
        return Response(
            data.dict(
                include={
                    "input_fade_transition",
                    "message_format",
                    "message_offline",
                }
            )
        )


class StreamStateView(views.APIView):
    permission_classes = [IsSystemTokenOrUser]
    serializer_class = StreamStateSerializer
    model_permission_name = "streamsetting"

    def get(self, request):
        data = Preference.get_stream_state()
        return Response(
            data.dict(
                include={
                    "input_main_connected",
                    "input_main_streaming",
                    "input_show_connected",
                    "input_show_streaming",
                    "schedule_streaming",
                }
            )
        )


class StreamAuthView(views.APIView):
    permission_classes = [IsSystemTokenOrUser]
    serializer_class = StreamAuthSerializer
    model_permission_name = "streamsetting"

    def post(self, request):
        serializer = StreamAuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.input == "main":
            stream_preferences = Preference.get_stream_preferences()
            main_username = stream_preferences.input_main_username
            main_password = stream_preferences.input_main_username

            if main_username is None or main_password is None:
                raise exceptions.AuthenticationFailed("invalid credentials")

            if not (
                compare_digest(serializer.username, main_username)
                and compare_digest(serializer.password, main_password)
            ):
                raise exceptions.AuthenticationFailed("invalid credentials")

        elif serializer.input == "show":
            current = ShowInstance.get_current()

            if not current.show.live_enabled:
                raise exceptions.AuthenticationFailed("invalid credentials")

            if current.show.live_auth_custom:
                if not (
                    compare_digest(
                        serializer.username,
                        current.show.live_auth_custom_user,
                    )
                    and compare_digest(
                        serializer.password,
                        current.show.live_auth_custom_password,
                    )
                ):
                    raise exceptions.AuthenticationFailed("invalid credentials")

            raise exceptions.AuthenticationFailed("not implemented input")
        else:
            raise exceptions.AuthenticationFailed("invalid input")

        return Response(status=200)

    #     // check against show dj auth
    #     $showInfo = Application_Model_Show::getCurrentShow();

    #     // there is current playing show
    #     if (isset($showInfo[0]['id'])) {
    #         $current_show_id = $showInfo[0]['id'];
    #         $CcShow = CcShowQuery::create()->findPK($current_show_id);

    #         // get custom pass info from the show
    #         $custom_user = $CcShow->getDbLiveStreamUser();
    #         $custom_pass = $CcShow->getDbLiveStreamPass();

    #         // get hosts ids
    #         $show = new Application_Model_Show($current_show_id);
    #         $hosts_ids = $show->getHostsIds();

    #         // check against hosts auth
    #         if ($CcShow->getDbLiveStreamUsingAirtimeAuth()) {
    #             foreach ($hosts_ids as $host) {
    #                 $h = new Application_Model_User($host['subjs_id']);
    #                 if ($username == $h->getLogin() && md5($password) == $h->getPassword()) {
    #                     $this->view->msg = true;

    #                     return;
    #                 }
    #             }
    #         }
    #         // check against custom auth
    #         if ($CcShow->getDbLiveStreamUsingCustomAuth()) {
    #             if ($username == $custom_user && $password == $custom_pass) {
    #                 $this->view->msg = true;
    #             } else {
    #                 $this->view->msg = false;
    #             }
    #         } else {
    #             $this->view->msg = false;
    #         }
