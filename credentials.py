import os

# This file emulates the environment variables passed by WS Pipelines. Set them if running locally.

def set_env_variables_for_credentials():
    """
    
    Complete and import this method to test your notebooks outside of a WS Pipeline environment.
    
    """

    ## IBM CLOUD (IC)
    os.environ["CLOUD_API_KEY"] = ""

    ## CLOUD OBJECT STORAGE (COS)
    os.environ["MLOPS_COS_CREDENTIALS"] = "{\"API_KEY\":\"[API_KEY]\",\"AUTH_ENDPOINT\":\"https://iam.cloud.ibm.com/oidc/token\",\"BUCKET\":\"[BUCKET_NAME]\",\"CRN\":\"[CRN]\",\"ENDPOINT_URL\":\"https://s3.eu-de.cloud-object-storage.appdomain.cloud\"}"
    os.environ["PROJECT_COS_CREDENTIALS"] = "{\"API_KEY\": \"[API_KEY]\"," \
                                            "\"CRN\": null, \"AUTH_ENDPOINT\": \"https://iam.cloud.ibm.com/oidc/token\"," \
                                            "\"ENDPOINT_URL\": \"https://s3.private.eu-de.cloud-object-storage.appdomain.cloud\"," \
                                            "\"BUCKET\": \"[BUCKET_NAME]\"}"
    os.environ["PROJECT_ID"] = ""

    ## CLOUD OBJECT STORAGE (COS HMAC)
    # HMAC credentials
    os.environ["HMAC_ADMIN_ACCESS_KEY"] = ""
    os.environ["HMAC_ADMIN_SECRET_ACCESS_KEY"] = ""

    # COPERNICUS (CDS)
    os.environ["CDS_USER_ID"] = ""
    os.environ["CDS_API_KEY"] = ""

    # GIT REPOSITORY (solely for data and model versioning)
    os.environ["GIT_REPOSITORY"] = ""

    # VARIABLES FOR TEMP. TESTING
    os.environ["serialized_data_filename"] = "era5-glofas-merged.pkl"