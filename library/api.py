from library.appium import AppiumLib
# TODO: easier to incorporate into other projects
class Api(object):
    driver = None
    def __init__(self, *args, **kwargs):
        self.driver = AppiumLib(auto_start=True, **kwargs)
        pass
    # TODO: open whatsapp app
    def open_whatsapp(self):
        self.driver.open_whatsapp()
        pass
    # TODO: Whatsapp Install Api
    def install_whatsapp(self):
        self.driver.install_whatsapp()
        pass
    def exit_whatsapp(self):
        self.driver.exit_whatsapp()
    # TODO: Add Contact @phone @name
    def add_phone(self):
        self.driver.add_phone(phone="+905319378541")
    def send_message_normal(self,phone = None, message = None):
        self.driver.exit_whatsapp()
        self.driver.send_message_normal(phone=phone,message=message)
        self.driver.open_whatsapp()
    def read_messages(self,read_type = "all",filter=dict()):
        self.driver.exit_whatsapp()
        result = self.driver.read_messages(read_type=read_type,filter=filter)
        self.driver.open_whatsapp()
        return result
