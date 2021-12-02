import io
import random
import ast
import re

class Helper(object):
    def convert_message(self, output,regex_):
        data = []
        sp_out = output.split("\r\n")

        for sp in sp_out:
            data.append(re.findall(regex_, sp.encode()))
        data = [x for x in data if x]
        return data

    def uuid(self):
        import uuid
        value = uuid.uuid4()
        del uuid
        return value

    def convert_phone(self, phone=None):
        if phone:
            return {"normal": phone, "clean": phone.replace("+", ""),
                    "remote_jid": phone.replace("+", "") + '@s.whatsapp.net'}
        else:
            return None

    def build_string(self, lenght=16):
        import string

        allchar = string.ascii_letters + string.digits
        return "".join(random.choice(allchar) for x in range(random.randint(16, 16))).lower()

    def open_file(self, file):
        f = io.open(file, mode="r", encoding="utf-8")
        oku = f.read()
        f.close()
        return oku

    def build_mac(self):
        return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                                            random.randint(0, 255),
                                            random.randint(0, 255))

    def build_phone(self):
        f = io.open("data/devices.txt", mode="r", encoding="utf-8")
        oku = f.read()
        devices = ast.literal_eval(oku)
        f.close()

        return random.choice(devices)

    def connection_type(self):
        data = [
            ["312", "530", "Sprint Spectrum"],
            ["310", "120", "Sprint Spectrum"],
            ["316", "010", "Sprint Spectrum"],
            ["312", "190", "Sprint Spectrum"],
            ["311", "880", "Sprint Spectrum"],
            ["311", "870", "Sprint Spectrum"],
            ["311", "490", "Sprint Spectrum"],
            ["310", "160", "T-Mobile"],
            ["310", "240", "T-Mobile"],
            ["310", "660", "T-Mobile"],
            ["310", "230", "T-Mobile"],
            ["310", "31", "T-Mobile"],
            ["310", "220", "T-Mobile"],
            ["310", "270", "T-Mobile"],
            ["310", "210", "T-Mobile"],
            ["310", "260", "T-Mobile"],
            ["310", "200", "T-Mobile"],
            ["310", "250", "T-Mobile"],
            ["310", "300", "T-Mobile"],
            ["310", "280", "T-Mobile"],
            ["310", "330", "T-Mobile"],
            ["310", "800", "T-Mobile"],
            ["310", "310", "T-Mobile"],
            ["310", "012", "Verizon Wireless"],
            ["311", "280", "Verizon Wireless"],
            ["311", "485", "Verizon Wireless"],
            ["311", "110", "Verizon Wireless"],
            ["311", "285", "Verizon Wireless"],
            ["311", "274", "Verizon Wireless"],
            ["311", "390", "Verizon Wireless"],
            ["310", "010", "Verizon Wireless"],
            ["311", "279", "Verizon Wireless"],
            ["311", "484", "Verizon Wireless"],
            ["310", "910", "Verizon Wireless"],
            ["311", "284", "Verizon Wireless"],
            ["311", "489", "Verizon Wireless"],
            ["311", "273", "Verizon Wireless"],
            ["311", "289", "Verizon Wireless"],
            ["310", "004", "Verizon Wireless"],
            ["311", "278", "Verizon Wireless"],
            ["311", "483", "Verizon Wireless"],
            ["310", "890", "Verizon Wireless"],
            ["311", "283", "Verizon Wireless"],
            ["311", "488", "Verizon Wireless"],
            ["311", "272", "Verizon Wireless"],
            ["311", "288", "Verizon Wireless"],
            ["311", "277", "Verizon Wireless"],
            ["311", "482", "Verizon Wireless"],
            ["310", "590", "Verizon Wireless"],
            ["311", "282", "Verizon Wireless"],
            ["311", "487", "Verizon Wireless"],
            ["311", "271", "Verizon Wireless"],
            ["311", "287", "Verizon Wireless"],
            ["311", "276", "Verizon Wireless"],
            ["311", "481", "Verizon Wireless"],
            ["310", "013", "Verizon Wireless"],
            ["311", "281", "Verizon Wireless"],
            ["311", "486", "Verizon Wireless"],
            ["311", "270", "Verizon Wireless"],
            ["311", "286", "Verizon Wireless"],
            ["311", "275", "Verizon Wireless"],
            ["311", "480", "Verizon Wireless"],
            ["310", "560", "AT&T Wireless Inc."],
            ["310", "410", "AT&T Wireless Inc."],
            ["310", "380", "AT&T Wireless Inc."],
            ["310", "170", "AT&T Wireless Inc."],
            ["310", "150", "AT&T Wireless Inc."],
            ["310", "680", "AT&T Wireless Inc."],
            ["310", "070", "AT&T Wireless Inc."],
            ["310", "980", "AT&T Wireless Inc."]
        ]
        return random.choice(data)
