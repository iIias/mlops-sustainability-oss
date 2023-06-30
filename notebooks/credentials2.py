import os

# This file emulates the environment variables passed by WS Pipelines. Set them if running locally.

def set_env_variables_for_credentials():
    """
    
    Complete and import this method to test your notebooks outside of a WS Pipeline environment.
    
    """

    ## IBM CLOUD (IC)
    os.environ["CLOUD_API_KEY"] = "t9_rVHDftt3jhZCU1nDfEV7fZbtW97MsqmPunvgiOeSP"

    ## CLOUD OBJECT STORAGE (COS)
    os.environ["MLOPS_COS_CREDENTIALS"] = "{\"API_KEY\":\"mfy1BVF3KJJ11ECL1_O1D8OVPrVY2WSKUQbONUXcxnxx\",\"AUTH_ENDPOINT\":\"https://iam.cloud.ibm.com/oidc/token\",\"BUCKET\":\"mlops-sustainability-data\",\"CRN\":\"crn:v1:bluemix:public:cloud-object-storage:global:a/504dd816f9de4145afea0a23d744f2f8:8d81b9f5-fde9-4571-b32e-b2b48184a24f::\",\"ENDPOINT_URL\":\"https://s3.eu-de.cloud-object-storage.appdomain.cloud\"}"
    os.environ["PROJECT_COS_CREDENTIALS"] = "{\"API_KEY\": \"YNVNV9pJkp_jYp3rTvKFEOEI74mDD3AHWuBM9NnJ8dvq\"," \
                                            "\"CRN\": null, \"AUTH_ENDPOINT\": \"https://iam.cloud.ibm.com/oidc/token\"," \
                                            "\"ENDPOINT_URL\": \"https://s3.private.eu-de.cloud-object-storage.appdomain.cloud\"," \
                                            "\"BUCKET\": \"mlopsforsustainability-donotdelete-pr-jqgwg4b2m3k67p\"}"
    os.environ["PROJECT_ID"] = "5f0d238e-b1b1-41c4-b83c-5a4c262d1988"

    ## CLOUD OBJECT STORAGE (COS HMAC)
    # HMAC credentials
    os.environ["HMAC_ADMIN_ACCESS_KEY"] = "d9e9ebdda90b4a2f916e350c840c5b44"
    os.environ["HMAC_ADMIN_SECRET_ACCESS_KEY"] = "338ea829c19f70fa1d3095201ccb6eb8e67e261390aacceb"

    # COPERNICUS (CDS)
    os.environ["CDS_USER_ID"] = "198547"
    os.environ["CDS_API_KEY"] = "84cce522-23c8-4df9-8458-f1f3e7f15a07"

    # GIT REPOSITORY (solely for data and model versioning)
    os.environ["REPO_NAME"] = "dvc-testing"
    os.environ["GIT_REPOSITORY"] = \
        f"https://iiias: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@github.com/iiias/{os.getenv('REPO_NAME')}.git"

    os.environ["GIT_USER_EMAIL"] = "ilias.ennmouri@ibm.com"
    os.enivorn["GIT_USER_NAME"] = "Ilias Ennmouri"

    # VARIABLES FOR TEMP. TESTING
    os.environ["serialized_data_filename"] = ""

    os.environ["MODEL_FILENAME"] = "xgbr.pkl"

    os.environ["model_dvc_location"] = f"model/{os.getenv('MODEL_FILENAME')}"

    # For testing
    os.environ["train_package_dvc_location"] = "data/train_package.pkl"
    os.environ["test_package_dvc_location"] = "data/test_package.pkl"