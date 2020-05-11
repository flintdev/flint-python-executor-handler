from kubernetes import client, config
import json
from kubernetes.client.rest import ApiException

config.load_kube_config()
api = client.CustomObjectsApi()


class Model:
    def __init__(self):
        self.obj_name = ""
        self.group = ""
        self.version = ""
        self.namespace = ""
        self.plural = ""
