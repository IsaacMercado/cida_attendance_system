from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARKLAMP_INFOCFG(Structure):
    pass

_S(struct_tagNET_DVR_PARKLAMP_INFOCFG, [
    ('dwSize', DWORD),
    ('sLicense', c_char * 16),
    ('sParkingNo', c_char * 16),
    ('byLampFlicker', BYTE),
    ('byLampColor', BYTE),
    ('byStatus', BYTE),
    ('byColorDepth', BYTE),
    ('byColor', BYTE),
    ('byVehicleLogoRecog', BYTE),
    ('byRes', BYTE * 250),
])

NET_DVR_PARKLAMP_INFOCFG = struct_tagNET_DVR_PARKLAMP_INFOCFG
LPNET_DVR_PARKLAMP_INFOCFG = POINTER(struct_tagNET_DVR_PARKLAMP_INFOCFG)
tagNET_DVR_PARKLAMP_INFOCFG = struct_tagNET_DVR_PARKLAMP_INFOCFG
