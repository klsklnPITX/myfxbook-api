from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


class MyfxBookApi():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        r = requests.get(
            f"https://www.myfxbook.com/api/login.json?email={email}&password={password}"
        )
        data = json.loads(json.dumps(r.json()))
        self.session = data["session"]

    def logout(self):
        r = requests.get(
            f"https://www.myfxbook.com/api/logout.json?session={self.session}"
        )
        data = json.loads(json.dumps(r.json()))
        print(data["message"])

    def get_my_accounts(self):
        r = requests.get(
            f"https://www.myfxbook.com/api/get-my-accounts.json?session={self.session}"
        )
        data = json.loads(json.dumps(r.json()))
        print(data)


a = MyfxBookApi(EMAIL, PASSWORD)
a.get_my_accounts()
