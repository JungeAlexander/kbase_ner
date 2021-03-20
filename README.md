<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: NER in kbase

Named entity recognition for documents in kbase using spacy.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `convert` | Convert the data to spaCy's binary format |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `convert` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/20210312-dummy/run-DataSink0-1-part-r-00000.bz2`](assets/20210312-dummy/run-DataSink0-1-part-r-00000.bz2) | Local | Dummy data as downloaded on 20210312 from RDS DB dump as produced by AWS Glue ETL. |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

## Setup

### Dependencies

Dependencies are managed via poetry:

```
poetry install --no-root
```

All commands in this README need to be run in a poetry shell which can be activated as follows:

```
poetry shell
```

### Project structure

The project structure is based on a spacy example project structure obtained as follows and
then adjusted:

```
python -m spacy project clone pipelines/ner_demo
```

## Documentation

To update the auto-generated parts of the documentation, run:

```
python -m spacy project document --output README.md
```