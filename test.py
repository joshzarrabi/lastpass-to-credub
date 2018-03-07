import unittest

import to_credhub

class TestLastpassConversion(unittest.TestCase):
    def test_basic_password(self):
        password_input = {"some-name": "some-value"}
        expected_output = [{"type": "password", "name": "some-name", "value": "some-value"}]
        output = to_credhub.convert_password_to_credhub(password_input)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
