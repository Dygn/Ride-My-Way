from APP import app
import json

def test_create_ride():
    """test that the API can fetch all rides available"""
    client = app.test_client()
    dt={"id": 6, "destination":"san francisco", "departure_point":"miami", "fare":1000, "driver":{"username":"amos"}}
    response = client.post('/api/v1/rides', data = json.dumps(dt) , content_type = 'application/json' )
    result = json.loads(response.data.decode())
    assert response.status_code == 201
    assert 'destination' in response.get_data(as_text=True)
    assert result['status'] == 'ok'
    assert result['destination'] =='san francisco'
    
