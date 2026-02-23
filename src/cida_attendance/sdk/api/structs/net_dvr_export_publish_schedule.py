from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from ..functions import DOWNLOAD_DATA_CB


class struct_tagNET_DVR_EXPORT_PUBLISH_SCHEDULE(Structure):
    pass

_S(struct_tagNET_DVR_EXPORT_PUBLISH_SCHEDULE, [
    ('dwScheduleID', DWORD),
    ('fnDownloadFileCallBack', DOWNLOAD_DATA_CB),
    ('pUser', POINTER(None)),
    ('byRes', BYTE * 32),
])

NET_DVR_EXPORT_PUBLISH_SCHEDULE = struct_tagNET_DVR_EXPORT_PUBLISH_SCHEDULE
LPNET_DVR_EXPORT_PUBLISH_SCHEDULE = POINTER(struct_tagNET_DVR_EXPORT_PUBLISH_SCHEDULE)
tagNET_DVR_EXPORT_PUBLISH_SCHEDULE = struct_tagNET_DVR_EXPORT_PUBLISH_SCHEDULE
