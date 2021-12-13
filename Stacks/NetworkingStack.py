from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)

class NetworkingStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "MyVPC",
            cidr="10.0.0.0/16"
        )
        