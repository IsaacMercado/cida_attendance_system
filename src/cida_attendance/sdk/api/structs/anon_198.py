from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, LONG, WORD
from ..ctypes_preamble import POINTER


class struct_anon_198(Structure):
    pass

_S(struct_anon_198, [
    ('byUserIDValid', BYTE),
    ('bySerialValid', BYTE),
    ('byVersionValid', BYTE),
    ('byDeviceNameValid', BYTE),
    ('byMacAddrValid', BYTE),
    ('byLinkPortValid', BYTE),
    ('byDeviceIPValid', BYTE),
    ('bySocketIPValid', BYTE),
    ('lUserID', LONG),
    ('sSerialNumber', BYTE * 48),
    ('dwDeviceVersion', DWORD),
    ('sDeviceName', c_char * 32),
    ('byMacAddr', BYTE * 6),
    ('wLinkPort', WORD),
    ('sDeviceIP', c_char * 128),
    ('sSocketIP', c_char * 128),
    ('byIpProtocol', BYTE),
    ('byRes1', BYTE * 2),
    ('bJSONBroken', BYTE),
    ('wSocketPort', WORD),
    ('byRes2', BYTE * 6),
])

NET_DVR_ALARMER = struct_anon_198
LPNET_DVR_ALARMER = POINTER(struct_anon_198)
