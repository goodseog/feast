# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/Entity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.protos.feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66\x65\x61st/core/Entity.proto\x12\nfeast.core\x1a\x17\x66\x65\x61st/types/Value.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"V\n\x06\x45ntity\x12&\n\x04spec\x18\x01 \x01(\x0b\x32\x18.feast.core.EntitySpecV2\x12$\n\x04meta\x18\x02 \x01(\x0b\x32\x16.feast.core.EntityMeta\"\xf3\x01\n\x0c\x45ntitySpecV2\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\t \x01(\t\x12/\n\nvalue_type\x18\x02 \x01(\x0e\x32\x1b.feast.types.ValueType.Enum\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08join_key\x18\x04 \x01(\t\x12\x30\n\x04tags\x18\x08 \x03(\x0b\x32\".feast.core.EntitySpecV2.TagsEntry\x12\r\n\x05owner\x18\n \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x7f\n\nEntityMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampBP\n\x10\x66\x65\x61st.proto.coreB\x0b\x45ntityProtoZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')



_ENTITY = DESCRIPTOR.message_types_by_name['Entity']
_ENTITYSPECV2 = DESCRIPTOR.message_types_by_name['EntitySpecV2']
_ENTITYSPECV2_TAGSENTRY = _ENTITYSPECV2.nested_types_by_name['TagsEntry']
_ENTITYMETA = DESCRIPTOR.message_types_by_name['EntityMeta']
Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'feast.core.Entity_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.Entity)
  })
_sym_db.RegisterMessage(Entity)

EntitySpecV2 = _reflection.GeneratedProtocolMessageType('EntitySpecV2', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENTITYSPECV2_TAGSENTRY,
    '__module__' : 'feast.core.Entity_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.EntitySpecV2.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _ENTITYSPECV2,
  '__module__' : 'feast.core.Entity_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.EntitySpecV2)
  })
_sym_db.RegisterMessage(EntitySpecV2)
_sym_db.RegisterMessage(EntitySpecV2.TagsEntry)

EntityMeta = _reflection.GeneratedProtocolMessageType('EntityMeta', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYMETA,
  '__module__' : 'feast.core.Entity_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.EntityMeta)
  })
_sym_db.RegisterMessage(EntityMeta)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020feast.proto.coreB\013EntityProtoZ/github.com/feast-dev/feast/go/protos/feast/core'
  _ENTITYSPECV2_TAGSENTRY._options = None
  _ENTITYSPECV2_TAGSENTRY._serialized_options = b'8\001'
  _ENTITY._serialized_start=97
  _ENTITY._serialized_end=183
  _ENTITYSPECV2._serialized_start=186
  _ENTITYSPECV2._serialized_end=429
  _ENTITYSPECV2_TAGSENTRY._serialized_start=386
  _ENTITYSPECV2_TAGSENTRY._serialized_end=429
  _ENTITYMETA._serialized_start=431
  _ENTITYMETA._serialized_end=558
# @@protoc_insertion_point(module_scope)