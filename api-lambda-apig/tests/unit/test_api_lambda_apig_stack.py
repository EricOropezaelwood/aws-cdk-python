import aws_cdk as core
import aws_cdk.assertions as assertions

from api_lambda_apig.api_lambda_apig_stack import ApiLambdaApigStack

# example tests. To run these tests, uncomment this file along with the example
# resource in api_lambda_apig/api_lambda_apig_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApiLambdaApigStack(app, "api-lambda-apig")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
