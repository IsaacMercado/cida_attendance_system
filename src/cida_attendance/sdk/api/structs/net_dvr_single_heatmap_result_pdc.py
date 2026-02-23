from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SINGLE_HEATMAP_RESULT_PDC(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_HEATMAP_RESULT_PDC, [
    ('dwMaxHeatMapValue', DWORD),
    ('dwMinHeatMapValue', DWORD),
    ('dwTimeHeatMapValue', DWORD),
    ('wArrayLine', WORD),
    ('wArrayColumn', WORD),
    ('pBuffer', POINTER(BYTE)),
    ('byRes', BYTE * 32),
])

NET_DVR_SINGLE_HEATMAP_RESULT_PDC = struct_tagNET_DVR_SINGLE_HEATMAP_RESULT_PDC
LPNET_DVR_SINGLE_HEATMAP_RESULT_PDC = POINTER(struct_tagNET_DVR_SINGLE_HEATMAP_RESULT_PDC)
tagNET_DVR_SINGLE_HEATMAP_RESULT_PDC = struct_tagNET_DVR_SINGLE_HEATMAP_RESULT_PDC
