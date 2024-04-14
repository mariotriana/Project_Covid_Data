# Project_Covid_Data

## Problem description
Covid-19 pandemic was the most serious health crisis we have suffered in the last time globally. The unexpected spread and consequences of the virus crated an urgent need for data to track its evolution, understand how covid numbers changes to formulate effective countermeasures. In this project I selected a raw dataset from World Health Organization (WHO) which contains Covid Data since 2020 until March of the current year. Data were processed, transformed and partitioned to make easier and more understandable its interpretation for everyone who is interested in it.
## Cloud
GCS
## Data ingestion/Batch
Mage Pipelines
## Data warehouse
Big Query
## Transformations
Spark
## Dashboard
Looker Studio
## Instructions 

Clone this repository:
```
git clone https://github.com/mariotriana/Project_Covid_Data
```

Previously you must installed in your machine Terraform and Docker.

## Deploy Infraestructure (Terraform)
1. Navigate into Terraform folder within the Project folder
2. Place your own Google Cloud Platform credentials file into keys/ folder, then rename the file as (my-creds.json)
3. Run terraform initialize commands in this order:
```
terraform plan
```
```
terraform apply
```
Here you are creating a GCS bucket named "covid-data-project-bucket" and a Dataproc Cluter named "covid-data-cluster".

## Data processing through Mage, Pyspark and GCS
1. Navigate into mage folder within the Project folder
2. Place your credentials file (my-creds.json) within mage folder
3. Run the next commands to initialize Mage: 
```
docker compose build
```
```
docker compose up
```
Then, navigate to http://localhost:6789 in your browser. Now you are able to run Mage pipelines.

4. Go to the pipeline named "covid_data_pipeline" and run blocks in this order:
* data loader
* transformer 
* data exporter

5. Go to Google Cloud Storage in your navigator and check if the file named "covid_data.parquet" is in the bucket builded previously("covid-data-project-bucket")

* Run 2nd data exporter to submit Pyspark Job into Dataproc Cluster

6. Check if the job was uploaded into the cluster "covid-data-cluster" and the output of the job is here: gs://covid-data-project-bucket/output-data

## Big Query and Looker Studio
1. Return to mage, go to the pipeline named "covid_data_to_gcs" and run both blocks to send job's output to BigQuery.

2. To create a dashboard, go to Looker Studio in your browser, then click in create a new report and select Bigquery to choose the dataset called covid_data contained in the project called "My First project".

3. Choose the table "who_covid_data" and add it to the report.

4. Now you can create your own dashboard as I did here