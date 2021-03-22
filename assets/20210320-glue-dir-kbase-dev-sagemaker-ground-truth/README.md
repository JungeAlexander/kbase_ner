# NER labeling in SageMaker Ground Truth

## Prepare files for labeling

Download contents from S3:

```
aws s3 sync s3://glue-dir-kbase-dev glue-dir-kbase-dev
```

Generate `20210320-glue-dir-kbase-dev.manifest` by running `prepare_sagemaker_ground_truth.ipynb`.
Then upload `20210320-glue-dir-kbase-dev.manifest` to `s3://glue-dir-kbase-dev-sagemaker-ground-truth`

Clean up input files:

```
rm -rf glue-dir-kbase-dev
```

## Download and convert labels

Download labels:

```
aws s3 sync s3://glue-dir-kbase-dev-sagemaker-ground-truth/annotations/ annotations
```

Clean up:

```
rm -rf annotations/
```