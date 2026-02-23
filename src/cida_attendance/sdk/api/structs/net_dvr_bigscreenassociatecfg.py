from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BIGSCREENASSOCIATECFG(Structure):
    pass

_S(struct_tagNET_DVR_BIGSCREENASSOCIATECFG, [
    ('dwSize', DWORD),
    ('byEnableBaseMap', BYTE),
    ('byAssociateBaseMap', BYTE),
    ('byEnableSpartan', BYTE),
    ('byRes', BYTE * 21),
])

NET_DVR_BIGSCREENASSOCIATECFG = struct_tagNET_DVR_BIGSCREENASSOCIATECFG
LPNET_DVR_BIGSCREENASSOCIATECFG = POINTER(struct_tagNET_DVR_BIGSCREENASSOCIATECFG)
tagNET_DVR_BIGSCREENASSOCIATECFG = struct_tagNET_DVR_BIGSCREENASSOCIATECFG
