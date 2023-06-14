# TODO

**General**
- [ ] Build workarounds for issues faced with data pulling and management due to missing persistent filesystem in CPDaaS
- 

**Data**
- [ ] Make more sophisticated training data (concatenate hourly to daily for all months etc)
- [ ] Make extensive feature selection, feature engineering
- *Remote*
    - [x] Test Copernicus (cdsapi) and get some data (ERA5/GloFAS) related to precipitation/river discharge/floods
    - [x] Investigate DVC and check whether or not viable candidate for OSS part of demo
    - [x] Implement data version control for originally retrieved data from Copernicus 
    - [x] Implement DVC with COS as remote (S3-protocol)
        - not that COS credentials must be created with HMAC option enabled

**Model**
- [ ] (Write notebook for model development?)
- [x] Write notebook for model training
- [ ] Write notebook for model deployment
- [ ] Write notebook for getting "newest data" that is supposed to be run weekly.
- [ ] Write notebook for merging old data with newer data (data_until_last week + data_from_last_week)

**MLOps / WS**
- [ ] Put together pipeline
- [ ] Consider and realize pipeline scheduling
- [ ] (Think about pipeline extension where **model trained on data_until_last_week** is benchmarked against **data_with_last_week**)



**To think about:**

- Maybe track model in c0_train_model instead of c1_deploy_model to avoid - once again - storing the model to cos and then downloading it again in the next notebook before finally tracking it.

