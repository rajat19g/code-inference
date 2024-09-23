from pydantic import BaseModel
from enum import Enum


class BinaryInput(Enum):
    zero = 0
    one = 1


# Define the input and output schema for the FastAPI application here
class InputData(BaseModel):
    first_bit: BinaryInput
    second_bit: BinaryInput


class PredictionResponse(BaseModel):
    prediction: BinaryInput