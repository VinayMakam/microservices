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

"""A client that makes Products RPCs."""

from __future__ import print_function

import grpc

import products_pb2
import products_pb2_grpc
import products_resources


def get_one_record(products_stub, Id):
  record = products_stub.GetRecord(Id)
  if not record.id:
    print("Server returned incomplete product information.")
    return

  if record.id:
      print("Record:\n %s %s, %s, %d, %s" %  (
                                        record.id,
                                        record.product_name,
                                        record.supplier,
                                        record.quantity,
                                        record.unit_cost))
  else:
    print("Found no feature at %s" % record.id)


def get_record(products_stub):
  get_one_record(
      products_stub,
      products_pb2.Id(oid="5968dd23fc13ae04d9000003"))


def list_records(products_stub):
  allrecords = products_pb2.AllRecords(
      start_oid = products_pb2.Id(oid = "5968dd23fc13ae04d9000001"),
      end_oid = products_pb2.Id(oid = "5968dd23fc13ae04d9000005"))

  records = products_stub.ListRecords(allrecords)

  for record in records:
    print("Record:\n %s %s, %s, %d, %s" %  (
                                          record.id,
                                          record.product_name,
                                          record.supplier,
                                          record.quantity,
                                          record.unit_cost))


def run():
  channel = grpc.insecure_channel('localhost:50051')
  products_stub = products_pb2_grpc.ProductsStub(channel)

  print("\n--GetRecord----------------------------------------------------")
  get_record(products_stub)

  print("\n--ListRecords--------------------------------------------------")
  list_records(products_stub)


if __name__ == '__main__':
  run()
