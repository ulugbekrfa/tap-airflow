#!/usr/bin/env python3

import sys
import json
import singer
from tap_airflow.discover import discover
from tap_airflow.sync import sync

LOGGER = singer.get_logger()

REQUIRED_CONFIG_KEYS = [
    'host',
    'username',
    'password'
]


def do_discover(config):
    LOGGER.info('Starting discover')
    catalog = discover(config)
    json.dump(catalog.to_dict(), sys.stdout, indent=2, ensure_ascii=False)
    LOGGER.info('Finished discover')


@singer.utils.handle_top_exception(LOGGER)
def main():
    parsed_args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)
    state = {}
    if parsed_args.state:
        state = parsed_args.state
    if parsed_args.discover:
        do_discover(parsed_args.config)
    elif parsed_args.catalog:
        sync(config=parsed_args.config, catalog=parsed_args.catalog, state=state)


if __name__ == '__main__':
    main()
