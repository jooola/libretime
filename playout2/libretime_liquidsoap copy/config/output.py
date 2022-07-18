from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, conlist, conint, Field, AnyHttpUrl, validator
from typing_extensions import Annotated, Literal


class BaseAudio(BaseModel):
    channels: int = 2


class AudioMp3(BaseAudio):
    format: Literal["mp3"] = "mp3"
    bitrate: int = 256

    ALLOWED_BITRATE = (64, 96, 128, 160, 192, 224, 256, 320)

    @classmethod
    @validator("bitrate")
    def bitrate_must_be_valid(cls, value):
        if value not in cls.ALLOWED_BITRATE:
            raise ValueError(f"must be one of {cls.ALLOWED_BITRATE}")
        return value


class AudioAac(BaseAudio):
    format: Literal["aac"] = "aac"
    bitrate: int = 256

    ALLOWED_BITRATE = (64, 96, 128, 160, 192, 224, 256, 320)

    @classmethod
    @validator("bitrate")
    def bitrate_must_be_valid(cls, value):
        if value not in cls.ALLOWED_BITRATE:
            raise ValueError(f"must be one of {cls.ALLOWED_BITRATE}")
        return value


class AudioOggVorbis(BaseAudio):
    format: Literal["vorbis"] = "vorbis"
    bitrate: int = 256


class AudioOggOpus(BaseAudio):
    format: Literal["opus"] = "opus"
    bitrate: int = 256

    @classmethod
    @validator("bitrate")
    def bitrate_must_be_valid(cls, value):
        if 5 < value and value < 512:
            raise ValueError("must be between 5 and 512")
        return value


class BaseIcecastConnection(BaseModel):
    host: str = "localhost"
    port: int = 8000
    mount: str = "main"
    username: str = "source"
    password: str = "hackme"

    # Stats
    admin_username: str = "admin"
    admin_password: Optional[str] = None


class IcecastConnection(BaseIcecastConnection):
    kind: Literal["icecast"] = "icecast"
    audio: Annotated[
        Union[AudioMp3, AudioOggOpus, AudioOggVorbis],
        Field(discriminator="format"),
    ] = AudioOggVorbis()


class ShoutcastConnection(BaseModel):
    kind: Literal["shoutcast"] = "shoutcast"
    audio: Annotated[
        Union[AudioMp3, AudioOggOpus, AudioOggVorbis],
        Field(discriminator="format"),
    ] = AudioOggVorbis()


class HLSConnection(BaseModel):
    kind: Literal["hls"] = "hls"
    path: Path = Path.cwd() / "hls"
    playlist: str = "main.m3u8"


Connection = Annotated[
    Union[
        IcecastConnection,
        ShoutcastConnection,
        HLSConnection,
    ],
    Field(discriminator="kind"),
]


class Output(BaseModel):
    enabled: bool = False
    name: Optional[str] = None
    url: Optional[AnyHttpUrl] = None
    connection: Connection = IcecastConnection()
