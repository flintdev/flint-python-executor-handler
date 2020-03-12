from kubernetes import client, config
import json
from kubernetes.client.rest import ApiException
from pprint import pprint

GROUP = 'flint.flint.com'
VERSION = 'v1'
NAMESPACE = 'default'
PLURAL = 'workflows'

config.load_kube_config()
api = client.CustomObjectsApi()


class FlowData:
    def __init__(self):
        self.obj_name = ""

    def get(self, path):
        path = parse_path(path)
        try:
            obj = api.get_namespaced_custom_object(GROUP, VERSION, NAMESPACE, PLURAL, self.obj_name)
            pprint(obj)
            flow_data = json.loads(obj["spec"]["flowData"])
            if not path:
                return flow_data
            return flow_data[path]
        except ApiException as e:
            print("Exception when calling CustomObjectsApi->get_namespaced_custom_object: %s\n" % e)
            return None

    def set(self, path, value):
        obj = api.get_namespaced_custom_object(GROUP, VERSION, NAMESPACE, PLURAL, self.obj_name)
        path = parse_path(path)
        flow_data = json.loads(obj["spec"]["flowData"])
        if not path:
            obj["spec"]["flowData"] = json.dumps(value)
        else:
            flow_data[path] = value
            obj["spec"]["flowData"] = json.dumps(flow_data)
        try:
            obj = api.patch_namespaced_custom_object(GROUP, VERSION, NAMESPACE, PLURAL, self.obj_name, obj)
            pprint(obj)
        except ApiException as e:
            print("Exception when calling CustomObjectsApi->patch_namespaced_custom_object: %s\n" % e)
            return None


def parse_path(path):
    path = path.split(".")
    if path[0] == "$":
        path = path[1:]
    return ".".join(path)
