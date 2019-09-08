from app.libs.redprint import Redprint

api = Redprint('client')


@api.route('register', methods=['POST'])
def create_client():
    pass


