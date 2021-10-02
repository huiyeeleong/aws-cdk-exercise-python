from aws_cdk import core as cdk
from aws_cdk import (
    core,
    aws_s3 as _s3,
    
)
from aws_cdk import core as cdk

class S3LifeCycleStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #Create s3 bucket with lifecycle rules
        hui_bucket = _s3.Bucket(
            self,
            "HuiBucketID",
            versioned=True,
            removal_policy=core.RemovalPolicy.DESTROY,
            )
        
        s3_life_cycle = _s3.LifecycleRule(
            expiration = 365,
            transitions = _s3.Transition(
                storage_class = _s3.StorageClass.INFREQUENT_ACCESS,
                transition_after= 90
            )
        )
        


