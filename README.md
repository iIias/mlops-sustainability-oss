
# mlops-sustainability-oss

Welcome 👋 to this MLOps repository.
Consider this repository a modified version (extended-subset) of our [MLOps-CPD](https://github.com/IBM/MLOps-CPD) repository which is our simplest approach with the most rigorous documentation.

The main differences are:
- Using **climate data from Copernicus** instead of the German Credit Risk Dataset
- Self-sustaining approach through a scheduled pipeline system that retrieves the most recent weather data
- **Use of Open Source  Software (OSS) for Model and Dataset Versioning** via Data Version Control ([DVC](https://dvc.org))

This MLOps accelerator uses IBM Cloud Object Storage (COS) as remote for DVC (via S3 API), an SKLearn model for training, and Watson Machine Learning (WML) for deployment.
Our notebook repertoire is easily modified to leverage a different data store, custom ML models, and other providers for model deployment. 

Welcome 👋 to our MLOps for sustainability repository.

**The Mission:**
With climate change becoming an increasingly pressing issue, flood risks gain in prevalence. We want to demonstrate how we can leverage data from Copernicus Climate Data Store, and build an MLOps pipeline which is self-sustaining in nature.
When training a model once - or only re-training it in terms of hyperparameter tuning - the model's accuarcy will decay leaving a more or less unusable model after a given amount of time. 📉
Once the days for which we predicted flood risks passed and actual data is available, we retrieve the newest data, retrain the model, and benchmark the model against its predecessor, to determine which model to keep and deploy.

Consider this repository a modified version (extended-subset) of our [MLOps-CPD](https://github.com/IBM/MLOps-CPD) repository which is our simplest approach with the most rigorous documentation.

The main differences are:
- Using **climate data from Copernicus** instead of the German Credit Risk Dataset
- Self-sustaining approach through a scheduled pipeline system that retrieves the most recent weather data
- **Use of Open Source  Software (OSS) for Model and Dataset Versioning** via Data Version Control ([DVC](https://dvc.org))

This MLOps accelerator uses IBM Cloud Object Storage (COS) as remote for DVC (via S3 API), an SKLearn model for training, and Watson Machine Learning (WML) for deployment.
Our notebook repertoire is easily modified to leverage a different data store, custom ML models, and other providers for model deployment. 

**IBM Employees only:** Checkout the [recording](https://ibm.ent.box.com/s/2hco3iifpoiq3nlv354nag30s4l318i3) of our TechFest23 session for this project

**Disclaimer:** This model is currently no where near academic-grade quality. We focused primarily on quickly constructing an MLOps workflow that works with sustainability data and DVC.

We reserve the right to continously fix, improve, and progress this repertoire. See [todos](TODO.md) for information on upcoming features.

### Overview

This subsection will describe our data source, datasets, sub-modules, requirements *etc.* in more detail.

#### Data Source and Datasets
We use the [Copernicus Data Store](https://cds.climate.copernicus.eu/#!/home) to retrieve historic and current climate data. We are collecting the following datasets and variables:

- 🌍 [ERA5-Land hourly data from 1950 to present](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form)
    - ```stl1``` (Soil Temperature Level 1)
    - ```vswl1``` (Volumetric Soil Water Layer 1)
    - ```total_preciptation``` (Total Precipitation)

- 🌊 [River discharge and related historical data from the Global Floow Awareness System (GloFAS)](https://cds.climate.copernicus.eu/cdsapp#!/dataset/cems-glofas-historical?tab=form)
    - ```dis24``` (averaged daily river discharge in m^3/s)

Since we want to predict flooding risks, we want to predict the time and place where extremely high river discharge occurs. Therefore, all variables gathered from ERA5 are used to predict our predictant ```dis24```. All data coming from the aforementioned datasets come either in NetCDF or NetCDF4 format, which is easily handled in our Notebooks. 
We make use of Copernicus' "Sub-region extraction" feature to not get data for the whole globe, but rather for a specified sub-region delimited by coordinates for N, W, S, E boundaries. This allows us to easily make different pipelines (and subsequently deploy different models for different regions). In our example, we set Europe as specified region in our pipeline parameters.

All of the aforementioned is handled in our notebooks. For you to recreated the proposed MLOps lifecycle, you will need to create your own Copernicus account to retrieve personalized credentials, since we are not sharing / hard-coding ours for obvious reasons.

#### Prerequisites on IBM Cloud

In order to use the above asset we need to have access to have an IBM environment with authentication. Your IBM Cloud Account should have access following services:

- IBM Watson Studio
- IBM Watson Machine Learning (If you are not deploying with a different provider)
- IBM Watson Knowledge Catalog (with Factsheets and Model Inventory)*
- IBM Watson OpenScale
- IBM Cloud Object Storage (If you are not using a different data store)

Please ascertain you have appropriate access in all the services.

The runs are also governed by the amount of capacity unit hours (CUH) you have access to. If you are running on the free plan please refer to the following links:

- https://cloud.ibm.com/catalog/services/watson-studio
- https://cloud.ibm.com/catalog/services/watson-machine-learning
- https://cloud.ibm.com/catalog/services/watson-openscale
- https://cloud.ibm.com/catalog/services/watson-knowledge-catalog


## Instructions for Project Set-up

### General Set-up

For a general tutorial please refer to the regularly maintained instructions in our [main MLOps repository](https://github.com/IBM/MLOps-CPD). We cannot afford to update each repository subsequent to changes or new features in Watson Studio *etc.*, which is why we refer you to the main documentation.

There you will find instructions on Watson Studio Project and Deployment Spaces, Cloud Object Storage set-up, Pipeline set-up *and more*.

### Where this project deviates

### Addendum: Cloud Object Storage Set-up

When creating Cloud Object Storage **credentials**, you will need to enable HMAC. 

Service Credentials > New Credential (Advanced > USE HMAC KEYS ("HMAC": true) and WRITER privilege). We need the access_key_id and secret_access_key from this file.

**Add both keys to your ```credentials.py``` file if you are running locally, or..**

**Make sure to make both keys available to the pipeline...** e.g. <br>
- add them to the ```MLOPS_COS_CREDENTIALS``` with all other Cloud Object Storage secrets.

### Addendum: Pipeline Set-up

<img width="1878" alt="Screenshot 2023-06-19 at 12 25 10" src="https://github.com/iIias/mlops-sustainability-oss/assets/15169745/5eeef014-7a3f-4866-8378-3ce9e471e21b">


### DVC Set-up

[DVC](https://dvc.org) is a git-like way to manage large data across systems, and it can connect easily with IBM COS to store and distribute versioned data. This section assumes some familiarity with how to create resources through the cloud.ibm.com dashboard from [MLOps-CPD](https://github.com/iiias/MLOps-CPD).

#### NOT covered by Notebooks

In order for DVC to be able to actively track datasets or models, you will need to initialize a new empty repository.

Add the information for your Repository to ```credentials.py``` under the ```GIT_REPOSITORY```environment variable.
It has to have the following format:<br>
```https://USERNAME:GIT-TOKEN@github.com/USERNAME/REPOSITORY-NAME```

Note: DVC will **not** store your dataset and model but placeholders to track data files and directories. Additionally it will contain your DVC configuration file, which in turn contains your remote (URL, Endpoint, **unhashed** Access Secrets).

#### Covered by Notebook

Within notebook [a1_init_dvc_and_track_data.ipynb](/notebooks/a1_init_dvc_and_track_data.ipynb) 

- the previouosly created Git Repository is cloned into the temporary filesystem of the CPDaaS Jupyter Runtime.
- DVC is initialized (```dvc init```)
- A Cloud Object Storage instance is added to DVC as a remote (using the credentials passed via WS Pipeline Parameters) and subsequently committed to the DVC Git Repository via ```git commit```and ```dvc push```.
- Create folder structure e.g. ```/data```, ```/model```
- The full pickle binary of the dataset is added ```dvc add```, ```git commit```, ```dvc push````
    - Metadata is pushed to repository
    - Binary is uploaded to COS Bucket

Note: All steps will be repeated by pipeline as a consequence of having the pipeline run according to a schedule. That is of no concern, since redundant cells will be skipped. 
