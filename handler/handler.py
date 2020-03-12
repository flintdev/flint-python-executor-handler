from .flow_data import FlowData
from .model import Model


class Handler:
    def __init__(self):
        self.flow_data = FlowData()
        self.model = Model()

