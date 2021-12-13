from constructs import Construct
from aws_cdk import (
    Stage
)
from .NetworkingStack import NetworkingStack

class NetworkingStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = NetworkingStack(self, 'Networking')