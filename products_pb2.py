# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='products.proto',
  package='product',
  syntax='proto3',
  serialized_pb=_b('\n\x0eproducts.proto\x12\x07product\"\x11\n\x02Id\x12\x0b\n\x03oid\x18\x01 \x01(\t\"n\n\x06Record\x12\x14\n\x0cproduct_name\x18\x01 \x01(\t\x12\x10\n\x08supplier\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x11\n\tunit_cost\x18\x04 \x01(\t\x12\x17\n\x02id\x18\x05 \x01(\x0b\x32\x0b.product.Id\"J\n\nAllRecords\x12\x1e\n\tstart_oid\x18\x01 \x01(\x0b\x32\x0b.product.Id\x12\x1c\n\x07\x65nd_oid\x18\x02 \x01(\x0b\x32\x0b.product.Id2p\n\x08Products\x12+\n\tGetRecord\x12\x0b.product.Id\x1a\x0f.product.Record\"\x00\x12\x37\n\x0bListRecords\x12\x13.product.AllRecords\x1a\x0f.product.Record\"\x00\x30\x01\x42)\n\x10io.grpc.ProductsB\rProductsProtoP\x01\xa2\x02\x03PRDb\x06proto3')
)




_ID = _descriptor.Descriptor(
  name='Id',
  full_name='product.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='product.Id.oid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=44,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='product.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_name', full_name='product.Record.product_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier', full_name='product.Record.supplier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='product.Record.quantity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_cost', full_name='product.Record.unit_cost', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='product.Record.id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=156,
)


_ALLRECORDS = _descriptor.Descriptor(
  name='AllRecords',
  full_name='product.AllRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_oid', full_name='product.AllRecords.start_oid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_oid', full_name='product.AllRecords.end_oid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=232,
)

_RECORD.fields_by_name['id'].message_type = _ID
_ALLRECORDS.fields_by_name['start_oid'].message_type = _ID
_ALLRECORDS.fields_by_name['end_oid'].message_type = _ID
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['AllRecords'] = _ALLRECORDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), dict(
  DESCRIPTOR = _ID,
  __module__ = 'products_pb2'
  # @@protoc_insertion_point(class_scope:product.Id)
  ))
_sym_db.RegisterMessage(Id)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'products_pb2'
  # @@protoc_insertion_point(class_scope:product.Record)
  ))
_sym_db.RegisterMessage(Record)

AllRecords = _reflection.GeneratedProtocolMessageType('AllRecords', (_message.Message,), dict(
  DESCRIPTOR = _ALLRECORDS,
  __module__ = 'products_pb2'
  # @@protoc_insertion_point(class_scope:product.AllRecords)
  ))
_sym_db.RegisterMessage(AllRecords)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020io.grpc.ProductsB\rProductsProtoP\001\242\002\003PRD'))

_PRODUCTS = _descriptor.ServiceDescriptor(
  name='Products',
  full_name='product.Products',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=234,
  serialized_end=346,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRecord',
    full_name='product.Products.GetRecord',
    index=0,
    containing_service=None,
    input_type=_ID,
    output_type=_RECORD,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListRecords',
    full_name='product.Products.ListRecords',
    index=1,
    containing_service=None,
    input_type=_ALLRECORDS,
    output_type=_RECORD,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTS)

DESCRIPTOR.services_by_name['Products'] = _PRODUCTS

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class ProductsStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetRecord = channel.unary_unary(
          '/product.Products/GetRecord',
          request_serializer=Id.SerializeToString,
          response_deserializer=Record.FromString,
          )
      self.ListRecords = channel.unary_stream(
          '/product.Products/ListRecords',
          request_serializer=AllRecords.SerializeToString,
          response_deserializer=Record.FromString,
          )


  class ProductsServicer(object):
    """Interface exported by the server.
    """

    def GetRecord(self, request, context):
      """A simple RPC.                                                              
      Obtains the record at a given position.
      A Record with an empty info is returned if there's no record found in db.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ListRecords(self, request, context):
      """A server-to-client streaming RPC.                                       

      Obtains the Records available within the given criteria.  Results are 
      streamed rather than returned at once (e.g. in a response message with a
      repeated field).                                                
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_ProductsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetRecord': grpc.unary_unary_rpc_method_handler(
            servicer.GetRecord,
            request_deserializer=Id.FromString,
            response_serializer=Record.SerializeToString,
        ),
        'ListRecords': grpc.unary_stream_rpc_method_handler(
            servicer.ListRecords,
            request_deserializer=AllRecords.FromString,
            response_serializer=Record.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'product.Products', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaProductsServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Interface exported by the server.
    """
    def GetRecord(self, request, context):
      """A simple RPC.                                                              
      Obtains the record at a given position.
      A Record with an empty info is returned if there's no record found in db.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ListRecords(self, request, context):
      """A server-to-client streaming RPC.                                       

      Obtains the Records available within the given criteria.  Results are 
      streamed rather than returned at once (e.g. in a response message with a
      repeated field).                                                
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaProductsStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Interface exported by the server.
    """
    def GetRecord(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """A simple RPC.                                                              
      Obtains the record at a given position.
      A Record with an empty info is returned if there's no record found in db.
      """
      raise NotImplementedError()
    GetRecord.future = None
    def ListRecords(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """A server-to-client streaming RPC.                                       

      Obtains the Records available within the given criteria.  Results are 
      streamed rather than returned at once (e.g. in a response message with a
      repeated field).                                                
      """
      raise NotImplementedError()


  def beta_create_Products_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('product.Products', 'GetRecord'): Id.FromString,
      ('product.Products', 'ListRecords'): AllRecords.FromString,
    }
    response_serializers = {
      ('product.Products', 'GetRecord'): Record.SerializeToString,
      ('product.Products', 'ListRecords'): Record.SerializeToString,
    }
    method_implementations = {
      ('product.Products', 'GetRecord'): face_utilities.unary_unary_inline(servicer.GetRecord),
      ('product.Products', 'ListRecords'): face_utilities.unary_stream_inline(servicer.ListRecords),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Products_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('product.Products', 'GetRecord'): Id.SerializeToString,
      ('product.Products', 'ListRecords'): AllRecords.SerializeToString,
    }
    response_deserializers = {
      ('product.Products', 'GetRecord'): Record.FromString,
      ('product.Products', 'ListRecords'): Record.FromString,
    }
    cardinalities = {
      'GetRecord': cardinality.Cardinality.UNARY_UNARY,
      'ListRecords': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'product.Products', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)