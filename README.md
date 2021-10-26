# emr-testing
Testing repository for EMR

```bash
aws emr create-cluster --name "Test Cluster" --release-label emr-5.33.1 \
--use-default-roles \
--applications Name=Spark \
--instance-count 3 --instance-type m4.large \
--bootstrap-actions Path="s3://elasticmapreduce/bootstrap-actions/download.sh"
```

### SSH

```bash
ssh -i ~/.aws/keys/emr-test.pem hadoop@ec2-54-172-227-174.compute-1.amazonaws.com
```