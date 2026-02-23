from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_date_format import NET_DVR_DATE_FORMAT
from .net_dvr_osd_position import NET_DVR_OSD_POSITION
from .net_dvr_package_location import NET_DVR_PACKAGE_LOCATION


class struct_tagNET_DVR_ATM_PACKAGE_DATE(Structure):
    pass

_S(struct_tagNET_DVR_ATM_PACKAGE_DATE, [
    ('struPackageLocation', NET_DVR_PACKAGE_LOCATION),
    ('struDateForm', NET_DVR_DATE_FORMAT),
    ('struOsdPosition', NET_DVR_OSD_POSITION),
    ('res', BYTE * 8),
])

NET_DVR_ATM_PACKAGE_DATE = struct_tagNET_DVR_ATM_PACKAGE_DATE
LPNET_DVR_ATM_PACKAGE_DATE = POINTER(struct_tagNET_DVR_ATM_PACKAGE_DATE)
tagNET_DVR_ATM_PACKAGE_DATE = struct_tagNET_DVR_ATM_PACKAGE_DATE
