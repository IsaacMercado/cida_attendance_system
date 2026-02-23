from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS_(Structure):
    pass

_S(struct_tagNET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS_, [
    ('dwSize', DWORD),
    ('byDigitalChanPasswordStatus', BYTE * int(((32 + 32) * 4))),
    ('byRes', BYTE * 1140),
])

NET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS = struct_tagNET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS_
LPNET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS = POINTER(struct_tagNET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS_)
tagNET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS_ = struct_tagNET_DVR_DIGITAL_CHANNEL_SECURITY_STATUS_
