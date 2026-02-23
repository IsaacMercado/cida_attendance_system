from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MB_SENSORINPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_SENSORINPARA, [
    ('dwSize', DWORD),
    ('byTriggerType', BYTE * 8),
    ('byTriggerChannel', BYTE * 8),
    ('byOsdDisplay', BYTE * int((32 + 32))),
    ('byRes', BYTE * 32),
])

NET_DVR_MB_SENSORINPARA = struct_tagNET_DVR_MB_SENSORINPARA
LPNET_DVR_MB_SENSORINPARA = POINTER(struct_tagNET_DVR_MB_SENSORINPARA)
tagNET_DVR_MB_SENSORINPARA = struct_tagNET_DVR_MB_SENSORINPARA
