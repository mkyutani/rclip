#!/usr/bin/env python3

from pydantic import BaseModel
from typing import Optional

class MessageModel(BaseModel):
    message: str
    category: Optional[str] = None

class TTLModel(BaseModel):
    ttl: Optional[int] = None
