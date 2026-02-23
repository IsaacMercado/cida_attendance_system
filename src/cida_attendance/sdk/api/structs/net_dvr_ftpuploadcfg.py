from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ftpupload_param import NET_DVR_FTPUPLOAD_PARAM


class struct_tagNET_DVR_FTPUPLOADCFG(Structure):
    pass

_S(struct_tagNET_DVR_FTPUPLOADCFG, [
    ('dwSize', DWORD),
    ('byEventType', BYTE),
    ('byMode', BYTE),
    ('byRes', BYTE * 62),
    ('struCustomVehicle', NET_DVR_FTPUPLOAD_PARAM * 12),
    ('byRes1', BYTE * 1024),
])

NET_DVR_FTPUPLOADCFG = struct_tagNET_DVR_FTPUPLOADCFG
LPNET_DVR_FTPUPLOADCFG = POINTER(struct_tagNET_DVR_FTPUPLOADCFG)
tagNET_DVR_FTPUPLOADCFG = struct_tagNET_DVR_FTPUPLOADCFG
