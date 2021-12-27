import sys
sys.path.append('./')

import pandas as pd
import unittest
from mock import patch
from parameterized import parameterized

from modules.zadanie2 import Subscriber

class RandomUserTest(unittest.TestCase):

    @parameterized.expand([
      ([{"id": "akdj"}, {"id": "akla3"}, {"id": "adkl3"}], ),
      ([{"id": "akdj"}], ),
      ([], ),
    ])
    def test_client_list(self, client_list):
        subscriber = Subscriber(client_list)
        self.assertEqual(subscriber.client_list, client_list)

    @parameterized.expand([
      ([{"id": "akdj"}, {"id": "akla3"}, {"id": "adkl3"}], [{"id": "akdj"}, {"id": "akla3"}, {"id": "adkl3"}], ),
      ([{"id": "akdj"}], [{"id": "akdj"}, {"id": "adkl3"}], ),
      ([], [{"id": "adkl3"}], ),
    ])
    def test_add_client(self, start_client_list, end_client_list):
        subscriber = Subscriber(start_client_list)
        subscriber.add_client({"id": "adkl3"})
        self.assertEqual(subscriber.client_list, end_client_list)

    @parameterized.expand([
      ([{"id": "akdj"}, {"id": "akla3"}, {"id": "adkl3"}], "adkl3", [{"id": "akdj"}, {"id": "akla3"}], ),
      ([{"id": "akdj"}], "akdj", [], ),
      ([], "fake_id", [], ),
    ])
    def test_del_client(self, start_client_list, id_for_del, end_client_list):
        subscriber = Subscriber(start_client_list)
        subscriber.del_client(id_for_del)
        self.assertEqual(subscriber.client_list, end_client_list)
    
    @parameterized.expand([
      ([{"id": "akdj"}, {"id": "akla3"}, {"id": "adkl3"}], "adkl3", "Hello babygirl", 200, ),
      ([{"id": "akdj"}], "akdj", "How you doin", 200, ),
      ([], "fake_id", "fake message", 500, ),
    ])
    @patch("modules.zadanie2.Subscriber.send_nessage_to_client")
    def test_del_client(self, start_client_list, receiver_id, message, status, send_nessage_to_client):
        send_nessage_to_client.return_value = status
        subscriber = Subscriber(start_client_list)
        response = subscriber.send_nessage_to_client(receiver_id, message)
        self.assertEqual(response, status)

unittest.main()