# Cancer Classification App

src file is structured as follows:

.<br>
└── src/<br>
    ├── __init__.py <br>
    └── CancerClassifier/<br>
        ├── __init__.py<br>
        ├── components/<br>
        │   ├── data_ingestion.py<br>
        │   ├── mlflow_model_evaluation.py<br>
        │   ├── model_trainer.py<br>
        │   └── prepare_base_model.py<br>
        ├── config/<br>
        │   ├── configuration.py<br>
        │   └── constants/<br>
        │       └── __init__.py<br>
        ├── entity/<br>
        │   ├── __init__.py<br>
        │   └── config_entity.py <br>
        ├── pipeline/<br>
        │   ├── __init__.py<br>
        │   ├── prediction.py<br>
        │   ├── stage_01_data_ingestion.py<br>
        │   ├── stage_02_prepare_base_model.py<br>
        │   ├── stage_03_model_trainer.py<br>
        │   └── stage_04_mlflow_model_evaluation.py<br>
        └── utils/<br>
            ├── __init__.py<br>
            └── common.py<br>

components consists of the main steps in our pipeline
config contains our configuration class
entity contains the configuration parameters to be applied at each stage of the pipeline
pipeline simply contains code to run through the pipeline

