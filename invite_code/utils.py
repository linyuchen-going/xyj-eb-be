# -*- coding: UTF8 -*-
import hashlib
from user.models import User
from uuid import uuid4
from .models import CODE_LENGTH


def create_invite_code(user: User) -> str:
    m = hashlib.blake2b(digest_size=CODE_LENGTH / 2)
    m.update(bytes(str(user.id) + uuid4().hex, encoding="utf8"))
    return m.hexdigest()
