from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_397(Structure):
    pass

_S(struct_anon_397, [
    ('dwSize', DWORD),
    ('byIrLampServer', BYTE),
    ('bytelnetServer', BYTE),
    ('byABFServer', BYTE),
    ('byEnableLEDStatus', BYTE),
    ('byEnableAutoDefog', BYTE),
    ('byEnableSupplementLight', BYTE),
    ('byEnableDeicing', BYTE),
    ('byEnableVisibleMovementPower', BYTE),
    ('byEnableThermalMovementPower', BYTE),
    ('byEnablePtzPower', BYTE),
    ('byPowerSavingControl', BYTE),
    ('byCaptureWithSupplimentLightEnabled', BYTE),
    ('byRes', BYTE * 244),
])

NET_DVR_DEVSERVER_CFG = struct_anon_397
LPNET_DVR_DEVSERVER_CFG = POINTER(struct_anon_397)
