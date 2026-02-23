from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_ISAPI_PICDATA(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_ISAPI_PICDATA, [
    ('dwPicLen', DWORD),
    ('byPicType', BYTE),
    ('byRes', BYTE * 3),
    ('szFilename', c_char * 256),
    ('pPicData', POINTER(BYTE)),
])

NET_DVR_ALARM_ISAPI_PICDATA = struct_tagNET_DVR_ALARM_ISAPI_PICDATA
LPNET_DVR_ALARM_ISAPI_PICDATA = POINTER(struct_tagNET_DVR_ALARM_ISAPI_PICDATA)
tagNET_DVR_ALARM_ISAPI_PICDATA = struct_tagNET_DVR_ALARM_ISAPI_PICDATA
