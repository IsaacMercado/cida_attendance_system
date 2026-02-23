from ctypes import Structure, c_ubyte

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PACKET_INFO_EX(Structure):
    pass

_S(struct_tagNET_DVR_PACKET_INFO_EX, [
    ('wWidth', WORD),
    ('wHeight', WORD),
    ('dwTimeStamp', DWORD),
    ('dwTimeStampHigh', DWORD),
    ('dwYear', DWORD),
    ('dwMonth', DWORD),
    ('dwDay', DWORD),
    ('dwHour', DWORD),
    ('dwMinute', DWORD),
    ('dwSecond', DWORD),
    ('dwMillisecond', DWORD),
    ('dwFrameNum', DWORD),
    ('dwFrameRate', DWORD),
    ('dwFlag', DWORD),
    ('dwFilePos', DWORD),
    ('dwPacketType', DWORD),
    ('dwPacketSize', DWORD),
    ('pPacketBuffer', POINTER(c_ubyte)),
    ('byRes1', BYTE * 4),
    ('dwPacketMode', DWORD),
    ('byRes2', BYTE * 16),
    ('dwReserved', DWORD * 6),
])

NET_DVR_PACKET_INFO_EX = struct_tagNET_DVR_PACKET_INFO_EX
LPNET_DVR_PACKET_INFO_EX = POINTER(struct_tagNET_DVR_PACKET_INFO_EX)
tagNET_DVR_PACKET_INFO_EX = struct_tagNET_DVR_PACKET_INFO_EX
