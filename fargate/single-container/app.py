from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class MyFargateAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC with 2 Availability Zones
        vpc = ec2.Vpc(self, "sc-vpc", max_azs=2)

        # Create an ECS Cluster in the VPC
        cluster = ecs.Cluster(self, "sc-cluster", vpc=vpc)

        # Create a Fargate service with a load balancer
        ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "sc-fargate-service",
            cluster=cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=2,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("nginx"),
            ),
            public_load_balancer=True,
        )
