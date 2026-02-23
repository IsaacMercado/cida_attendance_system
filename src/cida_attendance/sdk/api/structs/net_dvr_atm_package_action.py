from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_116 import NET_DVR_FRAMETYPECODE
from .net_dvr_osd_position import NET_DVR_OSD_POSITION
from .net_dvr_package_location import NET_DVR_PACKAGE_LOCATION


class struct_tagNET_DVR_ATM_PACKAGE_ACTION(Structure):
    pass

_S(struct_tagNET_DVR_ATM_PACKAGE_ACTION, [
    ('struPackageLocation', NET_DVR_PACKAGE_LOCATION),
    ('struOsdPosition', NET_DVR_OSD_POSITION),
    ('struActionCode', NET_DVR_FRAMETYPECODE),
    ('struPreCode', NET_DVR_FRAMETYPECODE),
    ('byActionCodeMode', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_ATM_PACKAGE_ACTION = struct_tagNET_DVR_ATM_PACKAGE_ACTION
LPNET_DVR_ATM_PACKAGE_ACTION = POINTER(struct_tagNET_DVR_ATM_PACKAGE_ACTION)
tagNET_DVR_ATM_PACKAGE_ACTION = struct_tagNET_DVR_ATM_PACKAGE_ACTION
