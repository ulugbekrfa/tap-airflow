# tap-airflow

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

The tap is developed to get data from Airflow REST API.

Current tap fetches data from the endpoint /dags/{dag_id}/dagRuns.  

## How to run
1. Creating and activating virtual environment:
    
        python3 -m venv ~/.virtualenvs/tap-airflow
        source ~/.virtualenvs/tap-airflow/bin/activate

2. Installation:

        git clone https://github.com/RFAInc/tap-airflow.git
        cd tap-airflow
        python install setup.py
        deactivate

   1. Client configuration:
    ```
      {
        "host": "http://localhost:8080/api/v1",
        "username": "username",
        "password": "password",
        "selected_all": true
      }
    ```
       > Note: here <b>batch</b> is a limit for paging which supports upto <b>10000</b> records per request
       > Note: if <b>sync_tables</b> is not specified, then the tap will fetch data for all tables

3. Running
    
    * Run in discovery mode (for generating schemas and catalog)

            ~/.virtualenvs/tap-airflow/bin/tap-airflow --config client_config.json --discover > catalog.json

    * Run for full sync (for initial run):

            ~/.virtualenvs/tap-airflow/bin/tap-airflow --config client_config.json --catalog catalog.json

    * Run with state (for further run):

            ~/.virtualenvs/tap-airflow/bin/tap-airflow --config client_config.json --catalog catalog.json --state state.json
    
