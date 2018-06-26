from APP import app
import json

def test_get_byId():
    """test that the API can fetch ride by id"""
    client = app.test_client()
    res = client.get('/api/v1/rides/1')
    data = json.loads(res.data.decode())
    assert res.status_code == 200
    assert isinstance(data, list) == True
    assert len(data) == 2
    
