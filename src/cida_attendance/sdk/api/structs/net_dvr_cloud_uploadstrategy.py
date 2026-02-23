from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY(Structure):
    pass

_S(struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY, [
    ('dwSize', DWORD),
    ('byStrategyType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwRecordType', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_CLOUD_UPLOADSTRATEGY = struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY
LPNET_DVR_CLOUD_UPLOADSTRATEGY = POINTER(struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY)
tagNET_DVR_CLOUD_UPLOADSTRATEGY = struct_tagNET_DVR_CLOUD_UPLOADSTRATEGY
