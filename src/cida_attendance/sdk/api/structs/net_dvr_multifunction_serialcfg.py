from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MULTIFUNCTION_SERIALCFG(Structure):
    pass

_S(struct_tagNET_DVR_MULTIFUNCTION_SERIALCFG, [
    ('dwSize', DWORD),
    ('byVariable', BYTE),
    ('bySerialWorkMode', BYTE),
    ('byFunType', BYTE),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('byRes1', BYTE),
    ('dwBaudRate', DWORD),
    ('wProtocol', WORD),
    ('byRes', BYTE * 34),
])

NET_DVR_MULTIFUNCTION_SERIALCFG = struct_tagNET_DVR_MULTIFUNCTION_SERIALCFG
LPNET_DVR_MULTIFUNCTION_SERIALCFG = POINTER(struct_tagNET_DVR_MULTIFUNCTION_SERIALCFG)
tagNET_DVR_MULTIFUNCTION_SERIALCFG = struct_tagNET_DVR_MULTIFUNCTION_SERIALCFG
