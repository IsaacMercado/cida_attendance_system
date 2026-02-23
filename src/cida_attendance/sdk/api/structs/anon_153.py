from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_153(Structure):
    pass

_S(struct_anon_153, [
    ('sUsername', BYTE * 64),
    ('sPassword', BYTE * 64),
    ('sSmtpServer', BYTE * 64),
    ('sPop3Server', BYTE * 64),
    ('sMailAddr', BYTE * 64),
    ('sEventMailAddr1', BYTE * 64),
    ('sEventMailAddr2', BYTE * 64),
    ('res', BYTE * 16),
])

NET_DVR_EMAILPARA = struct_anon_153
LPNET_DVR_EMAILPARA = POINTER(struct_anon_153)
