# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kd.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08kd.proto\"\x1d\n\nIdxRequest\x12\x0f\n\x07idx_ori\x18\x01 \x03(\r\"\x1e\n\x0bIdxResponse\x12\x0f\n\x07idx_upd\x18\x01 \x03(\r\"\x1f\n\x0bGradRequest\x12\x10\n\x08grad_ori\x18\x01 \x03(\x05\" \n\x0cGradResponse\x12\x10\n\x08grad_upd\x18\x01 \x03(\x05\x32o\n\x16\x43ollaborative_Learning\x12(\n\tUpdateIdx\x12\x0b.IdxRequest\x1a\x0c.IdxResponse\"\x00\x12+\n\nUpdateGrad\x12\x0c.GradRequest\x1a\r.GradResponse\"\x00\x62\x06proto3'
)




_IDXREQUEST = _descriptor.Descriptor(
  name='IdxRequest',
  full_name='IdxRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_ori', full_name='IdxRequest.idx_ori', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=41,
)


_IDXRESPONSE = _descriptor.Descriptor(
  name='IdxResponse',
  full_name='IdxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_upd', full_name='IdxResponse.idx_upd', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=73,
)


_GRADREQUEST = _descriptor.Descriptor(
  name='GradRequest',
  full_name='GradRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='grad_ori', full_name='GradRequest.grad_ori', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=106,
)


_GRADRESPONSE = _descriptor.Descriptor(
  name='GradResponse',
  full_name='GradResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='grad_upd', full_name='GradResponse.grad_upd', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['IdxRequest'] = _IDXREQUEST
DESCRIPTOR.message_types_by_name['IdxResponse'] = _IDXRESPONSE
DESCRIPTOR.message_types_by_name['GradRequest'] = _GRADREQUEST
DESCRIPTOR.message_types_by_name['GradResponse'] = _GRADRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IdxRequest = _reflection.GeneratedProtocolMessageType('IdxRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDXREQUEST,
  '__module__' : 'kd_pb2'
  # @@protoc_insertion_point(class_scope:IdxRequest)
  })
_sym_db.RegisterMessage(IdxRequest)

IdxResponse = _reflection.GeneratedProtocolMessageType('IdxResponse', (_message.Message,), {
  'DESCRIPTOR' : _IDXRESPONSE,
  '__module__' : 'kd_pb2'
  # @@protoc_insertion_point(class_scope:IdxResponse)
  })
_sym_db.RegisterMessage(IdxResponse)

GradRequest = _reflection.GeneratedProtocolMessageType('GradRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADREQUEST,
  '__module__' : 'kd_pb2'
  # @@protoc_insertion_point(class_scope:GradRequest)
  })
_sym_db.RegisterMessage(GradRequest)

GradResponse = _reflection.GeneratedProtocolMessageType('GradResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADRESPONSE,
  '__module__' : 'kd_pb2'
  # @@protoc_insertion_point(class_scope:GradResponse)
  })
_sym_db.RegisterMessage(GradResponse)



_COLLABORATIVE_LEARNING = _descriptor.ServiceDescriptor(
  name='Collaborative_Learning',
  full_name='Collaborative_Learning',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=142,
  serialized_end=253,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateIdx',
    full_name='Collaborative_Learning.UpdateIdx',
    index=0,
    containing_service=None,
    input_type=_IDXREQUEST,
    output_type=_IDXRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateGrad',
    full_name='Collaborative_Learning.UpdateGrad',
    index=1,
    containing_service=None,
    input_type=_GRADREQUEST,
    output_type=_GRADRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COLLABORATIVE_LEARNING)

DESCRIPTOR.services_by_name['Collaborative_Learning'] = _COLLABORATIVE_LEARNING

# @@protoc_insertion_point(module_scope)