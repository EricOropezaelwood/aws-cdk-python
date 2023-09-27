from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct


class ApiLambdaApigStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function
        my_lambda = _lambda.Function(
            self, 'api-function',
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler='handler.my_handler',
            code=_lambda.Code.from_asset('lambda_code')
        )

        # Define the API Gateway
        api = apigw.RestApi(
            self, 'stats-api',
            rest_api_name='NFL stats API',
            description='Statistics from the NFL'
        )

        # Create a resource and method
        get_resource = api.root.add_resource('api-resource')
        get_method = get_resource.add_method(
            'GET',
            apigw.LambdaIntegration(my_lambda)
        )

