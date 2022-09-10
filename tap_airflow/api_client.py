import requests
from requests.auth import HTTPBasicAuth
import json
import singer
LOGGER = singer.get_logger()


class ApiClient:
    def __init__(self, config):
        self.host = config['host']
        self.username = config['username']
        self.password = config['password']

    def get_dag_list(self):
        response = requests.get(f'{self.host}/dags', auth=HTTPBasicAuth(self.username, self.password))
        json_response = json.loads(response.text)
        return json_response['dags']

    def get_dag_info(self, dag_id):
        response = requests.get(f'{self.host}/dags/{dag_id}/dagRuns', auth=HTTPBasicAuth(self.username, self.password))
        json_response = json.loads(response.text)
        return json_response['dag_runs']
        # # Create an instance of the API class
        # api_instance = dag_run_api.DAGRunApi(self.api_client)
        #
        # # example passing only required values which don't have defaults set
        # try:
        #     # List DAG runs
        #     api_response = api_instance.get_dag_runs(dag_id)
        #     dag_list = []
        #     LOGGER.info(api_response['dag_runs'][0])
        #     LOGGER.info(type(api_response['dag_runs']))
        #     LOGGER.info(type(api_response['dag_runs'][0]))
        #     k = json.dumps(api_response['dag_runs'][0])
        #     LOGGER.info(type(k))
        #     LOGGER.info(k)
        #     for dag in api_response['dag_runs']:
        #         dag_dict = {}
        #         for key in dag:
        #             if key == 'end_date':
        #                 value = json.dumps(dag[key], default=str)
        #             elif key == 'execution_date':
        #                 value = json.dumps(dag[key], default=str)
        #             elif key == 'logical_date':
        #                 value = json.dumps(dag[key], default=str)
        #             elif key == 'start_date':
        #                 value = json.dumps(dag[key], default=str)
        #             else:
        #                 value = dag[key]
        #             dag_dict[key] = value
        #         dag_list.append(dag_dict)
        #     return dag_list
        # except airflow_client.client.ApiException as e:
        #     print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)