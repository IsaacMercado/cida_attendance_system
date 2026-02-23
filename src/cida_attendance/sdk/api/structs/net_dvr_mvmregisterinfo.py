from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MVMRegisterInfo_(Structure):
    pass

_S(struct_tagNET_DVR_MVMRegisterInfo_, [
    ('dwSize', DWORD),
    ('sDetectorID', c_char),
    ('sManagerID', c_char),
    ('sSim', c_char * 20),
    ('dwLocalIP', DWORD),
    ('dwLocalIPMask', DWORD),
    ('dwLocalGateway', DWORD),
    ('dwDstIP', DWORD),
    ('byMACAddr', BYTE * 6),
    ('wLocalPort', WORD),
    ('wFirmwareYear', WORD),
    ('byFirmwareMonth', BYTE),
    ('byFirmwareDay', BYTE),
    ('byMajorVersion', BYTE),
    ('byMinorVersion', BYTE),
    ('byRes', BYTE * 170),
])

NET_DVR_MVMRegisterInfo = struct_tagNET_DVR_MVMRegisterInfo_
LPNET_DVR_MVMRegisterInfo = POINTER(struct_tagNET_DVR_MVMRegisterInfo_)
tagNET_DVR_MVMRegisterInfo_ = struct_tagNET_DVR_MVMRegisterInfo_
