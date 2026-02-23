from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_tagNET_DVR_VIDEOINTERCOM_STREAM(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOINTERCOM_STREAM, [
    ('dwSize', DWORD),
    ('byVisDevID', BYTE * 16),
    ('byDeviceName', BYTE * 32),
    ('bySourceType', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_VIDEOINTERCOM_STREAM = struct_tagNET_DVR_VIDEOINTERCOM_STREAM
LPNET_DVR_VIDEOINTERCOM_STREAM = struct_tagNET_DVR_VIDEOINTERCOM_STREAM
tagNET_DVR_VIDEOINTERCOM_STREAM = struct_tagNET_DVR_VIDEOINTERCOM_STREAM
