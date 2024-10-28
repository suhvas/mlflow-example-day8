import mlflow

experiment_name = "Basic"
entry_point = "main"

mlflow.set_tracking_uri("http://ec2-13-200-253-50.ap-south-1.compute.amazonaws.com:5000/")

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    experiment_name=experiment_name,
    env_manager="conda"
    #parameters={"alpha": 0.1, "l1_ratio": 0.1}
)