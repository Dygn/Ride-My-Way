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
                'message': 'User {} was created'.format( data['username'])
            }
        except:
            return {'message': 'Something went wrong'}, 500

class Login(Resource):
    def post(self):
        pass
      
      
class LogoutAccess(Resource):
    def post(self):
        pass
      
      
class LogoutRefresh(Resource):
    def post(self):
        pass 
      
      
class TokenRefresh(Resource):
    def post(self):
        pass
      
      
