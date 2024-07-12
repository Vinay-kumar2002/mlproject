import sys
import pandas as pd
from src.exception import customException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

class CustomData:
    def __init__( self,
                 gender:str,
                 race_ethinicity:str,
                 parantal_level_of_education:str,
                 lunch:str,
                 reading_score:str,
                 writing_score:int):
                 self.gender=gender
                 self.race_ethnicity=race_ethinicity
                 self.parantal_level_of_education=parantal_level_of_education
                 self.lunch=lunch
                 self.test_preparation_course=test_preparation_course
                 self.reading_score=reading_score
                 self.writing_score=writing_score 
    )    