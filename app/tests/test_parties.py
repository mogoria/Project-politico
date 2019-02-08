from . import BaseTest
import json


class BasePartiesTest(BaseTest):
    path = "/api/v1/parties"

    party_data = {
            "name":"new party",
            "id":254,
            "logoUrl":"https://photos/254",
            "hqAddress": "Nairobi"
        }
    party_data2 = {
            "name":"new party2",
            "id":257,
            "logoUrl":"https://photos/257",
            "hqAddress": "Somewhere"
        }
    def patch(self, party_id, data):
        path = "{}/{}/name".format(self.path, party_id)
        return self.client.patch(path, data=json.dumps(data), content_type="application/json")
    
class TestPartiesStatusCodes(BasePartiesTest):

    def test_create_party(self):
        self.assertEqual(self.post(self.party_data).status_code, 201)

    def test_get_single_party(self):        
        response = self.get_single(254)
        self.assertEqual(response.status_code, 200)

    def test_delete_party(self):
        new_party = self.post(self.party_data2)
        party_id = new_party.json['data'][0]["id"]
        response = self.delete(party_id)
        self.assertEqual(response.status_code, 200)

    def test_edit_party_name(self):
        new_party = self.post(self.party_data2)
        party_id = new_party.json['data'][0]["id"]
        response = self.patch(party_id,self.party_data2)
        self.assertEqual(response.status_code, 200)

    def test_get_all_parties(self):
        response = self.get()
        self.assertEqual(response.status_code, 200)

