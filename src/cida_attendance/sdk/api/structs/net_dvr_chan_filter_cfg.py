from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_27 import NET_DVR_RGB_COLOR
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40
from .net_dvr_pos_osd_region import NET_DVR_POS_OSD_REGION


class struct_tagNET_DVR_CHAN_FILTER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CHAN_FILTER_CFG, [
    ('dwSize', DWORD),
    ('byFilterID', BYTE),
    ('byFontSize', BYTE),
    ('byShowPosInfo', BYTE),
    ('byOverlayMode', BYTE),
    ('dwDelayTime', DWORD),
    ('struOsdPosInfo', NET_DVR_POS_OSD_REGION),
    ('struOsdColor', NET_DVR_RGB_COLOR),
    ('struAlarmSched', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('dwMaxRelRecordChanNum', DWORD),
    ('dwRelRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * int((32 + 32))),
    ('dwTimeOut', DWORD),
    ('byRes', BYTE * 60),
])

NET_DVR_CHAN_FILTER_CFG = struct_tagNET_DVR_CHAN_FILTER_CFG
LPNET_DVR_CHAN_FILTER_CFG = POINTER(struct_tagNET_DVR_CHAN_FILTER_CFG)
tagNET_DVR_CHAN_FILTER_CFG = struct_tagNET_DVR_CHAN_FILTER_CFG
