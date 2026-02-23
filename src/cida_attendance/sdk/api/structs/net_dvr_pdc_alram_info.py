from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .anon_289 import union_anon_289
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_PDC_ALRAM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PDC_ALRAM_INFO, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byChannel', BYTE),
    ('bySmart', BYTE),
    ('byRes1', BYTE),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('uStatModeParam', union_anon_289),
    ('dwLeaveNum', DWORD),
    ('dwEnterNum', DWORD),
    ('byBrokenNetHttp', BYTE),
    ('byRes3', BYTE),
    ('wDevInfoIvmsChannelEx', WORD),
    ('dwPassingNum', DWORD),
    ('dwChildLeaveNum', DWORD),
    ('dwChildEnterNum', DWORD),
    ('dwDuplicatePeople', DWORD),
    ('dwXmlLen', DWORD),
    ('pXmlBuf', String),
    ('byRes2', BYTE * 8),
])

NET_DVR_PDC_ALRAM_INFO = struct_tagNET_DVR_PDC_ALRAM_INFO
LPNET_DVR_PDC_ALRAM_INFO = POINTER(struct_tagNET_DVR_PDC_ALRAM_INFO)
tagNET_DVR_PDC_ALRAM_INFO = struct_tagNET_DVR_PDC_ALRAM_INFO
