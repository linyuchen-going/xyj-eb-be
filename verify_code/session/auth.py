# -*- coding: UTF8 -*-


def verify_code(request, session_key: str, code: str) -> bool:

    code = code.strip().lower()
    real_code = request.session.get(session_key)
    if not real_code:
        return False
    real_code = real_code.lower()
    result = real_code == code
    if result:
        request.session[session_key] = None

    return result
