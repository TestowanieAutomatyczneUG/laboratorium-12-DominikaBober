
class Subscriber:

    def __init__(self, client_list):
        self.client_list = client_list
    
    def add_client(self, new_client):
        updated_client_list = self.client_list.copy()
        if new_client['id'] not in list(map(lambda client: client['id'] , updated_client_list)):
            updated_client_list.append(new_client)
            self.client_list = updated_client_list
    
    def del_client(self, del_client_id):
        updated_client_list = self.client_list.copy()
        updated_client_list = list(filter(lambda client: client['id'] != del_client_id, updated_client_list))
        self.client_list = updated_client_list
    
    def send_nessage_to_client(self, id, message):
        pass
