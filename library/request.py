import requests

from helper.helper import Helper
from library.errorcodes import ErrorCodes
from library.error import Error


class Request(object):

    def post(self, url=None, data=None, headers={}, json=None, save_cookie=None):
        try:
            cookie = None
            if save_cookie:
                if save_cookie["load"]:
                    cookie = Helper.load_cookies(save_cookie["filename"])
            if json:
                req = requests.post(url=url, json=json, headers=headers, timeout=5, cookies=cookie)
            else:
                req = requests.post(url=url, data=data, headers=headers, timeout=5, cookies=cookie)
            if save_cookie:
                if save_cookie["save"]:
                    Helper().save_cookies(req.cookies, save_cookie["filename"])
            return req
        except Exception as e:
            raise Error(error_code=ErrorCodes.REQUEST_POST, message="Request POST FAILED\n" + str(e))

    def get(self, url=None, query=[], headers={}):
        try:
            return requests.get(url=url, params=query, headers=headers, timeout=5)
        except Exception as e:
            raise Error(error_code=ErrorCodes.REQUEST_POST, message="Request GET FAILED \n" + str(e))
