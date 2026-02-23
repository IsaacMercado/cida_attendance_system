from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_FACE_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_FACE_DETECTION, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('dwBackgroundPicLen', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struFacePic', NET_VCA_RECT * 30),
    ('byFacePicNum', BYTE),
    ('byUploadEventDataType', BYTE),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 249),
    ('pBackgroundPicpBuffer', POINTER(BYTE)),
])

NET_DVR_FACE_DETECTION = struct_tagNET_DVR_FACE_DETECTION
LPNET_DVR_FACE_DETECTION = POINTER(struct_tagNET_DVR_FACE_DETECTION)
tagNET_DVR_FACE_DETECTION = struct_tagNET_DVR_FACE_DETECTION
