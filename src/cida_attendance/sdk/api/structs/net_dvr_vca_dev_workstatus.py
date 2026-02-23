from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_vca_chan_workstatus import NET_DVR_VCA_CHAN_WORKSTATUS


class struct_tagNET_DVR_VCA_DEV_WORKSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_VCA_DEV_WORKSTATUS, [
    ('dwSize', DWORD),
    ('byDeviceStatus', BYTE),
    ('byCpuLoad', BYTE),
    ('struVcaChanStatus', NET_DVR_VCA_CHAN_WORKSTATUS * 16),
    ('dwRes', DWORD * 40),
])

NET_DVR_VCA_DEV_WORKSTATUS = struct_tagNET_DVR_VCA_DEV_WORKSTATUS
LPNET_DVR_VCA_DEV_WORKSTATUS = POINTER(struct_tagNET_DVR_VCA_DEV_WORKSTATUS)
tagNET_DVR_VCA_DEV_WORKSTATUS = struct_tagNET_DVR_VCA_DEV_WORKSTATUS
