from pydantic import BaseModel
from typing import List

class Plan(BaseModel):
    steps: List[str]

class ExecutionResult(BaseModel):
    data: dict

class VerificationResult(BaseModel):
    is_valid: bool
    issues: List[str]
