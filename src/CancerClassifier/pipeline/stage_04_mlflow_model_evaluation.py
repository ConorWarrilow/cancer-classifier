from CancerClassifier.config.configuration import ConfigurationManager
from CancerClassifier.components.mlflow_model_evaluation import Evaluation
from CancerClassifier import logger
import os


# Uncomment the below credentials to log to mlflow server

#MLFLOW_TRACKING_USERNAME="ConorWarrilow"
#MLFLOW_TRACKING_PASSWORD="Con=dh!-or1"
#
#MLFLOW_TRACKING_URI = f"https://dagshub.com/ConorWarrilow/cancer-classifier-app.mlflow"
#
#
#os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI
#os.environ["MLFLOW_TRACKING_USERNAME"] = MLFLOW_TRACKING_USERNAME
#os.environ["MLFLOW_TRACKING_PASSWORD"] = MLFLOW_TRACKING_PASSWORD






STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        #evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e