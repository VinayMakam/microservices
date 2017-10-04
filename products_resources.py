# Copyright 2015 gRPC authors.
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

"""Common resources used in the gRPC products example."""

import json

import products_pb2

def read_products_database():
  """Reads the products database.

  Returns:
    The full contents of the products database as a sequence of
      products_pb2.Record.
  """
  record_list = []
  with open("products.json") as products_db_file:
    for item in json.load(products_db_file):
      record = products_pb2.Record(
          product_name=item["product_name"],
          supplier=item["supplier"],
          quantity=item["quantity"],
          unit_cost=item["unit_cost"],
          id=products_pb2.Id(oid=item["_id"]["$oid"]))
      record_list.append(record)
  return record_list
