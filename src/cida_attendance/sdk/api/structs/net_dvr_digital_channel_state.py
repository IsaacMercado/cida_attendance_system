from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DIGITAL_CHANNEL_STATE(Structure):
    pass

_S(struct_tagNET_DVR_DIGITAL_CHANNEL_STATE, [
    ('dwSize', DWORD),
    ('byDigitalAudioChanTalkState', BYTE * int((32 + 32))),
    ('byDigitalChanState', BYTE * int((32 + 32))),
    ('byDigitalAudioChanTalkStateEx', BYTE * int(((32 + 32) * 3))),
    ('byDigitalChanStateEx', BYTE * int(((32 + 32) * 3))),
    ('byAnalogChanState', BYTE * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_DIGITAL_CHANNEL_STATE = struct_tagNET_DVR_DIGITAL_CHANNEL_STATE
LPNET_DVR_DIGITAL_CHANNEL_STATE = POINTER(struct_tagNET_DVR_DIGITAL_CHANNEL_STATE)
tagNET_DVR_DIGITAL_CHANNEL_STATE = struct_tagNET_DVR_DIGITAL_CHANNEL_STATE
