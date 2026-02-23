from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_t1test_data_union import NET_DVR_T1TEST_DATA_UNION


class struct_tagNET_DVR_T1TEST_SEND_DATA(Structure):
    pass

_S(struct_tagNET_DVR_T1TEST_SEND_DATA, [
    ('dwSize', DWORD),
    ('byDataType', BYTE),
    ('byRes1', BYTE * 3),
    ('uSendData', NET_DVR_T1TEST_DATA_UNION),
    ('byRes', BYTE * 64),
])

NET_DVR_T1TEST_SEND_DATA = struct_tagNET_DVR_T1TEST_SEND_DATA
LPNET_DVR_T1TEST_SEND_DATA = POINTER(struct_tagNET_DVR_T1TEST_SEND_DATA)
tagNET_DVR_T1TEST_SEND_DATA = struct_tagNET_DVR_T1TEST_SEND_DATA
