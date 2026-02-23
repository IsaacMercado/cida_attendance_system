from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_116 import NET_DVR_FRAMETYPECODE
from .net_dvr_osd_position import NET_DVR_OSD_POSITION
from .net_dvr_package_length import NET_DVR_PACKAGE_LENGTH
from .net_dvr_package_location import NET_DVR_PACKAGE_LOCATION


class struct_tagNET_DVR_ATM_PACKAGE_OTHERS(Structure):
    pass

_S(struct_tagNET_DVR_ATM_PACKAGE_OTHERS, [
    ('struPackageLocation', NET_DVR_PACKAGE_LOCATION),
    ('struPackageLength', NET_DVR_PACKAGE_LENGTH),
    ('struOsdPosition', NET_DVR_OSD_POSITION),
    ('struPreCode', NET_DVR_FRAMETYPECODE),
    ('res', BYTE * 8),
])

NET_DVR_ATM_PACKAGE_OTHERS = struct_tagNET_DVR_ATM_PACKAGE_OTHERS
LPNET_DVR_ATM_PACKAGE_OTHERS = POINTER(struct_tagNET_DVR_ATM_PACKAGE_OTHERS)
tagNET_DVR_ATM_PACKAGE_OTHERS = struct_tagNET_DVR_ATM_PACKAGE_OTHERS
