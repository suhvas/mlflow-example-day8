import mlflow.sagemaker
from mlflow.deployments import get_deploy_client

endpoint_name="prod-endpoint"
model_uri="s3://sv-mlflow-project-artifact-2024-26-10/2/2ca0ed2475074138a6a9c158ca12b1b0/artifacts/mymodel"




# Define your configuration parameters as a dictionary
config = {
    "execution_role_arn": "arn:aws:iam::975049980106:role/housing-price-role",
    "bucket_name": "sv-mlflow-project-artifact-2024-26-10",
    "image_url": "975049980106.dkr.ecr.ap-south-1.amazonaws.com/basic_elastic_net:2.17.0",
    "region_name": "ap-south-1",
    "archive": False,
    "instance_type": "ml.t2.medium",
    "instance_count": 1,
    "synchronous": True
}

# Initialize a deployment client for SageMaker
client = get_deploy_client("sagemaker")

# Create the deployment
client.create_deployment(
    name=endpoint_name,
    model_uri=model_uri,
    flavor="python_function",
    config=config,
)


