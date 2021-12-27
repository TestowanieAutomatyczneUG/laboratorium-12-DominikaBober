import sys
sys.path.append('./')

import pandas as pd
import unittest
from mock import patch
from parameterized import parameterized

from modules.zadanie3 import Messenger

class RandomUserTest(unittest.TestCase):

    @parameterized.expand([
      ("12eus34", "89adh", "Are you lost babygirl?", 200),
      ("12eus34", "12eus34", "Why I am talking to myself", 200),
      ("12eus34", "39add", "Byłeś na otwarciu?", 200),
      ("12eus34", "39add", "parasola", 200),
    ])
    @patch("modules.zadanie3.TemplateEngine.send")
    def test_send_message(self, user, receiver, message, status, send):
        send.return_value = status
        seder = {"id": user}
        messenger = Messenger(seder)
        self.assertEqual(messenger.send_message(receiver, message), 200)
    
    @parameterized.expand([
      ("12eus34", [{"time": pd.to_datetime("2021-04-30 21:04:00"), "sender": "12eus34", "message": "Why I am talking to myself"}], ),
      ("39add", [{"time": pd.to_datetime("2021-01-30 09:03:05"), "sender": "12eus34", "message": "Byłeś na otwarciu?"},
                {"time": pd.to_datetime("2021-01-30 09:04:00"), "sender": "12eus34", "message": "parasola"}], ),
      ("89adh", [{"time": pd.to_datetime("2020-01-30 06:04:00"), "sender": "12eus34", "message": "Are you lost babygirl?"},
                {"time": pd.to_datetime("2021-08-30 19:44:00"), "sender": "39add", "message": "..... klaśnij"}], ),
      ("47wj3l", [], ),
    ])
    @patch("modules.zadanie3.TemplateEngine.receive")
    def test_receive_message(self, user, messages, receive):
        receive.return_value = messages
        seder = {"id": user}
        messenger = Messenger(seder)
        self.assertEqual(messenger.receive_message(), messages)

unittest.main()