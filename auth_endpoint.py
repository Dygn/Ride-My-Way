from flask_restful import Resource, reqparse
from model import UserModel

parser = reqparse.RequestParser()
parser.add_argument('username',required=True)
parser.add_argument('password',required=True)

class SignUp(Resource):
    def post(self):
        data = parser.parse_args()
        newuser = UserModel (data['username'], data['password'])
        try:
            newuser.save()
            return {
                'message': 'User {} was created'.format(data['username'])
            }
        except:
            return {'message': 'Something went wrong'}, 500

class Login(Resource):
    def post(self):
        data = parser.parse_args()
        current_u = UserModel (data['username'], data['password'])
        registered= current_u.find_user(data['username'])
        if not registered:
            
            return {'message': 'User {} doesnt exists'.format(data['username'])}
        if data['password'] == registered[1]:
            return {'message': 'Logged in as {}'.format(registered[0])}
        else:
            return {'message': 'Wrong credentials'}
      
      
class LogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class LogoutRefresh(Resource):
    def post(self):
        return {'message': 'Use'}
      
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}
      
      
class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}
      
