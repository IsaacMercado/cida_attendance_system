from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_190 import NET_DVR_DEVICEINFO_V30


class struct_tagNET_DVR_DEVICEINFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_DEVICEINFO_V40, [
    ('struDeviceV30', NET_DVR_DEVICEINFO_V30),
    ('bySupportLock', BYTE),
    ('byRetryLoginTime', BYTE),
    ('byPasswordLevel', BYTE),
    ('byProxyType', BYTE),
    ('dwSurplusLockTime', DWORD),
    ('byCharEncodeType', BYTE),
    ('bySupportDev5', BYTE),
    ('bySupport', BYTE),
    ('byLoginMode', BYTE),
    ('dwOEMCode', DWORD),
    ('iResidualValidity', c_int),
    ('byResidualValidity', BYTE),
    ('bySingleStartDTalkChan', BYTE),
    ('bySingleDTalkChanNums', BYTE),
    ('byPassWordResetLevel', BYTE),
    ('bySupportStreamEncrypt', BYTE),
    ('byMarketType', BYTE),
    ('byRes2', BYTE * 238),
])

NET_DVR_DEVICEINFO_V40 = struct_tagNET_DVR_DEVICEINFO_V40
LPNET_DVR_DEVICEINFO_V40 = POINTER(struct_tagNET_DVR_DEVICEINFO_V40)
tagNET_DVR_DEVICEINFO_V40 = struct_tagNET_DVR_DEVICEINFO_V40
