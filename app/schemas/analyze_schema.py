from pydantic import BaseModel
from typing import Dict, List


class Metadata(BaseModel):
    rows: int
    columns: int
    numeric_columns: List[str]
    categorical_columns: List[str]


class AnalyzeResponse(BaseModel):
    meta_data: Metadata
    missing_values: Dict[str, int]
    duplicates: int
    data_types: Dict[str, str]