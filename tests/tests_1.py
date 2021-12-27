import sys
sys.path.append('./')

import unittest
from mock import patch
from parameterized import parameterized

from modules.zadanie1 import RandomUser
from tests.resource.test_users import *

class RandomUserTest(unittest.TestCase):

    def test_start_user(self):
        user = RandomUser()
        self.assertEqual(user.user_data, {})
    
    def test_set_new_user(self):
        user = RandomUser()
        user.set_user(user1)
        self.assertEqual(user.user_data, user1)
    
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_and_set_new_user(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        user.set_user(test_user)
        self.assertEqual(user.user_data, test_user)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_return_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user) is dict)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_keys_I(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['results', 'info']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user.keys()), keys)
    
    # results
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_results_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results']) is list)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_results_length(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['seed', 'results', 'page', 'version']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['info'].keys()), keys)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_results_list_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['gender', 'name', 'location', 'email', 'login', 'dob', 'registered', 'phone', 'cell', 'id', 'picture', 'nat']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0].keys()), keys)

    # gender
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_gender_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['gender']) is str)

    # name
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_name_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['title', 'first', 'last']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['name'].keys()), keys)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_name_values_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['name'].values())))
        self.assertTrue(all_types_str)

    # location
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_location_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['street', 'city', 'state', 'country', 'postcode', 'coordinates', 'timezone']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location'].keys()), keys)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_location_values_type_str(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['city', 'state', 'country']
        user = RandomUser()
        test_user = user.get_random_user()
        str_values = list(map(lambda key: test_user['results'][0]['location'][key], keys))
        all_types_str = all(list(map(lambda val: type(val) is str, str_values)))
        self.assertTrue(all_types_str)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_location_values_type_int(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['postcode']
        user = RandomUser()
        test_user = user.get_random_user()
        int_values = list(map(lambda key: test_user['results'][0]['location'][key], keys))
        all_types_int = all(list(map(lambda val: type(val) is int, int_values)))
        self.assertTrue(all_types_int)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_location_values_type_dict(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['street', 'coordinates', 'timezone']
        user = RandomUser()
        test_user = user.get_random_user()
        dict_values = list(map(lambda key: test_user['results'][0]['location'][key], keys))
        all_types_dict = all(list(map(lambda val: type(val) is dict, dict_values)))
        self.assertTrue(all_types_dict)

    # street
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_street_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['number', 'name']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location']['street'].keys()), keys)

    # coordinates
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_coordinates_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['latitude', 'longitude']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location']['coordinates'].keys()), keys)
    
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_coordinates_float_as_str(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        try:
            values = list(map(lambda val: float(val), list(test_user['results'][0]['location']['coordinates'].values())))
        except ValueError:
            return False
        self.assertTrue(all(list(map(lambda val: type(val) is float, values))))

    # timezone
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_coordinates_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['offset', 'description']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location']['timezone'].keys()), keys)

    # email
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_email_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['email']) is str)
    
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_email_at_include(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue('@' in test_user['results'][0]['email'])

    # login
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_login_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['uuid', 'username', 'password', 'salt', 'md5', 'sha1', 'sha256']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['login'].keys()), keys)
    
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_name_values_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['login'].values())))
        self.assertTrue(all_types_str)

    # dob
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_dob_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['date', 'age']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['dob'].keys()), keys)

    # registered
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_registered_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['date', 'age']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['registered'].keys()), keys)

    # phone
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_phone_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['phone']) is str)

    # cell
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_cell_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['cell']) is str)

    # id
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_id_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['name', 'value']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['id'].keys()), keys)
    
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_id_values_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['id'].values())))
        self.assertTrue(all_types_str)

    #picture
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_picture_keys(self, user, get_random_user):
        get_random_user.return_value = user
        keys = ['large', 'medium', 'thumbnail']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['picture'].keys()), keys)
    
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_picure_values_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['picture'].values())))
        self.assertTrue(all_types_str)

    #nat
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_nat_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['nat']) is str)

    # info
    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_info_type(self, user, get_random_user):
        get_random_user.return_value = user
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['info']) is dict)

    @parameterized.expand([
      (user1, ),
      (user2, ),
      (user3, ),
      (user4, ),
    ])
    @patch("modules.zadanie1.RandomUser.get_random_user")
    def test_get_user_info_keys(self, user, get_random_user):
        get_random_user.return_value = user
        info_keys = ['seed', 'results', 'page', 'version']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['info'].keys()), info_keys)

unittest.main()