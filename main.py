from helper.helper import Helper
from library.api import Api
from library.session import Session
from helper.config import Config

if __name__ == '__main__':
    ses = Session()
    config = Config()
    helper = Helper()
    api = Api(config=config, helper=helper)
    #api.send_message_normal(phone="+905319378541", message="whats")
    #api.install_whatsapp()
    print(api.read_messages(read_type="news"))
