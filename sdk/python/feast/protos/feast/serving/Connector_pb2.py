# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/serving/Connector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.protos.feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2
from feast.protos.feast.types import EntityKey_pb2 as feast_dot_types_dot_EntityKey__pb2
from feast.protos.feast.serving import ServingService_pb2 as feast_dot_serving_dot_ServingService__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66\x65\x61st/serving/Connector.proto\x12\x0egrpc.connector\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17\x66\x65\x61st/types/Value.proto\x1a\x1b\x66\x65\x61st/types/EntityKey.proto\x1a\"feast/serving/ServingService.proto\"\x9a\x01\n\x10\x43onnectorFeature\x12\x34\n\treference\x18\x01 \x01(\x0b\x32!.feast.serving.FeatureReferenceV2\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x05value\x18\x03 \x01(\x0b\x32\x12.feast.types.Value\"M\n\x14\x43onnectorFeatureList\x12\x35\n\x0b\x66\x65\x61tureList\x18\x01 \x03(\x0b\x32 .grpc.connector.ConnectorFeature\"_\n\x11OnlineReadRequest\x12*\n\nentityKeys\x18\x01 \x03(\x0b\x32\x16.feast.types.EntityKey\x12\x0c\n\x04view\x18\x02 \x01(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x03 \x03(\t\"K\n\x12OnlineReadResponse\x12\x35\n\x07results\x18\x01 \x03(\x0b\x32$.grpc.connector.ConnectorFeatureList2b\n\x0bOnlineStore\x12S\n\nOnlineRead\x12!.grpc.connector.OnlineReadRequest\x1a\".grpc.connector.OnlineReadResponseB4Z2github.com/feast-dev/feast/go/protos/feast/servingb\x06proto3')



_CONNECTORFEATURE = DESCRIPTOR.message_types_by_name['ConnectorFeature']
_CONNECTORFEATURELIST = DESCRIPTOR.message_types_by_name['ConnectorFeatureList']
_ONLINEREADREQUEST = DESCRIPTOR.message_types_by_name['OnlineReadRequest']
_ONLINEREADRESPONSE = DESCRIPTOR.message_types_by_name['OnlineReadResponse']
ConnectorFeature = _reflection.GeneratedProtocolMessageType('ConnectorFeature', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTORFEATURE,
  '__module__' : 'feast.serving.Connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.connector.ConnectorFeature)
  })
_sym_db.RegisterMessage(ConnectorFeature)

ConnectorFeatureList = _reflection.GeneratedProtocolMessageType('ConnectorFeatureList', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTORFEATURELIST,
  '__module__' : 'feast.serving.Connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.connector.ConnectorFeatureList)
  })
_sym_db.RegisterMessage(ConnectorFeatureList)

OnlineReadRequest = _reflection.GeneratedProtocolMessageType('OnlineReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _ONLINEREADREQUEST,
  '__module__' : 'feast.serving.Connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.connector.OnlineReadRequest)
  })
_sym_db.RegisterMessage(OnlineReadRequest)

OnlineReadResponse = _reflection.GeneratedProtocolMessageType('OnlineReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _ONLINEREADRESPONSE,
  '__module__' : 'feast.serving.Connector_pb2'
  # @@protoc_insertion_point(class_scope:grpc.connector.OnlineReadResponse)
  })
_sym_db.RegisterMessage(OnlineReadResponse)

_ONLINESTORE = DESCRIPTOR.services_by_name['OnlineStore']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/feast-dev/feast/go/protos/feast/serving'
  _CONNECTORFEATURE._serialized_start=173
  _CONNECTORFEATURE._serialized_end=327
  _CONNECTORFEATURELIST._serialized_start=329
  _CONNECTORFEATURELIST._serialized_end=406
  _ONLINEREADREQUEST._serialized_start=408
  _ONLINEREADREQUEST._serialized_end=503
  _ONLINEREADRESPONSE._serialized_start=505
  _ONLINEREADRESPONSE._serialized_end=580
  _ONLINESTORE._serialized_start=582
  _ONLINESTORE._serialized_end=680
# @@protoc_insertion_point(module_scope)