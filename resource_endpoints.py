from flask_restful import Resource, reqparse
from model import RideModel

parser = reqparse.RequestParser()



class Rides(Resource):
    def post(self):
        data = parser.parse_args()
        newride = RideModel (data["ridecreator"], data["destination"], data["departure"], data["fare"], data["d_date"], data["request"])
        try:
            newride.save()
            return {
                'message': 'User {} has created a new ride offer'.format(data['ride'])
            }
        except:
            return {'message': 'Something went wrong'}, 500
