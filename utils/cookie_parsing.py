from utils.database import authenticate


def parse_visits(cookies: dict) -> str:
    if 'visits' in cookies:
        new_visits = int(cookies['visits']) + 1
    else:
        new_visits = 1

    return str(new_visits)


def auth_user(cookies) -> str:
    username: str = ""
    if 'auth_token' in cookies:
        if authenticate("", cookies['auth_token']):
            username = authenticate("", cookies['auth_token'])['username']
        # username = 'Trusted User'

    return username
