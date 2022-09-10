import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.api import dag_run_api
import json
import singer
LOGGER = singer.get_logger()


class ApiClient:
    def __init__(self, config):
        self.configuration = airflow_client.client.Configuration(
            host=config['host'],
            username=config['username'],
            password=config['password']
        )
        self.api_client = airflow_client.client.ApiClient(self.configuration)

    def get_dag_list(self):
        api_instance = dag_api.DAGApi(self.api_client)
        try:
            # List DAGs
            api_response = api_instance.get_dags()
            return api_response['dags']
        except airflow_client.client.ApiException as e:
            print("Exception when calling DAGApi->get_dags: %s\n" % e)

    def get_dag_info(self, dag_id):
        # Create an instance of the API class
        api_instance = dag_run_api.DAGRunApi(self.api_client)

        # example passing only required values which don't have defaults set
        try:
            # List DAG runs
            api_response = api_instance.get_dag_runs(dag_id)
            dag_list = []
            LOGGER.info(api_response['dag_runs'][0])
            for dag in api_response['dag_runs']:
                dag_dict = {}
                for key in dag:
                    if key == 'end_date':
                        value = json.dumps(dag[key], default=str)
                    elif key == 'execution_date':
                        value = json.dumps(dag[key], default=str)
                    elif key == 'logical_date':
                        value = json.dumps(dag[key], default=str)
                    elif key == 'start_date':
                        value = json.dumps(dag[key], default=str)
                    else:
                        value = dag[key]
                    dag_dict[key] = value
                dag_list.append(dag_dict)
            return dag_list
        except airflow_client.client.ApiException as e:
            print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)