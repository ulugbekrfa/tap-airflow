import os


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


# def construct_schema(config):
#     client = Client(config)
#
#     endpoint = "/api/rest/v4/schema/entrytypes?"
#     response = client._get_response(method='get', endpoint=endpoint)
#
#     entrytypes = response.json()
#     streams_dict = {}
#     for entry in entrytypes:
#         endpoint = "/api/rest/v4/schema/entrytypes/{}/fields?".format(
#             entry["apiName"])
#         response = client._get_response(method='get', endpoint=endpoint)
#         fields = response.json()
#         json_schema = {"type": "object", "properties": {}}
#
#         table_name = entry["apiName"]
#         streams_dict[table_name] = {}
#         streams_dict[table_name]['key_properties'] = [
#             entry['name'] + '__ID']
#         streams_dict[table_name]['replication_method'] = 'INCREMENTAL'
#         streams_dict[table_name]['nested_entities'] = {}
#
#         for field in fields:
#             field_name = field['apiName']
#             field_type = field['fieldType']
#             is_money = field['isMoney']
#             system_field_type = field['systemFieldType']
#             if (field_type == 1 and system_field_type == 9) or (field_type in [5, 2, 7]) or (field_type == 3 and is_money is True):
#                 json_schema["properties"].update(
#                     {entry['name'] + '__ID': {"type": "integer"}})
#
#                 json_schema["properties"][field_name] = {}
#                 json_schema["properties"][field_name]["type"] = [
#                     "null", "object", "array"]
#             elif field_type == 3 and is_money is None:
#                 json_schema["properties"][field_name] = {}
#                 json_schema["properties"][field_name]["type"] = [
#                     "null", "number"]
#             elif field_type == 6:
#                 json_schema["properties"][field_name] = {}
#                 json_schema["properties"][field_name]["type"] = [
#                     "null", "boolean"]
#             else:
#                 json_schema["properties"][field_name] = {}
#                 json_schema["properties"][field_name]["type"] = [
#                     "null", "string"]
#
#         file_path = get_abs_path("schemas/{}.json".format(entry["apiName"]))
#
#         with open(file_path, 'w') as file:
#             json.dump(json_schema, file)
#
#     stream_path = get_abs_path("streams.py")
#     with open(stream_path, "w") as streams_file:
#         streams_file.write("STREAMS = {}".format(
#             json.dumps(streams_dict, indent=3)))
