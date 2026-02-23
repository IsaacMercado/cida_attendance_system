from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY_COND(Structure):
    pass

_S(struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 254),
])

NET_DVR_CLOUD_UPLOADSTRATEGY_COND = struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY_COND
LPNET_DVR_CLOUD_UPLOADSTRATEGY_COND = POINTER(struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY_COND)
tagNET_DVR_CLOUD_UPLOADSTRATEGY_COND = struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY_COND
