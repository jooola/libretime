from typing import Optional, Union

from libretime_shared.config import BaseConfig
from pydantic import AnyHttpUrl, BaseModel, Field, conlist
from typing_extensions import Annotated, Literal


class IcecastConnection(BaseModel):
    kind: Literal["icecast"]
    host: str = "localhost"
    port: int = 8000
    mount: str = "main"
    username: str = "source"
    password: str = "hackme"
    admin_username: Optional[str] = None
    admin_password: Optional[str] = None


class HLSConnection(BaseModel):
    kind: Literal["hls"] = "hls"
    path: str = "./hls/"


Connection = Annotated[
    Union[HLSConnection, IcecastConnection],
    Field(discriminator="kind"),
]


class Output(BaseModel):
    enabled: bool = False
    url: Optional[AnyHttpUrl]
    connection: Connection


class Input:
    enabled: bool = False
    url: Optional[AnyHttpUrl]
    connection: Connection


class Inputs(BaseModel):
    main: Input
    show: Input


class Config(BaseConfig):
    inputs: Inputs
    outputs: Optional[conlist(Output, min_items=1, max_items=4)]


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
