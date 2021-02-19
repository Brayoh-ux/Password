import unittest
from user import User
from credetials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_cred = Credentials()

    def test_init(self):
        self.assertTrue(self.new_cred.f, )

    def tearDown(self):
        Credentials.f = []

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Brian', '1234')

    def test_init(self):
        self.assertTrue(self.new_user.user_name, 'Brian')
        self.assertTrue(self.new_user.password, '1234')
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        User.user_list = []

if __name__ == '__main__':
    unittest.main()
