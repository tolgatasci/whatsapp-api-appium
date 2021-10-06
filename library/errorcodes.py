from enum import Enum, unique, auto
@unique
class ErrorCodes(Enum):
    ERR_INCORRECT_ERRCODE = auto()
    ERR_WHATSAPP_INSTALL = auto()
    ERR_INSERT_CHAT  = auto()