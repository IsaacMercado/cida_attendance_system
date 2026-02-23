from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_diffdev_info import NET_DVR_DIFFDEV_INFO
from .net_dvr_single_netparam import NET_DVR_SINGLE_NETPARAM


class struct_tagNET_DVR_SINGLE_DEV_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_DEV_INFO, [
    ('dwSize', DWORD),
    ('dwSoftVersion', DWORD),
    ('dwSoftwareBuildDate', DWORD),
    ('byUseInSys', BYTE),
    ('byDevStatus', BYTE),
    ('byDeviceType', BYTE),
    ('byRes1', BYTE * 17),
    ('sDevName', BYTE * 32),
    ('struEtherNet', NET_DVR_SINGLE_NETPARAM * 2),
    ('sSerialNumber', BYTE * 48),
    ('struSubDevInfo', NET_DVR_DIFFDEV_INFO),
    ('dwDeviceIndex', DWORD),
    ('dwSubBoardNo', DWORD),
    ('bySubSysNo', BYTE),
    ('byRes3', BYTE * 3),
    ('wStartAudioTalkChanNo', WORD),
    ('wAudioTalkChanNum', WORD),
    ('byRes2', BYTE * 36),
])

NET_DVR_SINGLE_DEV_INFO = struct_tagNET_DVR_SINGLE_DEV_INFO
LPNET_DVR_SINGLE_DEV_INFO = POINTER(struct_tagNET_DVR_SINGLE_DEV_INFO)
tagNET_DVR_SINGLE_DEV_INFO = struct_tagNET_DVR_SINGLE_DEV_INFO
