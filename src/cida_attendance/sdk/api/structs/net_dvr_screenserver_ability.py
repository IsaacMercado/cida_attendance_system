from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_proto_type import NET_DVR_PROTO_TYPE


class struct_tagNET_DVR_SCREENSERVER_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_SCREENSERVER_ABILITY, [
    ('dwSize', DWORD),
    ('byIsSupportScreenNum', BYTE),
    ('bySerialNums', BYTE),
    ('byMaxInputNums', BYTE),
    ('byMaxLayoutNums', BYTE),
    ('byMaxWinNums', BYTE),
    ('byRes1', BYTE * 19),
    ('byMaxScreenLayX', BYTE),
    ('byMaxScreenLayY', BYTE),
    ('wMatrixProtoNum', WORD),
    ('struScreenProto', NET_DVR_PROTO_TYPE * 20),
    ('byRes2', BYTE * 24),
])

NET_DVR_SCREENSERVER_ABILITY = struct_tagNET_DVR_SCREENSERVER_ABILITY
LPNET_DVR_SCREENSERVER_ABILITY = POINTER(struct_tagNET_DVR_SCREENSERVER_ABILITY)
tagNET_DVR_SCREENSERVER_ABILITY = struct_tagNET_DVR_SCREENSERVER_ABILITY
