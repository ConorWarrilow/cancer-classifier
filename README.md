# Cancer Classification App

src file is structured as follows:

.
└── src/
    ├── __init__.py
    └── CancerClassifier/
        ├── __init__.py
        ├── components/
        │   ├── data_ingestion.py
        │   ├── mlflow_model_evaluation.py
        │   ├── model_trainer.py
        │   └── prepare_base_model.py
        ├── config/
        │   ├── configuration.py
        │   └── constants/
        │       └── __init__.py
        ├── entity/
        │   ├── __init__.py
        │   └── config_entity.py 
        ├── pipeline/
        │   ├── __init__.py
        │   ├── prediction.py
        │   ├── stage_01_data_ingestion.py
        │   ├── stage_02_prepare_base_model.py
        │   ├── stage_03_model_trainer.py
        │   └── stage_04_mlflow_model_evaluation.py
        └── utils/
            ├── __init__.py
            └── common.py

components consists of the main steps in our pipeline
config contains our configuration class
entity contains the configuration parameters to be applied at each stage of the pipeline
pipeline simply contains code to run through the pipeline

