# About the project
This repository keeps a Data Engineering project that aims to gather data from Braziian economic landscape. Initially, most of data is about companies which are listed on B3 (Brasil, Bolsa, Balcão).

# Project outline
The project consists of collecting data using python applications and writting it on S3 **datalake**, then making needed **data cleaning** and **tranformations**. Once data is available on datalake, it is transformed into a **Data Lake House** by using **Delta** and **Pyspark**. The whole enviroment will be based on **Docker** containers orchestrated by **kubernetes operators** in **Airflow**.

## Settings
The first thing you need is a local Kubernetes Cluster, for this project KIND was used for this task. KIND is a cluster based on Docker containers, so it is crucial that you have KIND and Docker Desktop installed on your machine.
KIND uses YAML files to build the cluster and you can take a look at the b3_app\kind_b3.yaml to get familiarized with the required key:value pairs for the cluster configuration.

## KIND
Make sure you are in b3_app folder.
Run: 
* kind create cluster --name dfpcluster --config kind_b3.yaml
As a result you ll have two new containers running on your Docker, based on a kind image.

## DOCKER
Your recent created Kubernetes cluster needs that you have your images available on a container registry. The following steps are for build your image locally and then push into Docker Hub:

* docker build -t dfp:v1 .
* docker login
* docker tag dfp:v1 jcs7/dfp:v1 
* docker push jcs7/dfp:v1 ***It is gonna push as public, make it private, as soon as it is done by clicking on settings.***

