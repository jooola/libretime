from enum import Enum
from typing import Optional, Union

from pydantic import AnyHttpUrl, BaseModel, Field, validator
from typing_extensions import Annotated, Literal


class AudioMP3(BaseModel):
    format: Literal["mp3"] = "mp3"
    bitrate: int = 256

    @classmethod
    @validator("bitrate")
    def bitrate_must_be_valid(cls, value):
        allowed_bitrate = (64, 96, 128, 160, 192, 224, 256, 320)
        if value not in allowed_bitrate:
            raise ValueError(f"must be one of {allowed_bitrate}")
        return value


class AudioAAC(BaseModel):
    format: Literal["aac"] = "aac"
    bitrate: int = 256

    @classmethod
    @validator("bitrate")
    def bitrate_must_be_valid(cls, value):
        allowed_bitrate = (
            64,
            96,
            128,
            160,
            192,
            224,
            256,
            320,
        )
        if value not in allowed_bitrate:
            raise ValueError(f"must be one of {allowed_bitrate}")
        return value


class AudioOgg(BaseModel):
    format: Literal["ogg"] = "ogg"
    bitrate: int = 256
    quality: Optional[int] = None

    @classmethod
    @validator("bitrate")
    def bitrate_must_be_valid(cls, value):
        allowed_bitrate = (64, 96, 128, 160, 192, 224, 256, 320, 500)
        if value not in allowed_bitrate:
            raise ValueError(f"must be one of {allowed_bitrate}")
        return value


class AudioOpus(BaseModel):
    format: Literal["opus"] = "opus"
    bitrate: int = 256

    @classmethod
    @validator("bitrate")
    def bitrate_must_be_valid(cls, value):
        if 5 < value and value < 512:
            raise ValueError("must be between 5 and 512")
        return value


IcecastAudio = Annotated[
    Union[AudioMP3, AudioAAC, AudioOgg, AudioOpus],
    Field(discriminator="format"),
]


class IcecastConnection(BaseModel):
    kind: Literal["icecast"]
    host: str = "localhost"
    port: int = 8000
    mount: str = "main"
    username: str = "source"
    password: str = "hackme"

    audio: IcecastAudio = AudioOgg()

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
