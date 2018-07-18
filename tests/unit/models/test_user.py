from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', f'Username does not equal the given value: {user.username}.')
        self.assertEqual(user.password, 'abcd', f'Password does not equal the given value: {user.password}.')
