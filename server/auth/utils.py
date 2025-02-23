import shortuuid


def generate_short_id():
    return shortuuid.uuid()[:6]
