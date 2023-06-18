# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/Store.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66\x65\x61st/core/Store.proto\x12\nfeast.core\"\xfd\x06\n\x05Store\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.feast.core.Store.StoreType\x12\x35\n\rsubscriptions\x18\x04 \x03(\x0b\x32\x1e.feast.core.Store.Subscription\x12\x35\n\x0credis_config\x18\x0b \x01(\x0b\x32\x1d.feast.core.Store.RedisConfigH\x00\x12\x44\n\x14redis_cluster_config\x18\x0e \x01(\x0b\x32$.feast.core.Store.RedisClusterConfigH\x00\x1a\x88\x01\n\x0bRedisConfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x1a\n\x12initial_backoff_ms\x18\x03 \x01(\x05\x12\x13\n\x0bmax_retries\x18\x04 \x01(\x05\x12\x1f\n\x17\x66lush_frequency_seconds\x18\x05 \x01(\x05\x12\x0b\n\x03ssl\x18\x06 \x01(\x08\x1a\xdb\x02\n\x12RedisClusterConfig\x12\x19\n\x11\x63onnection_string\x18\x01 \x01(\t\x12\x1a\n\x12initial_backoff_ms\x18\x02 \x01(\x05\x12\x13\n\x0bmax_retries\x18\x03 \x01(\x05\x12\x1f\n\x17\x66lush_frequency_seconds\x18\x04 \x01(\x05\x12\x12\n\nkey_prefix\x18\x05 \x01(\t\x12\x17\n\x0f\x65nable_fallback\x18\x06 \x01(\x08\x12\x17\n\x0f\x66\x61llback_prefix\x18\x07 \x01(\t\x12@\n\tread_from\x18\x08 \x01(\x0e\x32-.feast.core.Store.RedisClusterConfig.ReadFrom\"P\n\x08ReadFrom\x12\n\n\x06MASTER\x10\x00\x12\x14\n\x10MASTER_PREFERRED\x10\x01\x12\x0b\n\x07REPLICA\x10\x02\x12\x15\n\x11REPLICA_PREFERRED\x10\x03\x1a\x44\n\x0cSubscription\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x65xclude\x18\x04 \x01(\x08J\x04\x08\x02\x10\x03\"N\n\tStoreType\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05REDIS\x10\x01\x12\x11\n\rREDIS_CLUSTER\x10\x04\"\x04\x08\x02\x10\x02\"\x04\x08\x03\x10\x03\"\x04\x08\x0c\x10\x0c\"\x04\x08\r\x10\rB\x08\n\x06\x63onfigBO\n\x10\x66\x65\x61st.proto.coreB\nStoreProtoZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')



_STORE = DESCRIPTOR.message_types_by_name['Store']
_STORE_REDISCONFIG = _STORE.nested_types_by_name['RedisConfig']
_STORE_REDISCLUSTERCONFIG = _STORE.nested_types_by_name['RedisClusterConfig']
_STORE_SUBSCRIPTION = _STORE.nested_types_by_name['Subscription']
_STORE_REDISCLUSTERCONFIG_READFROM = _STORE_REDISCLUSTERCONFIG.enum_types_by_name['ReadFrom']
_STORE_STORETYPE = _STORE.enum_types_by_name['StoreType']
Store = _reflection.GeneratedProtocolMessageType('Store', (_message.Message,), {

  'RedisConfig' : _reflection.GeneratedProtocolMessageType('RedisConfig', (_message.Message,), {
    'DESCRIPTOR' : _STORE_REDISCONFIG,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.RedisConfig)
    })
  ,

  'RedisClusterConfig' : _reflection.GeneratedProtocolMessageType('RedisClusterConfig', (_message.Message,), {
    'DESCRIPTOR' : _STORE_REDISCLUSTERCONFIG,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.RedisClusterConfig)
    })
  ,

  'Subscription' : _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), {
    'DESCRIPTOR' : _STORE_SUBSCRIPTION,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.Subscription)
    })
  ,
  'DESCRIPTOR' : _STORE,
  '__module__' : 'feast.core.Store_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.Store)
  })
_sym_db.RegisterMessage(Store)
_sym_db.RegisterMessage(Store.RedisConfig)
_sym_db.RegisterMessage(Store.RedisClusterConfig)
_sym_db.RegisterMessage(Store.Subscription)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020feast.proto.coreB\nStoreProtoZ/github.com/feast-dev/feast/go/protos/feast/core'
  _STORE._serialized_start=39
  _STORE._serialized_end=932
  _STORE_REDISCONFIG._serialized_start=286
  _STORE_REDISCONFIG._serialized_end=422
  _STORE_REDISCLUSTERCONFIG._serialized_start=425
  _STORE_REDISCLUSTERCONFIG._serialized_end=772
  _STORE_REDISCLUSTERCONFIG_READFROM._serialized_start=692
  _STORE_REDISCLUSTERCONFIG_READFROM._serialized_end=772
  _STORE_SUBSCRIPTION._serialized_start=774
  _STORE_SUBSCRIPTION._serialized_end=842
  _STORE_STORETYPE._serialized_start=844
  _STORE_STORETYPE._serialized_end=922
# @@protoc_insertion_point(module_scope)