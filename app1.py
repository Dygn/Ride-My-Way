from flask import Flask
import psycopg2
app = Flask(__name__)
from flask_restful import Api
import views,auth_endpoints#, models
app = Flask(__name__)
api = Api(app)


conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='XABC'")

api.add_resource(auth_endpoints.SignUp, '/signup')
api.add_resource(auth_endpoints.Login, '/login')
api.add_resource(auth_endpoints.LogoutAccess, '/logout/access')
api.add_resource(auth_endpoints.LogoutRefresh, '/logout/refresh')
api.add_resource(auth_endpoints.TokenRefresh, '/token/refresh')
api.add_resource(auth_endpoints.AllUsers, '/users')


if __name__ == '__main__':
    app.run(debug=True) 
