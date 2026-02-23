from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_proto_type_ex import NET_DVR_PROTO_TYPE_EX


class struct_tagNET_DVR_MATRIXMANAGE_ABIILITY(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXMANAGE_ABIILITY, [
    ('dwSize', DWORD),
    ('dwMaxCameraNum', DWORD),
    ('dwMaxMonitorNum', DWORD),
    ('wMaxMatrixNum', WORD),
    ('wMaxSerialNum', WORD),
    ('wMaxUser', WORD),
    ('wMaxResourceArrayNum', WORD),
    ('wMaxUserArrayNum', WORD),
    ('wMaxTrunkNum', WORD),
    ('nStartUserNum', BYTE),
    ('nStartUserGroupNum', BYTE),
    ('nStartResourceGroupNum', BYTE),
    ('nStartSerialNum', BYTE),
    ('dwMatrixProtoNum', DWORD),
    ('struMatrixProto', NET_DVR_PROTO_TYPE_EX * 20),
    ('dwKeyBoardProtoNum', DWORD),
    ('struKeyBoardProto', NET_DVR_PROTO_TYPE_EX * 20),
    ('byDelMonitorLongCfg', BYTE),
    ('byDelCamonitorLongCfg', BYTE),
    ('byAudioSwitchContorl', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_MATRIXMANAGE_ABILITY = struct_tagNET_DVR_MATRIXMANAGE_ABIILITY
LPNET_DVR_MATRIXMANAGE_ABILITY = POINTER(struct_tagNET_DVR_MATRIXMANAGE_ABIILITY)
tagNET_DVR_MATRIXMANAGE_ABIILITY = struct_tagNET_DVR_MATRIXMANAGE_ABIILITY
