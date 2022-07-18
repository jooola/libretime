from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, conlist, Field, AnyHttpUrl
from typing_extensions import Annotated, Literal


class IcecastConnection(BaseModel):
    kind: Literal["icecast"] = "icecast"
    host: str = "localhost"
    port: int = 8000
    mount: str = "main"
    admin_username: str = "admin"
    admin_password: str = ""
    username: str = "source"
    password: str = "hackme"


class ShoutcastConnection(BaseModel):
    kind: Literal["shoutcast"] = "shoutcast"
    host: str = "localhost"
    port: int = 8000
    mount: str = "main"
    admin_username: str = "admin"
    admin_password: str = ""
    username: str = "source"
    password: str = "hackme"


class HLSConnection(BaseModel):
    kind: Literal["hls"] = "hls"
    path: Path = Path.cwd() / "hls"
    playlist: str = "main.m3u8"


# (?id : string,
# ?encode_metadata : bool,
# ?fallible : bool,
# ?on_file_change : ((state : string, string) -> unit),
# ?on_start : (() -> unit),
# ?on_stop : (() -> unit),
# ?perm : int,
# ?persist : bool,
# ?persist_at : string,
# ?playlist : string,
# ?segment_duration : float,
# ?segment_name : ((position : int, extname : string, string) -> string),
# ?segments : int,
# ?segments_overhead : int,
# ?start : bool,
# ?streams_info : [string * (int * string * string)],
# string, [string * format('a)], source('a)) ->
# active_source('a)


Connection = Annotated[
    Union[IcecastConnection, ShoutcastConnection],
    Field(discriminator="kind"),
]


class OutputMeta(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[AnyHttpUrl] = None
    genre: Optional[str] = None


class OutputAudio(BaseModel):
    format: str = "ogg"
    bitrate: int = 256
    channels: int = 2


class Output(BaseModel):
    enabled: bool = False
    url: Optional[AnyHttpUrl] = None
    meta: OutputMeta = OutputMeta()
    audio: OutputAudio = OutputAudio()
    connection: Connection = IcecastConnection()


class Input(BaseModel):
    stream_port: int = 8001
    stream_mount: str = "/main"


class StreamsConfig(BaseModel):
    outputs: Optional[conlist(Output, min_items=1, max_items=4)]

    live_main: MainInput
    live_show: MainInput
    main_live_stream_port: int = 8001
    main_live_stream_mount: str = "/main"
    show_live_stream_port: int = 8002
    show_live_stream_mount: str = "/show"

    # Icecast
    icecast_vorbis_metadata: bool = False

    # Meta
    off_air_meta: str = "Offline"
    output_sound_device: bool = False
    output_sound_device_type: str = "ALSA"
    log_filepath: str = "liquidsoap.log"
    auth_command: str = "libretime-liquidsoap auth"


# class StreamInput(BaseModel):
#     enabled: bool =False
#     kind: str
#     public_url: Optional[AnyHttpUrl]= None
#     instructions: Optional[str] = None

# class IcecastStreamInput(StreamInput):
#     port: int= 8001
#     mount: str
#     username: str = "source"
#     password: str

# class StreamInputs(BaseModel):
#     main: Optional[IcecastStreamInput]
#     show: Optional[IcecastStreamInput]


# class IcecastStreamOutput(BaseModel):
#     public_url: str = "https://stream.radio.org/main.mp3"
#     host: str = "localhost"
#     port: int = 8000
#     mount: str
#     admin_username: str = "admin"
#     admin_password: str
#     username: str = "source"
#     password: str = "SOME_SECRET"


# class OutputMeta(BaseModel):
#     name: str = "Radio"
#     description: Optional[str]
#     url: str = "https://www.radio.org"
#     genre: str = "various"


# class OutputAudio(BaseModel):
#     format: str = "ogg"
#     bitrate: int = 256
#     channels: int = 2


# class StreamOutput(BaseModel):
#     enabled: bool = False
#     public_url: Optional[str]
#     output_kind: str
#     output: IcecastStreamOutput
