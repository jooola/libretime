from api_clients.version1 import AirtimeApiClient as ApiClient


def authenticate_live_stream_user(
    username: str,
    password: str,
    source: str,
):
    api = ApiClient()
    response = api.check_live_stream_auth(username, password, source)
    return "msg" in response and response["msg"] == True
