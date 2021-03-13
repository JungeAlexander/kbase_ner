- [NER in kbase](#ner-in-kbase)
  - [Setup](#setup)
  - [🗂 Assets](#-assets)

# NER in kbase

## Setup

The project structure is based on a spacy example project structure obtained as follows and
then adjusted:

```
poetry run python -m spacy project clone pipelines/ner_demo
```

## 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`poetry run python -m spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/20210312-dummy/run-DataSink0-1-part-r-00000.bz2](assets/20210312-dummy/run-DataSink0-1-part-r-00000.bz2) | Local | Dummy data as downloaded on 20210312 from RDS DB dump as produced by AWS Glue ETL. |