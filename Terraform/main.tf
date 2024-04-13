terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.23.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_storage_bucket_object" "script-job" {
  name = "spark_sql_project.py"
  bucket = google_storage_bucket.demo-bucket.name
  source = "../spark_sql_project.py"
}

resource "google_bigquery_dataset" "project_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}

resource "google_dataproc_cluster" "project_cluster" {
  name   = var.dataproc_cluster_name
  region = var.region 

  cluster_config {

      master_config {
        num_instances = 1
        machine_type  = "n2-standard-2"
        disk_config {
          boot_disk_type    = "pd-balanced"
          boot_disk_size_gb = 100
        }
      }
    
  }
}




