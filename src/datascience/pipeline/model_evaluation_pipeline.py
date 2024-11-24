from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        data_evaluation_config=config.get_model_evaluation_config()
        data_evaluation=ModelEvaluation(config=data_evaluation_config)
        data_evaluation.log_into_mlflow()
