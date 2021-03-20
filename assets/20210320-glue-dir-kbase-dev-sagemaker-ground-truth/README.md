Download contents from S3:

```
aws s3 sync s3://glue-dir-kbase-dev glue-dir-kbase-dev
```

Generate `20210320-glue-dir-kbase-dev.manifest` by running `prepare_sagemaker_ground_truth.ipynb`.

Clean up:

```
rm -rf glue-dir-kbase-dev
```