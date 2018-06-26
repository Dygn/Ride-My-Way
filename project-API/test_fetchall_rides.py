from APP import app
import json

def test_get_all_rides():
    """test that the API can fetch all rides available"""
    client = app.test_client()
    res = client.get('/api/v1/rides')
    data = json.loads(res.data.decode())
    assert res.status_code == 200
    #assert data['status'] == 'success'
    assert isinstance(data, list) == True
    assert len(data) == 2
   
