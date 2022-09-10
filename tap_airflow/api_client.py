import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.api import dag_run_api


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
            return api_response['dag_runs']
        except airflow_client.client.ApiException as e:
            print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)