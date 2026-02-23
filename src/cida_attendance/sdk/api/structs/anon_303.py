from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_303(Structure):
    pass

_S(struct_anon_303, [
    ('dwSize', DWORD),
    ('dwNum', DWORD),
    ('dwRwSelectPara', DWORD * int((32 + 32))),
    ('dwModeSelect', DWORD),
    ('byRes', BYTE * 24),
    ('dwStartCDRW', DWORD),
    ('dwHdExcp', DWORD),
    ('dwInterval', DWORD),
    ('sLable', c_char * 64),
])

NET_DVR_INQUEST_CDRW_CFG = struct_anon_303
LPNET_DVR_INQUEST_CDRW_CFG = POINTER(struct_anon_303)
