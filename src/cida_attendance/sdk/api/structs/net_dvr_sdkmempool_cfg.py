from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SDKMEMPOOL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SDKMEMPOOL_CFG, [
    ('byRes', BYTE * 256),
])

NET_DVR_SDKMEMPOOL_CFG = struct_tagNET_DVR_SDKMEMPOOL_CFG
LPNET_DVR_SDKMEMPOOL_CFG = POINTER(struct_tagNET_DVR_SDKMEMPOOL_CFG)
tagNET_DVR_SDKMEMPOOL_CFG = struct_tagNET_DVR_SDKMEMPOOL_CFG
