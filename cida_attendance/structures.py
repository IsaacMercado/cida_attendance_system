import ctypes
import datetime

from cida_attendance.constants import (
    ACS_CARD_NO_LEN,
    MACADDR_LEN,
    MAX_CARD_READER_NUM_512,
    MAX_DOOR_NUM_256,
    MAX_FINGER_PRINT_LEN,
    MAX_NAMELEN,
    NAME_LEN,
    NET_DVR_DEV_ADDRESS_MAX_LEN,
    NET_DVR_LOGIN_PASSWD_MAX_LEN,
    NET_DVR_LOGIN_USERNAME_MAX_LEN,
    NET_SDK_EMPLOYEE_NO_LEN,
    NET_SDK_MONITOR_ID_LEN,
    SERIALNO_LEN,
)


class NET_DVR_USER_LOGIN_INFO(ctypes.Structure):
    _fields_ = [
        ("sDeviceAddress", ctypes.c_byte * NET_DVR_DEV_ADDRESS_MAX_LEN),
        ("byUseTransport", ctypes.c_byte),
        ("wPort", ctypes.c_ushort),
        ("sUserName", ctypes.c_byte * NET_DVR_LOGIN_USERNAME_MAX_LEN),
        ("sPassword", ctypes.c_byte * NET_DVR_LOGIN_PASSWD_MAX_LEN),
        ("cbLoginResult", ctypes.c_void_p),
        ("pUser", ctypes.c_void_p),
        ("bUseAsynLogin", ctypes.c_bool),
        ("byProxyType", ctypes.c_byte),
        ("byUseUTCTime", ctypes.c_byte),
        ("byLoginMode", ctypes.c_byte),
        ("byHttps", ctypes.c_byte),
        ("iProxyID", ctypes.c_int),
        ("byVerifyMode", ctypes.c_byte),
        ("byRes3", ctypes.c_byte * 119),
    ]

    @classmethod
    def login(cls, device_address, username, password, port=8000):
        login_info = cls()
        login_info.sDeviceAddress = (ctypes.c_byte * NET_DVR_DEV_ADDRESS_MAX_LEN)(
            *device_address.ljust(NET_DVR_DEV_ADDRESS_MAX_LEN, b"\x00")
        )
        login_info.wPort = port
        login_info.bUseAsynLogin = False
        login_info.sUserName = (ctypes.c_byte * NET_DVR_LOGIN_USERNAME_MAX_LEN)(
            *username.ljust(NET_DVR_LOGIN_USERNAME_MAX_LEN, b"\x00")
        )
        login_info.sPassword = (ctypes.c_byte * NET_DVR_LOGIN_PASSWD_MAX_LEN)(
            *password.ljust(NET_DVR_LOGIN_PASSWD_MAX_LEN, b"\x00")
        )
        return login_info


class NET_DVR_DEVICEINFO_V30(ctypes.Structure):
    _fields_ = [
        ("sSerialNumber", ctypes.c_byte * SERIALNO_LEN),
        ("byAlarmInPortNum", ctypes.c_byte),
        ("byAlarmOutPortNum", ctypes.c_byte),
        ("byDiskNum", ctypes.c_byte),
        ("byDVRType", ctypes.c_byte),
        ("byChanNum", ctypes.c_byte),
        ("byStartChan", ctypes.c_byte),
        ("byAudioChanNum", ctypes.c_byte),
        ("byIPChanNum", ctypes.c_byte),
        ("byZeroChanNum", ctypes.c_byte),
        ("byMainProto", ctypes.c_byte),
        ("bySubProto", ctypes.c_byte),
        ("bySupport", ctypes.c_byte),
        ("bySupport1", ctypes.c_byte),
        ("bySupport2", ctypes.c_byte),
        ("wDevType", ctypes.c_ushort),
        ("bySupport3", ctypes.c_byte),
        ("byMultiStreamProto", ctypes.c_byte),
        ("byStartDChan", ctypes.c_byte),
        ("byStartDTalkChan", ctypes.c_byte),
        ("byHighDChanNum", ctypes.c_byte),
        ("bySupport4", ctypes.c_byte),
        ("byLanguageType", ctypes.c_byte),
        ("byRes2", ctypes.c_byte * 9),
    ]


class NET_DVR_DEVICEINFO_V40(ctypes.Structure):
    _fields_ = [
        ("struDeviceV30", NET_DVR_DEVICEINFO_V30),
        ("bySupportLock", ctypes.c_byte),
        ("byRetryLoginTime", ctypes.c_byte),
        ("byPasswordLevel", ctypes.c_byte),
        ("byProxyType", ctypes.c_byte),
        ("dwSurplusLockTime", ctypes.c_uint),
        ("byCharEncodeType", ctypes.c_byte),
        ("bySupportDev5", ctypes.c_byte),
        ("bySupport", ctypes.c_byte),
        ("byLoginMode", ctypes.c_byte),
        ("dwOEMCode", ctypes.c_int),
        ("iResidualValidity", ctypes.c_int),
        ("byResidualValidity", ctypes.c_byte),
        ("byRes2", ctypes.c_byte * 243),
    ]


class NET_DVR_XML_CONFIG_INPUT(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("lpRequestUrl", ctypes.c_void_p),
        ("dwRequestUrlLen", ctypes.c_uint),
        ("lpInBuffer", ctypes.c_void_p),
        ("dwInBufferSize", ctypes.c_uint),
        ("dwRecvTimeOut", ctypes.c_uint),
        ("byForceEncrpt", ctypes.c_byte),
        ("byNumOfMultiPart", ctypes.c_byte),
        ("byMIMEType", ctypes.c_byte),
        ("byRes", ctypes.c_byte * 29),
    ]

    def __init__(self):
        self.dwSize = ctypes.sizeof(self)


class NET_DVR_XML_CONFIG_OUTPUT(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("lpOutBuffer", ctypes.c_void_p),
        ("dwOutBufferSize", ctypes.c_uint),
        ("dwReturnedXMLSize", ctypes.c_uint),
        ("lpStatusBuffer", ctypes.c_void_p),
        ("dwStatusSize", ctypes.c_uint),
        ("lpDataBuffer", ctypes.c_void_p),
        ("byNumOfMultiPart", ctypes.c_byte),
        ("byRes", ctypes.c_byte * 23),
    ]


class NET_DVR_TIME(ctypes.Structure):
    _fields_ = [
        ("dwYear", ctypes.c_int),
        ("dwMonth", ctypes.c_int),
        ("dwDay", ctypes.c_int),
        ("dwHour", ctypes.c_int),
        ("dwMinute", ctypes.c_int),
        ("dwSecond", ctypes.c_int),
    ]

    def to_python(self, tz=None):
        return datetime.datetime(
            self.dwYear,
            self.dwMonth,
            self.dwDay,
            self.dwHour,
            self.dwMinute,
            self.dwSecond,
            tzinfo=tz,
        )

    def from_datetime(self, dt):
        self.dwYear = dt.year
        self.dwMonth = dt.month
        self.dwDay = dt.day
        self.dwHour = dt.hour
        self.dwMinute = dt.minute
        self.dwSecond = dt.second


class NET_DVR_ACS_EVENT_COND(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("dwMajor", ctypes.c_uint),
        ("dwMinor", ctypes.c_uint),
        ("struStartTime", NET_DVR_TIME),
        ("struEndTime", NET_DVR_TIME),
        ("byCardNo", ctypes.c_byte * ACS_CARD_NO_LEN),
        ("byName", ctypes.c_byte * NAME_LEN),
        ("dwBeginSerialNo", ctypes.c_uint),
        ("byPicEnable", ctypes.c_byte),
        ("byTimeType", ctypes.c_byte),
        ("byRes2", ctypes.c_byte * 2),
        ("dwEndSerialNo", ctypes.c_uint),
        ("dwIOTChannelNo", ctypes.c_uint),
        ("wInductiveEventType", ctypes.c_ushort),
        ("bySearchType", ctypes.c_byte),
        ("byRes1", ctypes.c_byte),
        ("szMonitorID", ctypes.c_char * NET_SDK_MONITOR_ID_LEN),
        ("byEmployeeNo", ctypes.c_byte * NET_SDK_EMPLOYEE_NO_LEN),
        ("byRes", ctypes.c_byte * 140),
    ]

    def __init__(self):
        self.dwSize = ctypes.sizeof(self)

    @classmethod
    def from_python(
        cls,
        major: int = None,
        minor: int = None,
        start_time: datetime.datetime = None,
        end_time: datetime.datetime = None,
    ):
        cond = cls()
        cond.dwSize = ctypes.sizeof(cls)

        if major is not None:
            cond.dwMajor = major

        if minor is not None:
            cond.dwMinor = minor

        if start_time is not None:
            cond.struStartTime.from_datetime(start_time)

        if end_time is not None:
            cond.struEndTime.from_datetime(end_time)

        return cond


class NET_DVR_IPADDR(ctypes.Structure):
    _fields_ = [
        ("sIpV4", ctypes.c_char * 16),
        ("byIPv6", ctypes.c_char * 128),
    ]

    def __init__(self):
        self.byIPv6 = (ctypes.c_byte * 128)()

    def to_python(self):
        return {
            "sIpV4": self.sIpV4.decode("ascii"),
            "byIPv6": self.byIPv6.decode("ascii"),
        }


class NET_VCA_POINT(ctypes.Structure):
    _fields_ = [
        ("fX", ctypes.c_float),  # X axis coordinate,  0.000~1
        ("fY", ctypes.c_float),  # Y axis coordinate,  0.000~1
    ]


class NET_DVR_ACS_EVENT_DETAIL(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("byCardNo", ctypes.c_byte * ACS_CARD_NO_LEN),
        ("byCardType", ctypes.c_byte),
        ("byAllowListNo", ctypes.c_byte),
        ("byReportChannel", ctypes.c_byte),
        ("byCardReaderKind", ctypes.c_byte),
        ("dwCardReaderNo", ctypes.c_uint),
        ("dwDoorNo", ctypes.c_uint),
        ("dwVerifyNo", ctypes.c_uint),
        ("dwAlarmInNo", ctypes.c_uint),
        ("dwAlarmOutNo", ctypes.c_uint),
        ("dwCaseSensorNo", ctypes.c_uint),
        ("dwRs485No", ctypes.c_uint),
        ("dwMultiCardGroupNo", ctypes.c_uint),
        ("wAccessChannel", ctypes.c_ushort),
        ("byDeviceNo", ctypes.c_byte),
        ("byDistractControlNo", ctypes.c_byte),
        ("dwEmployeeNo", ctypes.c_uint),
        ("wLocalControllerID", ctypes.c_ushort),
        ("byInternetAccess", ctypes.c_byte),
        ("byType", ctypes.c_byte),
        ("byMACAddr", ctypes.c_byte * MACADDR_LEN),
        ("bySwipeCardType", ctypes.c_byte),
        ("byEventAttribute", ctypes.c_byte),
        ("dwSerialNo", ctypes.c_uint),
        ("byChannelControllerID", ctypes.c_byte),
        ("byChannelControllerLampID", ctypes.c_byte),
        ("byChannelControllerIRAdaptorID", ctypes.c_byte),
        ("byChannelControllerIREmitterID", ctypes.c_byte),
        ("dwRecordChannelNum", ctypes.c_uint),
        ("pRecordChannelData", ctypes.c_char_p),
        ("byUserType", ctypes.c_byte),
        ("byCurrentVerifyMode", ctypes.c_byte),
        ("byAttendanceStatus", ctypes.c_byte),
        ("byStatusValue", ctypes.c_byte),
        ("byEmployeeNo", ctypes.c_byte * NET_SDK_EMPLOYEE_NO_LEN),
        ("byRes1", ctypes.c_byte),
        ("byMask", ctypes.c_byte),
        ("byThermometryUnit", ctypes.c_byte),
        ("byIsAbnomalTemperature", ctypes.c_byte),
        ("fCurrTemperature", ctypes.c_float),
        ("struRegionCoordinates", NET_VCA_POINT),
        ("byRes", ctypes.c_byte * 48),
    ]


class NET_DVR_ACS_EVENT_CFG(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("dwMajor", ctypes.c_uint),
        ("dwMinor", ctypes.c_uint),
        ("struTime", NET_DVR_TIME),
        ("sNetUser", ctypes.c_byte * MAX_NAMELEN),
        ("struRemoteHostAddr", NET_DVR_IPADDR),
        ("struAcsEventInfo", NET_DVR_ACS_EVENT_DETAIL),
        ("dwPicDataLen", ctypes.c_uint),
        ("pPicData", ctypes.c_void_p),
        ("wInductiveEventType", ctypes.c_ushort),
        ("byTimeType", ctypes.c_byte),
        ("byRes", ctypes.c_byte * 61),
    ]


class NET_DVR_CAPTURE_FINGERPRINT_COND(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("byFingerPrintPicType", ctypes.c_byte),
        ("byFingerNo", ctypes.c_byte),
        ("byRes", ctypes.c_byte * 126),
    ]

    def __init__(self):
        self.dwSize = ctypes.sizeof(self)


class NET_DVR_CAPTURE_FINGERPRINT_CFG(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("dwFingerPrintDataSize", ctypes.c_uint),
        ("byFingerData", ctypes.c_byte * MAX_FINGER_PRINT_LEN),
        ("dwFingerPrintPicSize", ctypes.c_uint),
        ("pFingerPrintPicBuffer", ctypes.c_char_p),
        ("byFingerNo", ctypes.c_byte),
        ("byFingerPrintQuality", ctypes.c_byte),
        ("byRes", ctypes.c_byte * 62),
    ]

    def __init__(self):
        self.dwSize = ctypes.sizeof(self)
        self.byFingerData = (ctypes.c_byte * MAX_FINGER_PRINT_LEN)()


class NET_DVR_FINGER_PRINT_INFO_COND_V50(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("byCardNo", ctypes.c_byte * ACS_CARD_NO_LEN),
        ("byEnableCardReader", ctypes.c_byte * MAX_CARD_READER_NUM_512),
        ("dwFingerPrintNum", ctypes.c_uint),
        ("byFingerPrintID", ctypes.c_byte),
        ("byCallbackMode", ctypes.c_byte),
        ("byRes2", ctypes.c_byte * 2),
        ("byEmployeeNo", ctypes.c_byte * NET_SDK_EMPLOYEE_NO_LEN),
        ("byRes1", ctypes.c_byte * 128),
    ]

    def __init__(self):
        self.dwSize = ctypes.sizeof(self)


class NET_DVR_FINGER_PRINT_CFG_V50(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("byCardNo", ctypes.c_byte * ACS_CARD_NO_LEN),
        ("dwFingerPrintLen", ctypes.c_uint),
        ("byEnableCardReader", ctypes.c_byte * MAX_CARD_READER_NUM_512),
        ("byFingerPrintID", ctypes.c_byte),
        ("byFingerType", ctypes.c_byte),
        ("byRes1", ctypes.c_byte * 30),
        ("byFingerData", ctypes.c_byte * MAX_FINGER_PRINT_LEN),
        ("byEmployeeNo", ctypes.c_byte * NET_SDK_EMPLOYEE_NO_LEN),
        ("byLeaderFP", ctypes.c_byte * MAX_DOOR_NUM_256),
        ("byRes", ctypes.c_byte * 128),
    ]

    def __init__(self):
        self.dwSize = ctypes.sizeof(self)
