from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('', methods=['GET'])
def get_user():
    return "i am mgw"
