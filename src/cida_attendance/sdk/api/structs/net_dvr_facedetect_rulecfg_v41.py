from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .anon_145 import NET_DVR_JPEGPARA
from .net_dvr_face_pipcfg import NET_DVR_FACE_PIPCFG
from .net_vca_polygon import NET_VCA_POLYGON
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_DVR_FACEDETECT_RULECFG_V41(Structure):
    pass

_S(struct_tagNET_DVR_FACEDETECT_RULECFG_V41, [
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
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('byPicRecordEnable', BYTE),
    ('byRes1', BYTE),
    ('wAlarmDelay', WORD),
    ('struFacePIP', NET_DVR_FACE_PIPCFG),
    ('wRelSnapChan', WORD * 3),
    ('byRes2', BYTE * 2),
    ('dwEventTypeEx', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_FACEDETECT_RULECFG_V41 = struct_tagNET_DVR_FACEDETECT_RULECFG_V41
LPNET_DVR_FACEDETECT_RULECFG_V41 = POINTER(struct_tagNET_DVR_FACEDETECT_RULECFG_V41)
tagNET_DVR_FACEDETECT_RULECFG_V41 = struct_tagNET_DVR_FACEDETECT_RULECFG_V41
