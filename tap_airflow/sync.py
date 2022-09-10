from tap_airflow.api_client import ApiClient
from datetime import datetime
from tap_airflow import streams
import singer

LOGGER = singer.get_logger()


def write_state(state, last_sync_at):
    state['last_sync_at'] = last_sync_at.strftime('%Y-%m-%dT%H:%M:%S')
    try:
        singer.write_state(state)
    except OSError as err:
        LOGGER.info('Error in writing state')
        raise err


def write_schema(catalog, stream_name):
    stream = catalog.get_stream(stream_name)
    schema = stream.schema.to_dict()
    try:
        singer.write_schema(stream_name, schema, stream.key_properties)
    except OSError as err:
        LOGGER.info('OS Error writing schema for: {}'.format(stream_name))
        raise err


def write_records(stream_name, records):
    try:
        singer.messages.write_records(stream_name, records)
    except OSError as err:
        LOGGER.info('OS Error writing record for: {}'.format(stream_name))
        LOGGER.info('record: {}'.format(records))
        raise err
    except TypeError as err:
        LOGGER.info('Type Error writing record for: {}'.format(stream_name))
        LOGGER.info('record: {}'.format(records))
        raise err
    except UnicodeDecodeError as err:
        raise err


def sync(config, state, catalog):
    last_sync_at = datetime.utcnow()
    api_client = ApiClient(config)
    for stream_name, _ in streams.STREAMS.items():
        records = []
        dag_list = api_client.get_dag_list()
        for dag in dag_list:
            LOGGER.info(f"Fetching data for dag_id: {dag['dag_id']}")
            records += api_client.get_dag_info(dag['dag_id'])
        write_schema(catalog, stream_name)
        write_records(stream_name, records)
    write_state(state, last_sync_at)
