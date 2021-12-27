import sys
sys.path.append('./')

import unittest

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
    
    def test_get_and_set_new_user(self):
        user = RandomUser()
        test_user = user.get_random_user()
        user.set_user(test_user)
        self.assertEqual(user.user_data, test_user)

    def test_get_user_return_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user) is dict)

    def test_get_user_keys_I(self):
        keys = ['results', 'info']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user.keys()), keys)
    
    # results
    def test_get_user_results_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results']) is list)

    def test_get_user_results_length(self):
        keys = ['seed', 'results', 'page', 'version']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['info'].keys()), keys)

    def test_get_user_results_list_keys(self):
        keys = ['gender', 'name', 'location', 'email', 'login', 'dob', 'registered', 'phone', 'cell', 'id', 'picture', 'nat']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0].keys()), keys)

    # gender
    def test_get_user_gender_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['gender']) is str)

    # name
    def test_get_user_name_keys(self):
        keys = ['title', 'first', 'last']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['name'].keys()), keys)

    def test_get_user_name_values_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['name'].values())))
        self.assertTrue(all_types_str)

    # location
    def test_get_user_location_keys(self):
        keys = ['street', 'city', 'state', 'country', 'postcode', 'coordinates', 'timezone']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location'].keys()), keys)

    def test_get_user_location_values_type_str(self):
        keys = ['city', 'state', 'country']
        user = RandomUser()
        test_user = user.get_random_user()
        str_values = list(map(lambda key: test_user['results'][0]['location'][key], keys))
        all_types_str = all(list(map(lambda val: type(val) is str, str_values)))
        self.assertTrue(all_types_str)

    def test_get_user_location_values_type_int(self):
        keys = ['postcode']
        user = RandomUser()
        test_user = user.get_random_user()
        int_values = list(map(lambda key: test_user['results'][0]['location'][key], keys))
        all_types_int = all(list(map(lambda val: type(val) is int, int_values)))
        self.assertTrue(all_types_int)

    def test_get_user_location_values_type_dict(self):
        keys = ['street', 'coordinates', 'timezone']
        user = RandomUser()
        test_user = user.get_random_user()
        dict_values = list(map(lambda key: test_user['results'][0]['location'][key], keys))
        all_types_dict = all(list(map(lambda val: type(val) is dict, dict_values)))
        self.assertTrue(all_types_dict)

    # street
    def test_get_user_street_keys(self):
        keys = ['number', 'name']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location']['street'].keys()), keys)

    # coordinates
    def test_get_user_coordinates_keys(self):
        keys = ['latitude', 'longitude']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location']['coordinates'].keys()), keys)
    
    def test_get_user_coordinates_float_as_str(self):
        user = RandomUser()
        test_user = user.get_random_user()
        try:
            values = list(map(lambda val: float(val), list(test_user['results'][0]['location']['coordinates'].values())))
        except ValueError:
            return False
        self.assertTrue(all(list(map(lambda val: type(val) is float, values))))

    # timezone
    def test_get_user_coordinates_keys(self):
        keys = ['offset', 'description']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['location']['timezone'].keys()), keys)

    # email
    def test_get_user_email_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['email']) is str)
    
    def test_get_user_email_at_include(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue('@' in test_user['results'][0]['email'])

    # login
    def test_get_user_login_keys(self):
        keys = ['uuid', 'username', 'password', 'salt', 'md5', 'sha1', 'sha256']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['login'].keys()), keys)
    
    def test_get_user_name_values_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['login'].values())))
        self.assertTrue(all_types_str)

    # dob
    def test_get_user_dob_keys(self):
        keys = ['date', 'age']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['dob'].keys()), keys)

    # registered
    def test_get_user_registered_keys(self):
        keys = ['date', 'age']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['registered'].keys()), keys)

    # phone
    def test_get_user_phone_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['phone']) is str)

    # cell
    def test_get_user_cell_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['cell']) is str)

    # id
    def test_get_user_id_keys(self):
        keys = ['name', 'value']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['id'].keys()), keys)
    
    def test_get_user_id_values_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['id'].values())))
        self.assertTrue(all_types_str)

    #picture
    def test_get_user_picture_keys(self):
        keys = ['large', 'medium', 'thumbnail']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['results'][0]['picture'].keys()), keys)
    
    def test_get_user_picure_values_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        all_types_str = all(list(map(lambda val: type(val) is str, test_user['results'][0]['picture'].values())))
        self.assertTrue(all_types_str)

    #nat
    def test_get_user_nat_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['results'][0]['nat']) is str)

    # info
    def test_get_user_info_type(self):
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertTrue(type(test_user['info']) is dict)

    def test_get_user_info_keys(self):
        info_keys = ['seed', 'results', 'page', 'version']
        user = RandomUser()
        test_user = user.get_random_user()
        self.assertEqual(list(test_user['info'].keys()), info_keys)

unittest.main()