from airflow.hooks.http_hook import HttpHook
import json

class IngestionApiHook(HttpHook):
    def __init__(self, http_conn_id, method='GET'):
        super().__init__(method=method, http_conn_id=http_conn_id)

    def run(self, endpoint, data=None, headers=None):
        self.method = self.method.upper()
        if self.method == 'POST' and data:
            response = super().run(
                endpoint,
                data=json.dumps(data),
                headers=headers
                )
            return response.json()
        else:
            response = super().run(
                endpoint,
                headers=headers)
            return response.json()