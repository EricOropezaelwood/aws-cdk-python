from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


class Ec2Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a new VPC
        vpc = ec2.Vpc(
            self,
            "VPC-01",
            max_azs=3,  # Number of Availability Zones
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="subnet-01", subnet_type=ec2.SubnetType.PUBLIC
                ),
                # Add more subnet configurations as needed (e.g., PrivateSubnet)
            ],
        )

        # Create a security group that allows incoming SSH traffic on port 22
        ssh_security_group = ec2.SecurityGroup(
            self,
            "sg-01",
            vpc=vpc,
            allow_all_outbound=True,  # Allow all outbound traffic
        )
        ssh_security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH access"
        )

        # Create an EC2 instance
        ec2_instance = ec2.Instance(
            self,
            "ubuntu-01",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,  # Attach the instance to the VPC
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),  # Use public subnet
            key_name="eric-dev-key",  # Associate the key pair with the EC2 instance
            security_group=ssh_security_group,  # Associate the SSH security group
        )

        # Optionally, you can add security groups, IAM roles, etc. to the EC2 instance here.
