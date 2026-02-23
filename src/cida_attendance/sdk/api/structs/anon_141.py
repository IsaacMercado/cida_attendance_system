from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_139 import struct_anon_139
from .anon_140 import struct_anon_140


class struct_anon_141(Structure):
    pass

_S(struct_anon_141, [
    ('dwSize', DWORD),
    ('sAccount', BYTE * 32),
    ('sPassword', BYTE * 32),
    ('struSender', struct_anon_139),
    ('sSmtpServer', BYTE * 48),
    ('sPop3Server', BYTE * 48),
    ('struReceiver', struct_anon_140 * 3),
    ('byAttachment', BYTE),
    ('bySmtpServerVerify', BYTE),
    ('byMailInterval', BYTE),
    ('byEnableSSL', BYTE),
    ('wSmtpPort', WORD),
    ('byEnableTLS', BYTE),
    ('byStartTLS', BYTE),
    ('byRes', BYTE * 72),
])

NET_DVR_EMAILCFG_V30 = struct_anon_141
LPNET_DVR_EMAILCFG_V30 = POINTER(struct_anon_141)
