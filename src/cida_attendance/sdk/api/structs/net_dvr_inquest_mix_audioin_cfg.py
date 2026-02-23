from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_MIX_AUDIOIN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_MIX_AUDIOIN_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwMixCnt', DWORD),
    ('bySrcChan', BYTE * 16),
    ('byLineIn', BYTE * 16),
    ('byMic', BYTE * 16),
    ('byMixAudioDelay', BYTE),
    ('byRes2', BYTE * 127),
])

NET_DVR_INQUEST_MIX_AUDIOIN_CFG = struct_tagNET_DVR_INQUEST_MIX_AUDIOIN_CFG
LPNET_DVR_INQUEST_MIX_AUDIOIN_CFG = POINTER(struct_tagNET_DVR_INQUEST_MIX_AUDIOIN_CFG)
tagNET_DVR_INQUEST_MIX_AUDIOIN_CFG = struct_tagNET_DVR_INQUEST_MIX_AUDIOIN_CFG
