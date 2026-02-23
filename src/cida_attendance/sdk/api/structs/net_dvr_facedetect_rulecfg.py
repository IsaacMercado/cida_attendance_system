from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .anon_145 import NET_DVR_JPEGPARA
from .net_vca_polygon import NET_VCA_POLYGON
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_DVR_FACEDETECT_RULECFG(Structure):
    pass

_S(struct_tagNET_DVR_FACEDETECT_RULECFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byEventType', BYTE),
    ('byUpLastAlarm', BYTE),
    ('byUpFacePic', BYTE),
    ('byRuleName', BYTE * 32),
    ('struVcaPolygon', NET_VCA_POLYGON),
    ('byPicProType', BYTE),
    ('bySensitivity', BYTE),
    ('wDuration', WORD),
    ('struPictureParam', NET_DVR_JPEGPARA),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 2) * 7),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('byPicRecordEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwEventTypeEx', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_FACEDETECT_RULECFG = struct_tagNET_DVR_FACEDETECT_RULECFG
LPNET_DVR_FACEDETECT_RULECFG = POINTER(struct_tagNET_DVR_FACEDETECT_RULECFG)
tagNET_DVR_FACEDETECT_RULECFG = struct_tagNET_DVR_FACEDETECT_RULECFG
