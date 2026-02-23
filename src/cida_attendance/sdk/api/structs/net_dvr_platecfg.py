from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_8 import NET_DVR_HANDLEEXCEPTION
from .anon_145 import NET_DVR_JPEGPARA
from .net_dvr_plate_param import NET_DVR_PALTE_PARAM


class struct_tagNET_DVR_PLATECFG(Structure):
    pass

_S(struct_tagNET_DVR_PLATECFG, [
    ('dwSize', DWORD),
    ('dwEnable', DWORD),
    ('byPicProType', BYTE),
    ('byRes1', BYTE * 3),
    ('struPictureParam', NET_DVR_JPEGPARA),
    ('struPlateParam', NET_DVR_PALTE_PARAM),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 4) * 7),
    ('byRelRecordChan', BYTE * 16),
    ('byRes', BYTE * 20),
])

NET_DVR_PLATECFG = struct_tagNET_DVR_PLATECFG
LPNET_DVR_PLATECFG = POINTER(struct_tagNET_DVR_PLATECFG)
tagNET_DVR_PLATECFG = struct_tagNET_DVR_PLATECFG
