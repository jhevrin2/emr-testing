# emr-testing
Testing repository for EMR

### SSH

```bash
ssh -i ~/.aws/keys/emr-test.pem hadoop@ec2-18-232-187-222.compute-1.amazonaws.com
```

### CLI Create

aws emr create-cluster --name "Test EMR Cluster" \
--applications Name=Spark --release-label emr-5.33.1 \
--instance-count 2 --instance-type m4.large  --region us-east-1 --use-default-roles \
--log-uri 's3n://aws-logs-812124875981-us-east-1/elasticmapreduce/' \
--steps '[{"Args":["spark-submit","s3://jhevrin2-datasci/datascience/emr-test/main.py"],"Type":"CUSTOM_JAR","ActionOnFailure":"TERMINATE_CLUSTER","Jar":"command-runner.jar","Properties":"","Name":"Spark application"}]' \
--bootstrap-actions '[{"Path":"s3://jhevrin2-datasci/datascience/emr-test/install.sh","Name":"Install requirements"}]' \
--scale-down-behavior TERMINATE_AT_TASK_COMPLETION \
--auto-terminate
