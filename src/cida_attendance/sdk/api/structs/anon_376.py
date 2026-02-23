from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_373 import NET_DVR_FTP_SERVER_TEST_PARA


class struct_anon_376(Structure):
    pass

_S(struct_anon_376, [
    ('struFtpPara', NET_DVR_FTP_SERVER_TEST_PARA),
    ('byRes1', BYTE * 212),
])

