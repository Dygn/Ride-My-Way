from APP import app
import json

def test_create_ride():
    """test that requests ride"""
    client = app.test_client()
    dt={"username":"dickens", "state":"requesting"}
    response = client.put('/api/v1/rides/1', data = json.dumps(dt) , content_type = 'application/json' )
    result = json.loads(response.data)
    assert response.status_code == 201
    #assertTrue(res.content_type == 'application/json')
    #self.assertTrue(data['status'] == 'success')
    #self.assertTrue(data['name'] == 'Adventure')
    #self.assertEqual(data['id'], 1)

