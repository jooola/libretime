from typing import Optional

from pydantic import AnyHttpUrl, BaseModel
from typing_extensions import Literal


class IcecastConnection(BaseModel):
    kind: Literal["icecast"]
    port: int
    mount: str


class Input(BaseModel):
    enabled: bool = False
    url: Optional[AnyHttpUrl]
    connection: IcecastConnection


class Inputs(BaseModel):
    main: Input
    show: Input
