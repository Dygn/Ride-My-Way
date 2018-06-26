from APP import app
import json

def test_create_ride():
    """test that requests ride"""
    client = app.test_client()
    dt={"username":"dickens", "state":"requesting"}
    response = client.put('/api/v1/rides/1', data = json.dumps(dt) , content_type = 'application/json' )
    result = json.loads(response.data.decode())
    assert response.status_code == 201
    

