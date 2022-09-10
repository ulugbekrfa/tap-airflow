from tap_airflow.schema import get_abs_path
from tap_airflow import streams
import json
from singer.catalog import Catalog, CatalogEntry
from singer.schema import Schema
from singer import metadata


def get_schemas(config, streams):
    schemas = {}
    field_metadata = {}
    selected_all = config.get("selected_all", False)

    for stream_name, stream_metadata in streams.items():
        schema_name = stream_name.replace(' ', '')
        schema_path = get_abs_path("schemas/{}.json".format(schema_name))
        with open(schema_path, encoding="utf8") as file:
            schema = json.load(file)
        schemas[stream_name] = schema
        mdata = metadata.new()
        mdata = metadata.get_standard_metadata(
            schema=schema,
            key_properties=stream_metadata.get("key_properties", None),
            valid_replication_keys=stream_metadata.get(
                "replication_keys", None),
            replication_method=stream_metadata.get("replication_method", None),
        )
        if selected_all:
            for m in mdata:
                m["metadata"]["selected"] = True
        field_metadata[stream_name] = {}
        field_metadata[stream_name]["mdata"] = mdata
        field_metadata[stream_name]["key_properties"] = stream_metadata.get(
            "key_properties", None
        )
    return schemas, field_metadata


def discover(config):
    schemas, field_metadata = get_schemas(config, streams.STREAMS)
    catalog = Catalog([])

    for stream_name, schema_dict in schemas.items():
        schema = Schema.from_dict(schema_dict)
        mdata = field_metadata[stream_name]['mdata']

        catalog.streams.append(CatalogEntry(
            stream=stream_name,
            tap_stream_id=stream_name,
            key_properties=streams.STREAMS[stream_name]['key_properties'],
            schema=schema,
            metadata=mdata
        ))

    return catalog
