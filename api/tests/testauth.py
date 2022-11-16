import requests
import unittest

from .utils import MyTestCase


IP = ""


class TestAuth(MyTestCase):
    ip = "http://"
    register_ip = ""
    logout_ip = ""

    def setUp(self) -> None:
        self.ip += IP if IP != "" else "127.0.0.1:5000"
        self.register_ip = self.ip + "/auth/register"
        self.logout_ip = self.ip + "/auth/logout"

    def test_empty_register(self):
        data = requests.post(self.register_ip)
        self.expectEqual(data.status_code, 400)

    def test_empty_username_register(self):
        data = requests.post(
            self.register_ip, json={"username": "", "password": "Rsapb7494512#"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_username_register_1(self):
        data = requests.post(
            self.register_ip, json={"username": "!??#", "password": "Rsapb7494512#"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_username_register_2(self):
        data = requests.post(
            self.register_ip, json={"username": "jackson!", "password": "Rsapb7494512#"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_username_register_3(self):
        data = requests.post(
            self.register_ip, json={"username": "cu", "password": "Rsapb7494512#"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_empty_password_register(self):
        data = requests.post(
            self.register_ip, json={"username": "joaocolhao", "password": ""})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_password_register_1(self):
        data = requests.post(
            self.register_ip, json={"username": "test", "password": "andresilva"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_password_register_2(self):
        data = requests.post(
            self.register_ip, json={"username": "test", "password": "a1#"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_password_register_3(self):
        data = requests.post(
            self.register_ip, json={"username": "test", "password": "Rsapb7494512"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_creds_1(self):
        data = requests.post(
            self.register_ip, json={"username": "inv#lid", "password": "Rsapb7494512"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_creds_2(self):
        data = requests.post(
            self.register_ip, json={"username": "", "password": ""})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_invalid_creds_3(self):
        data = requests.post(
            self.register_ip, json={"username": "", "password": "#2"})
        self.expectEqual(
            data.json(), {'Error': "Invalid username or password"})
        self.expectEqual(data.status_code, 422)

    def test_valid_registration(self):
        data = requests.post(
            self.register_ip, json={"username": "andre", "password": "Rsapb7494512#"})
        self.expectEqual(data.status_code, 201)

    def test_register_and_logout(self):
        with requests.Session() as s:
            data = s.post(self.register_ip, json={
                          "username": "joao", "password": "Rsapb7494512#"})
            self.expectEqual(data.status_code, 201)
            data2 = s.post(self.logout_ip)
            self.expectEqual(data2.status_code, 204)

    def test_simple_logout(self):
        with requests.Session() as s:
            data = s.post(self.logout_ip)
            self.expectEqual(data.status_code, 401)


if __name__ == "__main__":
    IP = input("Enter IP address: ")
    unittest.main()
