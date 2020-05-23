# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ValueType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Enum(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'ValueType.Enum': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['ValueType.Enum']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'ValueType.Enum']]: ...
        INVALID = typing___cast('ValueType.Enum', 0)
        BYTES = typing___cast('ValueType.Enum', 1)
        STRING = typing___cast('ValueType.Enum', 2)
        INT32 = typing___cast('ValueType.Enum', 3)
        INT64 = typing___cast('ValueType.Enum', 4)
        DOUBLE = typing___cast('ValueType.Enum', 5)
        FLOAT = typing___cast('ValueType.Enum', 6)
        BOOL = typing___cast('ValueType.Enum', 7)
        BYTES_LIST = typing___cast('ValueType.Enum', 11)
        STRING_LIST = typing___cast('ValueType.Enum', 12)
        INT32_LIST = typing___cast('ValueType.Enum', 13)
        INT64_LIST = typing___cast('ValueType.Enum', 14)
        DOUBLE_LIST = typing___cast('ValueType.Enum', 15)
        FLOAT_LIST = typing___cast('ValueType.Enum', 16)
        BOOL_LIST = typing___cast('ValueType.Enum', 17)
    INVALID = typing___cast('ValueType.Enum', 0)
    BYTES = typing___cast('ValueType.Enum', 1)
    STRING = typing___cast('ValueType.Enum', 2)
    INT32 = typing___cast('ValueType.Enum', 3)
    INT64 = typing___cast('ValueType.Enum', 4)
    DOUBLE = typing___cast('ValueType.Enum', 5)
    FLOAT = typing___cast('ValueType.Enum', 6)
    BOOL = typing___cast('ValueType.Enum', 7)
    BYTES_LIST = typing___cast('ValueType.Enum', 11)
    STRING_LIST = typing___cast('ValueType.Enum', 12)
    INT32_LIST = typing___cast('ValueType.Enum', 13)
    INT64_LIST = typing___cast('ValueType.Enum', 14)
    DOUBLE_LIST = typing___cast('ValueType.Enum', 15)
    FLOAT_LIST = typing___cast('ValueType.Enum', 16)
    BOOL_LIST = typing___cast('ValueType.Enum', 17)
    global___Enum = Enum


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ValueType: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ValueType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___ValueType = ValueType

class Value(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    bytes_val = ... # type: builtin___bytes
    string_val = ... # type: typing___Text
    int32_val = ... # type: builtin___int
    int64_val = ... # type: builtin___int
    double_val = ... # type: builtin___float
    float_val = ... # type: builtin___float
    bool_val = ... # type: builtin___bool

    @property
    def bytes_list_val(self) -> global___BytesList: ...

    @property
    def string_list_val(self) -> global___StringList: ...

    @property
    def int32_list_val(self) -> global___Int32List: ...

    @property
    def int64_list_val(self) -> global___Int64List: ...

    @property
    def double_list_val(self) -> global___DoubleList: ...

    @property
    def float_list_val(self) -> global___FloatList: ...

    @property
    def bool_list_val(self) -> global___BoolList: ...

    def __init__(self,
        *,
        bytes_val : typing___Optional[builtin___bytes] = None,
        string_val : typing___Optional[typing___Text] = None,
        int32_val : typing___Optional[builtin___int] = None,
        int64_val : typing___Optional[builtin___int] = None,
        double_val : typing___Optional[builtin___float] = None,
        float_val : typing___Optional[builtin___float] = None,
        bool_val : typing___Optional[builtin___bool] = None,
        bytes_list_val : typing___Optional[global___BytesList] = None,
        string_list_val : typing___Optional[global___StringList] = None,
        int32_list_val : typing___Optional[global___Int32List] = None,
        int64_list_val : typing___Optional[global___Int64List] = None,
        double_list_val : typing___Optional[global___DoubleList] = None,
        float_list_val : typing___Optional[global___FloatList] = None,
        bool_list_val : typing___Optional[global___BoolList] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Value: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Value: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bool_list_val",b"bool_list_val",u"bool_val",b"bool_val",u"bytes_list_val",b"bytes_list_val",u"bytes_val",b"bytes_val",u"double_list_val",b"double_list_val",u"double_val",b"double_val",u"float_list_val",b"float_list_val",u"float_val",b"float_val",u"int32_list_val",b"int32_list_val",u"int32_val",b"int32_val",u"int64_list_val",b"int64_list_val",u"int64_val",b"int64_val",u"string_list_val",b"string_list_val",u"string_val",b"string_val",u"val",b"val"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bool_list_val",b"bool_list_val",u"bool_val",b"bool_val",u"bytes_list_val",b"bytes_list_val",u"bytes_val",b"bytes_val",u"double_list_val",b"double_list_val",u"double_val",b"double_val",u"float_list_val",b"float_list_val",u"float_val",b"float_val",u"int32_list_val",b"int32_list_val",u"int32_val",b"int32_val",u"int64_list_val",b"int64_list_val",u"int64_val",b"int64_val",u"string_list_val",b"string_list_val",u"string_val",b"string_val",u"val",b"val"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"val",b"val"]) -> typing_extensions___Literal["bytes_val","string_val","int32_val","int64_val","double_val","float_val","bool_val","bytes_list_val","string_list_val","int32_list_val","int64_list_val","double_list_val","float_list_val","bool_list_val"]: ...
global___Value = Value

class BytesList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BytesList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BytesList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
global___BytesList = BytesList

class StringList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StringList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StringList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
global___StringList = StringList

class Int32List(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[builtin___int]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Int32List: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Int32List: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
global___Int32List = Int32List

class Int64List(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[builtin___int]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Int64List: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Int64List: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
global___Int64List = Int64List

class DoubleList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DoubleList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DoubleList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
global___DoubleList = DoubleList

class FloatList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FloatList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FloatList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
global___FloatList = FloatList

class BoolList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bool]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[builtin___bool]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BoolList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BoolList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
global___BoolList = BoolList
