def render_json(message, code, status, data=None):
    response = {
        "meta": {
            "message": message,
            "code": code,
            "status": status
        },
        "data": data
    }

    return response, code
