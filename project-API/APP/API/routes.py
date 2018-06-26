def ride_resource():
    """implement ride resource as a list of dictionary"""
    rides = [{"id":1, "destination":"Nairobi", "departure_point":"Eldoret", "fare":800, "driver":{"username":"Jesse", "gender":"male"}, "requests":[{"username":"jane","state":"accepted"},{"username":"jack","state":"accepted"},{"username":"frank", "state":"accepted"}],
 "passengers":{"usernames":["jane", "jack", "frank"],"number":3}, "stop_over":["Nakuru","Limuru"]}, {"id":2, "destination":"Mombasa", "departure_point":"Nairobi", "fare":1200, "driver":{"username":"Milac", "gender":"female"},
"passengers":{"usernames":["jeff", "steve"],"number":2}, "stop_over":["Mtito Andei"], "requests":[{"username":"jeff","state":"accepted"},{"username":"steve","state":"accepted"}]}] 
    return rides



@Bluep.route('/rides', methods=['GET'])
def get_rides():
    """get all ride"""
    return make_response(jsonify(ride_resource()))

@Bluep.route('/rides/<int:id>', methods=['GET'])
def get_ride_by_id(id):
    """access ride by id"""
    if isinstance(id, int):
        for ride in ride_resource():
            if ride["id"] == id:
                return make_response(jsonify(ride))
        else:
           return make_response(jsonify({"message":"resource must have id 1 2 or one you just created"}))
    else:
        return make_response(jsonify("{message":"id must be an integer"}))
    

@Bluep.route('/rides/<int:id>', methods=['POST'])
def post_ride_request(id):
    """update ride by id""" 
    if isinstance(id, int):
        for ride in ride_resource():
            if ride["id"] == id:
                data = request.get_json()
                ride["requests"].append(data)
                return make_response(jsonify(ride), 201)
        else:
            return make_response(jsonify({"message":"resource must have id 1 2 or one you just created"}))
    else:
        return make_response(jsonify({"message":"id must be an int"}))


@Bluep.route('/rides', methods=['POST'])
def create_ride():
    """create ride"""
    data = request.get_json()
    if isinstance(data["id"], int) and isinstance(data["departure"], string):
        for ride in ride_resource():
            if ride["id"] == id:
                return make_response(jsonify({"message":"ride id must be unique"}))
        else:
            dt = ride_resource().append(data)
            return make_response(jsonify(dt), 201)
    
