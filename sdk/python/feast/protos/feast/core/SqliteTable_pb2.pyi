"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SqliteTable(google.protobuf.message.Message):
    """Represents a Sqlite table"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATH_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    path: typing.Text = ...
    """Absolute path of the table"""

    name: typing.Text = ...
    """Name of the table"""

    def __init__(self,
        *,
        path : typing.Text = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","path",b"path"]) -> None: ...
global___SqliteTable = SqliteTable