
# mlops-sustainability-oss

Welcome 👋 to this MLOps repository.
Consider this repository a modified version (extended-subset) of our [MLOps-CPD](https://github.com/IBM/MLOps-CPD) repository which is our simplest approach with the most rigorous documentation.

The main differences are:
- Using **climate data from Copernicus** instead of the German Credit Risk Dataset
- Self-sustaining approach through a scheduled pipeline system that retrieves the most recent weather data
- **Use of Open Source  Software (OSS) for Model and Dataset Versioning** via Data Version Control ([DVC](https://dvc.org))

This MLOps accelerator uses IBM Cloud Object Storage (COS) as remote for DVC (via S3 API), an SKLearn model for training, and Watson Machine Learning (WML) for deployment.
Our notebook repertoire is easily modified to leverage a different data store, custom ML models, and other providers for model deployment. 

See [todos](TODO.md)
