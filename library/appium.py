import time

from appium import webdriver

from library.error import Error


class AppiumLib(object):
    # TODO: caps appium config

    # TODO: Appium Driver
    driver = None
    # TODO : Appium server url
    driver_url = "http://localhost:4723/wd/hub"

    def __init__(self, driver_url=None, caps=None, auto_start=False, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        # TODO: if change default config set ( caps, driver_url )
        if caps:
            self.config.CAPS = caps
        if driver_url:
            self.driver_url = driver_url
        # TODO: If auto_start run
        if auto_start:
            self.driver = webdriver.Remote(self.driver_url, self.config.CAPS)

    # TODO: open whatsapp app
    def open_whatsapp(self):
        self.driver.start_activity(self.config.WHATSAPP_APP_NAME, self.config.WHATSAPP_APP_HOME_ACTIVITY)

    # TODO: Whatsapp Install AppiumLib if have  error install arm try x32_x64 install
    def install_whatsapp(self):
        try:
            self.driver.install_app(self.config.WHATSAPP_APP_FILE_URL)
        except:
            Error(error_code='ERR_WHATSAPP_INSTALL', message='Whatsapp ARM install failed! Trying x32_64 now...')
            # TODO: x32_x64
            try:
                self.driver.install_app(self.config.WHATSAPP_APP_FILE_URL_32_64)
                print("Installed Successfull whatsapp")
            except:
                Error(error_code='ERR_WHATSAPP_INSTALL', message='Whatsapp install failed!', exit=True)
        # Todo: Kill whatsapp

    def adb_shell(self, command, args=[]):
        return self.driver.execute_script('mobile: shell', {
            'command': command,
            'args': args,
            'includeStderr': True,
            'timeout': 5000
        })

    def get_key_id_to_and_from(self):
        key_id_from = int(round(time.time() * 1000))
        key_id_to = int(key_id_from / 1000)
        return key_id_from, key_id_to

    def insert_chat(self, remote_jid):
        query_sql = self.config.INSERT_CHAT_OKEY.format(
            remote_jid=remote_jid
        )
        self.adb_shell("su root  sqlite3 {} \"{}\"".format(self.config.DATABASE_PATH, query_sql))

    def send_message_normal(self, phone, message):
        key_id_from, key_id_to = self.get_key_id_to_and_from()
        self.add_phone(phone)
        phone = self.helper.convert_phone(phone=phone)
        remote_jid = phone['remote_jid']
        sql_query = self.config.INSERT_INTO_MESSAGES_QUERY.format(
            remote_jid=remote_jid,
            messages_table_name=self.config.MESSAGES_TABLE_NAME,
            key_id_from=key_id_from,
            key_id_to=key_id_to,
            k_constant=self.config.K_CONSTANT,
            message=message,
        )
        try:
            self.insert_chat(remote_jid)
        except:
            pass

        self.adb_shell("su root  sqlite3 {} \"{}\"".format(self.config.DATABASE_PATH, sql_query))

    def read_messages(self, read_type="all"):
        if read_type == "news":
            reader = self.adb_shell("su root  sqlite3 {} \"{}\"".format(self.config.DATABASE_PATH, self.config.GET_MESSAGES_YENI))
            reader = self.helper.convert_message(reader["stdout"], self.config.MESSAGES_ROW_NEWS_REGEX)
        else:
            reader = self.adb_shell("su root  sqlite3 {} \"{}\"".format(self.config.DATABASE_PATH, self.config.GET_MESSAGES))
            reader = self.helper.convert_message(reader["stdout"], self.config.MESSAGES_ROW_REGEX)

        return reader

    def add_phone(self, phone=None):
        sql_query = self.config.INSERT_JID.format(
            clean_phone=phone.replace('+', ''),
            no_clean_phone=phone.replace('+', '') + '@s.whatsapp.net'
        )

        # self.adb_shell("su root  sqlite3 {} \"{}\"".format(self.config.DATABASE_PATH,"delete from jid"))
        self.adb_shell("su root  sqlite3 {} \"{}\"".format(self.config.DATABASE_PATH, sql_query))

    def exit_whatsapp(self):
        return self.adb_shell(command="su root pkill {}".format(self.config.WHATSAPP_APP_NAME))
    # TODO: New APK Helper NEED
