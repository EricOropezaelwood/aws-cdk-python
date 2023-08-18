from aws_cdk import core

# Create a new CDK project
app = core.App()

# Create an Amazon S3 bucket
bucket = core.Stack(app, "MyBucket", aws_cdk.aws_s3.Bucket(bucket_name="my-bucket"))

# Deploy the stack
app.synth()
