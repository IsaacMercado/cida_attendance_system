from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PAPERCHARGEINFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PAPERCHARGEINFO_CFG, [
    ('dwSize', DWORD),
    ('szBarCode', c_char * 16),
    ('szLicense', c_char * 16),
    ('szVehicleInTime', c_char * 32),
    ('szPaymentTime', c_char * 32),
    ('fPaymentAmount', c_float),
    ('dwPaymentOutFailureTime', DWORD),
    ('byVehicleOutEnabled', BYTE),
    ('byRes', BYTE * 128),
])

NET_DVR_PAPERCHARGEINFO_CFG = struct_tagNET_DVR_PAPERCHARGEINFO_CFG
LPNET_DVR_PAPERCHARGEINFO_CFG = POINTER(struct_tagNET_DVR_PAPERCHARGEINFO_CFG)
tagNET_DVR_PAPERCHARGEINFO_CFG = struct_tagNET_DVR_PAPERCHARGEINFO_CFG
