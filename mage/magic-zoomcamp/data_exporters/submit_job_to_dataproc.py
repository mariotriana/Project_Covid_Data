import os
from google.oauth2 import service_account
from google.cloud import dataproc_v1 as dataproc
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/my-creds.json"
credentials = service_account.Credentials.from_service_account_file("/home/src/my-creds.json")

PROJECT_ID="weighty-elf-412403"
REGION="us-east1"
CLUSTER_NAME="covid-data-cluster"
PYSPARK_FILE="gs://covid-data-project-bucket/spark_sql_project.py"
EXTRA_ARGS=["--input=gs://covid-data-project-bucket/covid_data.parquet" , "--output=gs://covid-data-project-bucket/output-data"]
BUCKET_NAME="covid-data-project-bucket" 


@data_exporter 
def submit_pyspark_job(hello):
    # Create a client with the given project and region
    client = dataproc.JobControllerClient(client_options={"api_endpoint": f"{REGION}-dataproc.googleapis.com:443"})
    
    # Create a PySpark job
    job = {
        "placement": {"cluster_name": CLUSTER_NAME},
        "pyspark_job": {
            "main_python_file_uri":PYSPARK_FILE,
            "args": EXTRA_ARGS
        }
    }

    # Submit the job
    operation = client.submit_job_as_operation(project_id=PROJECT_ID, region=REGION, job=job)
    response = operation.result()
  