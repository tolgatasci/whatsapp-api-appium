import sys

from library.errorcodes import ErrorCodes
import traceback

class Error(Exception):
    CRED = '\033[91m'
    CEND = '\033[0m'
    def __init__(self, error_code, message='', *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if error_code not in ErrorCodes.__dict__:
            msg = 'INKNOWN'
            raise Error('ERR_INCORRECT_ERRCODE', msg)

        self.error_code = error_code

        self.traceback = sys.exc_info()

        try:
            msg = '\033[91m [{0}] {1} \n {2} \033[0m'.format(error_code, message.format(*args, **kwargs),traceback.format_exc())
        except (IndexError, KeyError):
            msg = '\033[91m [{0}] {1} \033[0m'.format(error_code, message)
        super().__init__(msg)
        print(msg)
        if "exit" in kwargs:
            if kwargs.get('exit'):
                exit(-1)

