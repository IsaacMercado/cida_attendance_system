from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HANDLEEXCEPTION_V41(Structure):
    pass

_S(struct_tagNET_DVR_HANDLEEXCEPTION_V41, [
    ('dwHandleType', DWORD),
    ('dwMaxRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOut', DWORD * int((4096 + 32))),
    ('byRes', BYTE * 64),
])

NET_DVR_HANDLEEXCEPTION_V41 = struct_tagNET_DVR_HANDLEEXCEPTION_V41
LPNET_DVR_HANDLEEXCEPTION_V41 = POINTER(struct_tagNET_DVR_HANDLEEXCEPTION_V41)
tagNET_DVR_HANDLEEXCEPTION_V41 = struct_tagNET_DVR_HANDLEEXCEPTION_V41
