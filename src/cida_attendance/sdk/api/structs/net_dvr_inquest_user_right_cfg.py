from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_USER_RIGHT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_USER_RIGHT_CFG, [
    ('dwSize', DWORD),
    ('byLocalRight', BYTE * 32),
    ('byRemoteRight', BYTE * 32),
    ('byNetAudioRight', BYTE * 512),
    ('byRes', BYTE * int((512 * 9))),
])

NET_DVR_INQUEST_USER_RIGHT_CFG = struct_tagNET_DVR_INQUEST_USER_RIGHT_CFG
LPNET_DVR_INQUEST_USER_RIGHT_CFG = POINTER(struct_tagNET_DVR_INQUEST_USER_RIGHT_CFG)
tagNET_DVR_INQUEST_USER_RIGHT_CFG = struct_tagNET_DVR_INQUEST_USER_RIGHT_CFG
