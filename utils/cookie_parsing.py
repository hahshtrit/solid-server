from utils.database import authenticate


def parse_visits(cookies: dict) -> str:
    if 'visits' in cookies:
        new_visits = int(cookies['visits']) + 1
    else:
        new_visits = 1

    return str(new_visits)


# might have to refactor this
def auth_user(cookies) -> str:
    username: str = ""
    if 'auth_token' in cookies:
        if authenticate("", cookies['auth_token']):
            username = authenticate("", cookies['auth_token'])['username']
        # username = 'Trusted User'

    return username


def photo_user(cookies):
    pic = b""
    if 'auth_token' in cookies:
        if authenticate("", cookies['auth_token']):
            pic = authenticate("", cookies['auth_token'])['profile_pic']

    return pic


def get_pref(cookies) -> bool:
    pref = True
    if 'auth_token' in cookies:
        if authenticate("", cookies['auth_token']):
            pref = authenticate("", cookies['auth_token'])['dog']

    return pref
