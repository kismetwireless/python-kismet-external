# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eventbus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='eventbus.proto',
  package='KismetEventBus',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x0e\x65ventbus.proto\x12\x0eKismetEventBus\"#\n\rEventbusEvent\x12\x12\n\nevent_json\x18\x01 \x02(\t\")\n\x18\x45ventbusRegisterListener\x12\r\n\x05\x65vent\x18\x01 \x03(\t\"F\n\x14\x45ventbusPublishEvent\x12\x12\n\nevent_type\x18\x01 \x02(\t\x12\x1a\n\x12\x65vent_content_json\x18\x02 \x02(\tB\x02H\x03')
)




_EVENTBUSEVENT = _descriptor.Descriptor(
  name='EventbusEvent',
  full_name='KismetEventBus.EventbusEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_json', full_name='KismetEventBus.EventbusEvent.event_json', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=69,
)


_EVENTBUSREGISTERLISTENER = _descriptor.Descriptor(
  name='EventbusRegisterListener',
  full_name='KismetEventBus.EventbusRegisterListener',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='KismetEventBus.EventbusRegisterListener.event', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=112,
)


_EVENTBUSPUBLISHEVENT = _descriptor.Descriptor(
  name='EventbusPublishEvent',
  full_name='KismetEventBus.EventbusPublishEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_type', full_name='KismetEventBus.EventbusPublishEvent.event_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_content_json', full_name='KismetEventBus.EventbusPublishEvent.event_content_json', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['EventbusEvent'] = _EVENTBUSEVENT
DESCRIPTOR.message_types_by_name['EventbusRegisterListener'] = _EVENTBUSREGISTERLISTENER
DESCRIPTOR.message_types_by_name['EventbusPublishEvent'] = _EVENTBUSPUBLISHEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventbusEvent = _reflection.GeneratedProtocolMessageType('EventbusEvent', (_message.Message,), dict(
  DESCRIPTOR = _EVENTBUSEVENT,
  __module__ = 'eventbus_pb2'
  # @@protoc_insertion_point(class_scope:KismetEventBus.EventbusEvent)
  ))
_sym_db.RegisterMessage(EventbusEvent)

EventbusRegisterListener = _reflection.GeneratedProtocolMessageType('EventbusRegisterListener', (_message.Message,), dict(
  DESCRIPTOR = _EVENTBUSREGISTERLISTENER,
  __module__ = 'eventbus_pb2'
  # @@protoc_insertion_point(class_scope:KismetEventBus.EventbusRegisterListener)
  ))
_sym_db.RegisterMessage(EventbusRegisterListener)

EventbusPublishEvent = _reflection.GeneratedProtocolMessageType('EventbusPublishEvent', (_message.Message,), dict(
  DESCRIPTOR = _EVENTBUSPUBLISHEVENT,
  __module__ = 'eventbus_pb2'
  # @@protoc_insertion_point(class_scope:KismetEventBus.EventbusPublishEvent)
  ))
_sym_db.RegisterMessage(EventbusPublishEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
