from cgi import parse_multipart
import requests
import inspect


class EmailClient(object):

    base_url = f"https://api.listrak.com/email/v1/"

    def __init__(self, token: str, **path):
        self.token = token

    @property
    def lists(self):
        from listrak.service import lists

        return lists.Lists(self)

    @property
    def contacts(self):
        from listrak.service import contacts

        return contacts.Contacts(self)

    def request(self, method, path, **params):
        method = method.upper()
        request_kwargs = {}

        if method == "GET":
            request_kwargs["params"] = params
        elif method == "POST":
            request_kwargs["data"] = params
        elif method == "DELETE" or method == "PUT":
            request_kwargs["json"] = params
        else:
            raise Exception

        response = requests.request(
            method,
            f"{self.base_url + path}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}",
            },
            **request_kwargs,
        )

        print(f"{self.base_url + path}")
        print(response)
        return response

    def get(self, path, **params):
        return self.request("GET", path, **params)
