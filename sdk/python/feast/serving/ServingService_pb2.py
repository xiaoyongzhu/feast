# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/serving/ServingService.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/serving/ServingService.proto',
  package='feast.serving',
  syntax='proto3',
  serialized_options=b'\n\rfeast.servingB\017ServingAPIProtoZ2github.com/gojek/feast/sdk/go/protos/feast/serving',
  serialized_pb=b'\n\"feast/serving/ServingService.proto\x12\rfeast.serving\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17\x66\x65\x61st/types/Value.proto\"\x1c\n\x1aGetFeastServingInfoRequest\"{\n\x1bGetFeastServingInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.feast.serving.FeastServingType\x12\x1c\n\x14job_staging_location\x18\n \x01(\t\"u\n\x11\x46\x65\x61tureSetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x15\n\rfeature_names\x18\x03 \x03(\t\x12*\n\x07max_age\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x93\x03\n\x18GetOnlineFeaturesRequest\x12\x36\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32 .feast.serving.FeatureSetRequest\x12\x46\n\x0b\x65ntity_rows\x18\x02 \x03(\x0b\x32\x31.feast.serving.GetOnlineFeaturesRequest.EntityRow\x12!\n\x19omit_entities_in_response\x18\x03 \x01(\x08\x1a\xd3\x01\n\tEntityRow\x12\x34\n\x10\x65ntity_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12M\n\x06\x66ields\x18\x02 \x03(\x0b\x32=.feast.serving.GetOnlineFeaturesRequest.EntityRow.FieldsEntry\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.Value:\x02\x38\x01\"\x87\x01\n\x17GetBatchFeaturesRequest\x12\x36\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32 .feast.serving.FeatureSetRequest\x12\x34\n\x0e\x64\x61taset_source\x18\x02 \x01(\x0b\x32\x1c.feast.serving.DatasetSource\"\x8c\x02\n\x19GetOnlineFeaturesResponse\x12J\n\x0c\x66ield_values\x18\x01 \x03(\x0b\x32\x34.feast.serving.GetOnlineFeaturesResponse.FieldValues\x1a\xa2\x01\n\x0b\x46ieldValues\x12P\n\x06\x66ields\x18\x01 \x03(\x0b\x32@.feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.Value:\x02\x38\x01\";\n\x18GetBatchFeaturesResponse\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.feast.serving.Job\"0\n\rGetJobRequest\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.feast.serving.Job\"1\n\x0eGetJobResponse\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.feast.serving.Job\"\xb3\x01\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x04type\x18\x02 \x01(\x0e\x32\x16.feast.serving.JobType\x12(\n\x06status\x18\x03 \x01(\x0e\x32\x18.feast.serving.JobStatus\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\x11\n\tfile_uris\x18\x05 \x03(\t\x12.\n\x0b\x64\x61ta_format\x18\x06 \x01(\x0e\x32\x19.feast.serving.DataFormat\"\xb2\x01\n\rDatasetSource\x12>\n\x0b\x66ile_source\x18\x01 \x01(\x0b\x32\'.feast.serving.DatasetSource.FileSourceH\x00\x1aO\n\nFileSource\x12\x11\n\tfile_uris\x18\x01 \x03(\t\x12.\n\x0b\x64\x61ta_format\x18\x02 \x01(\x0e\x32\x19.feast.serving.DataFormatB\x10\n\x0e\x64\x61taset_source*o\n\x10\x46\x65\x61stServingType\x12\x1e\n\x1a\x46\x45\x41ST_SERVING_TYPE_INVALID\x10\x00\x12\x1d\n\x19\x46\x45\x41ST_SERVING_TYPE_ONLINE\x10\x01\x12\x1c\n\x18\x46\x45\x41ST_SERVING_TYPE_BATCH\x10\x02*6\n\x07JobType\x12\x14\n\x10JOB_TYPE_INVALID\x10\x00\x12\x15\n\x11JOB_TYPE_DOWNLOAD\x10\x01*h\n\tJobStatus\x12\x16\n\x12JOB_STATUS_INVALID\x10\x00\x12\x16\n\x12JOB_STATUS_PENDING\x10\x01\x12\x16\n\x12JOB_STATUS_RUNNING\x10\x02\x12\x13\n\x0fJOB_STATUS_DONE\x10\x03*;\n\nDataFormat\x12\x17\n\x13\x44\x41TA_FORMAT_INVALID\x10\x00\x12\x14\n\x10\x44\x41TA_FORMAT_AVRO\x10\x01\x32\x92\x03\n\x0eServingService\x12l\n\x13GetFeastServingInfo\x12).feast.serving.GetFeastServingInfoRequest\x1a*.feast.serving.GetFeastServingInfoResponse\x12\x66\n\x11GetOnlineFeatures\x12\'.feast.serving.GetOnlineFeaturesRequest\x1a(.feast.serving.GetOnlineFeaturesResponse\x12\x63\n\x10GetBatchFeatures\x12&.feast.serving.GetBatchFeaturesRequest\x1a\'.feast.serving.GetBatchFeaturesResponse\x12\x45\n\x06GetJob\x12\x1c.feast.serving.GetJobRequest\x1a\x1d.feast.serving.GetJobResponseBT\n\rfeast.servingB\x0fServingAPIProtoZ2github.com/gojek/feast/sdk/go/protos/feast/servingb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,feast_dot_types_dot_Value__pb2.DESCRIPTOR,])

_FEASTSERVINGTYPE = _descriptor.EnumDescriptor(
  name='FeastServingType',
  full_name='feast.serving.FeastServingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_ONLINE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_BATCH', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1757,
  serialized_end=1868,
)
_sym_db.RegisterEnumDescriptor(_FEASTSERVINGTYPE)

FeastServingType = enum_type_wrapper.EnumTypeWrapper(_FEASTSERVINGTYPE)
_JOBTYPE = _descriptor.EnumDescriptor(
  name='JobType',
  full_name='feast.serving.JobType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOB_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_TYPE_DOWNLOAD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1870,
  serialized_end=1924,
)
_sym_db.RegisterEnumDescriptor(_JOBTYPE)

JobType = enum_type_wrapper.EnumTypeWrapper(_JOBTYPE)
_JOBSTATUS = _descriptor.EnumDescriptor(
  name='JobStatus',
  full_name='feast.serving.JobStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_DONE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1926,
  serialized_end=2030,
)
_sym_db.RegisterEnumDescriptor(_JOBSTATUS)

JobStatus = enum_type_wrapper.EnumTypeWrapper(_JOBSTATUS)
_DATAFORMAT = _descriptor.EnumDescriptor(
  name='DataFormat',
  full_name='feast.serving.DataFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA_FORMAT_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_FORMAT_AVRO', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2032,
  serialized_end=2091,
)
_sym_db.RegisterEnumDescriptor(_DATAFORMAT)

DataFormat = enum_type_wrapper.EnumTypeWrapper(_DATAFORMAT)
FEAST_SERVING_TYPE_INVALID = 0
FEAST_SERVING_TYPE_ONLINE = 1
FEAST_SERVING_TYPE_BATCH = 2
JOB_TYPE_INVALID = 0
JOB_TYPE_DOWNLOAD = 1
JOB_STATUS_INVALID = 0
JOB_STATUS_PENDING = 1
JOB_STATUS_RUNNING = 2
JOB_STATUS_DONE = 3
DATA_FORMAT_INVALID = 0
DATA_FORMAT_AVRO = 1



_GETFEASTSERVINGINFOREQUEST = _descriptor.Descriptor(
  name='GetFeastServingInfoRequest',
  full_name='feast.serving.GetFeastServingInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=143,
  serialized_end=171,
)


_GETFEASTSERVINGINFORESPONSE = _descriptor.Descriptor(
  name='GetFeastServingInfoResponse',
  full_name='feast.serving.GetFeastServingInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.serving.GetFeastServingInfoResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.serving.GetFeastServingInfoResponse.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_staging_location', full_name='feast.serving.GetFeastServingInfoResponse.job_staging_location', index=2,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=296,
)


_FEATURESETREQUEST = _descriptor.Descriptor(
  name='FeatureSetRequest',
  full_name='feast.serving.FeatureSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.serving.FeatureSetRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.serving.FeatureSetRequest.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_names', full_name='feast.serving.FeatureSetRequest.feature_names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_age', full_name='feast.serving.FeatureSetRequest.max_age', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=415,
)


_GETONLINEFEATURESREQUEST_ENTITYROW_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='feast.serving.GetOnlineFeaturesRequest.EntityRow.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesRequest.EntityRow.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesRequest.EntityRow.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=756,
  serialized_end=821,
)

_GETONLINEFEATURESREQUEST_ENTITYROW = _descriptor.Descriptor(
  name='EntityRow',
  full_name='feast.serving.GetOnlineFeaturesRequest.EntityRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_timestamp', full_name='feast.serving.GetOnlineFeaturesRequest.EntityRow.entity_timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='feast.serving.GetOnlineFeaturesRequest.EntityRow.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESREQUEST_ENTITYROW_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=821,
)

_GETONLINEFEATURESREQUEST = _descriptor.Descriptor(
  name='GetOnlineFeaturesRequest',
  full_name='feast.serving.GetOnlineFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_sets', full_name='feast.serving.GetOnlineFeaturesRequest.feature_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_rows', full_name='feast.serving.GetOnlineFeaturesRequest.entity_rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='omit_entities_in_response', full_name='feast.serving.GetOnlineFeaturesRequest.omit_entities_in_response', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESREQUEST_ENTITYROW, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=821,
)


_GETBATCHFEATURESREQUEST = _descriptor.Descriptor(
  name='GetBatchFeaturesRequest',
  full_name='feast.serving.GetBatchFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_sets', full_name='feast.serving.GetBatchFeaturesRequest.feature_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_source', full_name='feast.serving.GetBatchFeaturesRequest.dataset_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=959,
)


_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=756,
  serialized_end=821,
)

_GETONLINEFEATURESRESPONSE_FIELDVALUES = _descriptor.Descriptor(
  name='FieldValues',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1068,
  serialized_end=1230,
)

_GETONLINEFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetOnlineFeaturesResponse',
  full_name='feast.serving.GetOnlineFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_values', full_name='feast.serving.GetOnlineFeaturesResponse.field_values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESRESPONSE_FIELDVALUES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=962,
  serialized_end=1230,
)


_GETBATCHFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetBatchFeaturesResponse',
  full_name='feast.serving.GetBatchFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='feast.serving.GetBatchFeaturesResponse.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1232,
  serialized_end=1291,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='feast.serving.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='feast.serving.GetJobRequest.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1293,
  serialized_end=1341,
)


_GETJOBRESPONSE = _descriptor.Descriptor(
  name='GetJobResponse',
  full_name='feast.serving.GetJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='feast.serving.GetJobResponse.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1343,
  serialized_end=1392,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='feast.serving.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.serving.Job.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.serving.Job.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='feast.serving.Job.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='feast.serving.Job.error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_uris', full_name='feast.serving.Job.file_uris', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_format', full_name='feast.serving.Job.data_format', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1395,
  serialized_end=1574,
)


_DATASETSOURCE_FILESOURCE = _descriptor.Descriptor(
  name='FileSource',
  full_name='feast.serving.DatasetSource.FileSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_uris', full_name='feast.serving.DatasetSource.FileSource.file_uris', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_format', full_name='feast.serving.DatasetSource.FileSource.data_format', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1658,
  serialized_end=1737,
)

_DATASETSOURCE = _descriptor.Descriptor(
  name='DatasetSource',
  full_name='feast.serving.DatasetSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_source', full_name='feast.serving.DatasetSource.file_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATASETSOURCE_FILESOURCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='dataset_source', full_name='feast.serving.DatasetSource.dataset_source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1577,
  serialized_end=1755,
)

_GETFEASTSERVINGINFORESPONSE.fields_by_name['type'].enum_type = _FEASTSERVINGTYPE
_FEATURESETREQUEST.fields_by_name['max_age'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_GETONLINEFEATURESREQUEST_ENTITYROW_FIELDSENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETONLINEFEATURESREQUEST_ENTITYROW_FIELDSENTRY.containing_type = _GETONLINEFEATURESREQUEST_ENTITYROW
_GETONLINEFEATURESREQUEST_ENTITYROW.fields_by_name['entity_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETONLINEFEATURESREQUEST_ENTITYROW.fields_by_name['fields'].message_type = _GETONLINEFEATURESREQUEST_ENTITYROW_FIELDSENTRY
_GETONLINEFEATURESREQUEST_ENTITYROW.containing_type = _GETONLINEFEATURESREQUEST
_GETONLINEFEATURESREQUEST.fields_by_name['feature_sets'].message_type = _FEATURESETREQUEST
_GETONLINEFEATURESREQUEST.fields_by_name['entity_rows'].message_type = _GETONLINEFEATURESREQUEST_ENTITYROW
_GETBATCHFEATURESREQUEST.fields_by_name['feature_sets'].message_type = _FEATURESETREQUEST
_GETBATCHFEATURESREQUEST.fields_by_name['dataset_source'].message_type = _DATASETSOURCE
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY.containing_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES
_GETONLINEFEATURESRESPONSE_FIELDVALUES.fields_by_name['fields'].message_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY
_GETONLINEFEATURESRESPONSE_FIELDVALUES.containing_type = _GETONLINEFEATURESRESPONSE
_GETONLINEFEATURESRESPONSE.fields_by_name['field_values'].message_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES
_GETBATCHFEATURESRESPONSE.fields_by_name['job'].message_type = _JOB
_GETJOBREQUEST.fields_by_name['job'].message_type = _JOB
_GETJOBRESPONSE.fields_by_name['job'].message_type = _JOB
_JOB.fields_by_name['type'].enum_type = _JOBTYPE
_JOB.fields_by_name['status'].enum_type = _JOBSTATUS
_JOB.fields_by_name['data_format'].enum_type = _DATAFORMAT
_DATASETSOURCE_FILESOURCE.fields_by_name['data_format'].enum_type = _DATAFORMAT
_DATASETSOURCE_FILESOURCE.containing_type = _DATASETSOURCE
_DATASETSOURCE.fields_by_name['file_source'].message_type = _DATASETSOURCE_FILESOURCE
_DATASETSOURCE.oneofs_by_name['dataset_source'].fields.append(
  _DATASETSOURCE.fields_by_name['file_source'])
_DATASETSOURCE.fields_by_name['file_source'].containing_oneof = _DATASETSOURCE.oneofs_by_name['dataset_source']
DESCRIPTOR.message_types_by_name['GetFeastServingInfoRequest'] = _GETFEASTSERVINGINFOREQUEST
DESCRIPTOR.message_types_by_name['GetFeastServingInfoResponse'] = _GETFEASTSERVINGINFORESPONSE
DESCRIPTOR.message_types_by_name['FeatureSetRequest'] = _FEATURESETREQUEST
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesRequest'] = _GETONLINEFEATURESREQUEST
DESCRIPTOR.message_types_by_name['GetBatchFeaturesRequest'] = _GETBATCHFEATURESREQUEST
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesResponse'] = _GETONLINEFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetBatchFeaturesResponse'] = _GETBATCHFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobResponse'] = _GETJOBRESPONSE
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['DatasetSource'] = _DATASETSOURCE
DESCRIPTOR.enum_types_by_name['FeastServingType'] = _FEASTSERVINGTYPE
DESCRIPTOR.enum_types_by_name['JobType'] = _JOBTYPE
DESCRIPTOR.enum_types_by_name['JobStatus'] = _JOBSTATUS
DESCRIPTOR.enum_types_by_name['DataFormat'] = _DATAFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeastServingInfoRequest = _reflection.GeneratedProtocolMessageType('GetFeastServingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGINFOREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingInfoRequest)
  })
_sym_db.RegisterMessage(GetFeastServingInfoRequest)

GetFeastServingInfoResponse = _reflection.GeneratedProtocolMessageType('GetFeastServingInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGINFORESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingInfoResponse)
  })
_sym_db.RegisterMessage(GetFeastServingInfoResponse)

FeatureSetRequest = _reflection.GeneratedProtocolMessageType('FeatureSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.FeatureSetRequest)
  })
_sym_db.RegisterMessage(FeatureSetRequest)

GetOnlineFeaturesRequest = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesRequest', (_message.Message,), {

  'EntityRow' : _reflection.GeneratedProtocolMessageType('EntityRow', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETONLINEFEATURESREQUEST_ENTITYROW_FIELDSENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequest.EntityRow.FieldsEntry)
      })
    ,
    'DESCRIPTOR' : _GETONLINEFEATURESREQUEST_ENTITYROW,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequest.EntityRow)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequest)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesRequest)
_sym_db.RegisterMessage(GetOnlineFeaturesRequest.EntityRow)
_sym_db.RegisterMessage(GetOnlineFeaturesRequest.EntityRow.FieldsEntry)

GetBatchFeaturesRequest = _reflection.GeneratedProtocolMessageType('GetBatchFeaturesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBATCHFEATURESREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetBatchFeaturesRequest)
  })
_sym_db.RegisterMessage(GetBatchFeaturesRequest)

GetOnlineFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesResponse', (_message.Message,), {

  'FieldValues' : _reflection.GeneratedProtocolMessageType('FieldValues', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry)
      })
    ,
    'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FIELDVALUES,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FieldValues)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesResponse)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FieldValues)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FieldValues.FieldsEntry)

GetBatchFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetBatchFeaturesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBATCHFEATURESRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetBatchFeaturesResponse)
  })
_sym_db.RegisterMessage(GetBatchFeaturesResponse)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

GetJobResponse = _reflection.GeneratedProtocolMessageType('GetJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetJobResponse)
  })
_sym_db.RegisterMessage(GetJobResponse)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.Job)
  })
_sym_db.RegisterMessage(Job)

DatasetSource = _reflection.GeneratedProtocolMessageType('DatasetSource', (_message.Message,), {

  'FileSource' : _reflection.GeneratedProtocolMessageType('FileSource', (_message.Message,), {
    'DESCRIPTOR' : _DATASETSOURCE_FILESOURCE,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.DatasetSource.FileSource)
    })
  ,
  'DESCRIPTOR' : _DATASETSOURCE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.DatasetSource)
  })
_sym_db.RegisterMessage(DatasetSource)
_sym_db.RegisterMessage(DatasetSource.FileSource)


DESCRIPTOR._options = None
_GETONLINEFEATURESREQUEST_ENTITYROW_FIELDSENTRY._options = None
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY._options = None

_SERVINGSERVICE = _descriptor.ServiceDescriptor(
  name='ServingService',
  full_name='feast.serving.ServingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2094,
  serialized_end=2496,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeastServingInfo',
    full_name='feast.serving.ServingService.GetFeastServingInfo',
    index=0,
    containing_service=None,
    input_type=_GETFEASTSERVINGINFOREQUEST,
    output_type=_GETFEASTSERVINGINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetOnlineFeatures',
    full_name='feast.serving.ServingService.GetOnlineFeatures',
    index=1,
    containing_service=None,
    input_type=_GETONLINEFEATURESREQUEST,
    output_type=_GETONLINEFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBatchFeatures',
    full_name='feast.serving.ServingService.GetBatchFeatures',
    index=2,
    containing_service=None,
    input_type=_GETBATCHFEATURESREQUEST,
    output_type=_GETBATCHFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='feast.serving.ServingService.GetJob',
    index=3,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_GETJOBRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVINGSERVICE)

DESCRIPTOR.services_by_name['ServingService'] = _SERVINGSERVICE

# @@protoc_insertion_point(module_scope)
