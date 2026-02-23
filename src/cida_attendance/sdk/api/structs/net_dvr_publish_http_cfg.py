from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUBLISH_HTTP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PUBLISH_HTTP_CFG, [
    ('strUrl', BYTE * 256),
])

NET_DVR_PUBLISH_HTTP_CFG = struct_tagNET_DVR_PUBLISH_HTTP_CFG
LPNET_DVR_PUBLISH_HTTP_CFG = POINTER(struct_tagNET_DVR_PUBLISH_HTTP_CFG)
tagNET_DVR_PUBLISH_HTTP_CFG = struct_tagNET_DVR_PUBLISH_HTTP_CFG
