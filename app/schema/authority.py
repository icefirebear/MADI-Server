from typing import Optional, List
from enum import Enum

from pydantic import BaseModel, HttpUrl


class Authority(Enum):
    name = "name"
    gender = "gender"
    std_no = "std_no"
    profile_image = "profile_image"
