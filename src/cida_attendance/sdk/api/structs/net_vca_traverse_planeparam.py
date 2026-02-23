from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40
from .net_vca_traverse_plane import NET_VCA_TRAVERSE_PLANE


class struct_tagNET_VCA_TRAVERSE_PLANEPARAM(Structure):
    pass

_S(struct_tagNET_VCA_TRAVERSE_PLANEPARAM, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byEnableDualVca', BYTE),
    ('byEnableHumanMisinfoFilter', BYTE),
    ('byEnableVehicleMisinfoFilter', BYTE),
    ('struAlertParam', NET_VCA_TRAVERSE_PLANE * 8),
    ('struAlarmSched', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('dwMaxRelRecordChanNum', DWORD),
    ('dwRelRecordChanNum', DWORD),
    ('byRelRecordChan', DWORD * int((32 + 32))),
    ('struHolidayTime', NET_DVR_SCHEDTIME * 8),
    ('byRes2', BYTE * 100),
])

NET_VCA_TRAVERSE_PLANE_DETECTION = struct_tagNET_VCA_TRAVERSE_PLANEPARAM
LPNET_VCA_TRAVERSE_PLANE_DETECTION = POINTER(struct_tagNET_VCA_TRAVERSE_PLANEPARAM)
tagNET_VCA_TRAVERSE_PLANEPARAM = struct_tagNET_VCA_TRAVERSE_PLANEPARAM
