import requests


class TestTestCase:
    def test_get_right_testcase(self):
        r = requests.get("http://localhost:5000/login", auth=("xxx", "xx"))
        token = r.json().get("access_token")
        r = requests.get("http://localhost:5000/testcase/get", auth=(token, ""))
        assert r.status_code == 200
        assert r.json().get("msg") == "OK"

    def test_get_error_testcase(self):
        token = ""
        r = requests.get("http://localhost:5000/testcase/get", auth=(token, ""))
        assert r.status_code == 401
