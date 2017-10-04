# Copyright 2016 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A gRPC server servicing Products RPCs."""

from concurrent import futures

import time
import grpc

import products_pb2
import products_pb2_grpc
import products_resources

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def _get_record(products_db, id):
  """Returns Record for a specific order id or None."""
  for record in products_db:
    if record.id.oid  == id.oid:
      return record
  return None

class _ProductsServicer(products_pb2_grpc.ProductsServicer):
  """Provides methods that implement functionality of products server."""

  def __init__(self):
    self.db = products_resources.read_products_database()

  def GetRecord(self, request, context):
    record = _get_record(self.db, request)
    if record is None:
      return products_pb2.Record(product_name ="", id = request)
    else:
      return record

  def ListRecords(self, request, context):
    start = request.start_oid.oid
    end = request.end_oid.oid
    for record in self.db:
        if(record.id.oid >= start and
           record.id.oid <= end):
           yield record

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  products_pb2_grpc.add_ProductsServicer_to_server(
      _ProductsServicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
