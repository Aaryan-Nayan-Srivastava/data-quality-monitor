import numpy as np
import pandas as pd
from app.utils.logger import get_logger

logger=get_logger(__name__)

# Counts the no of missing value in each column
def detect_missing_values(df):
    missing={}
    for column in df.columns:
        missing[column]=df[column].isnull().sum()
    return missing

# Counts the no of duplicate rows
def detect_duplicates(df: pd.DataFrame):
    return df.duplicated().sum()

# Tells the datatype of all the columns
def detect_data_types(df:pd.DataFrame):
    data_types={}
    for column in df.columns:
        data_types[column]=str(df[column].dtype)
    return data_types

# Detects outliers using IQR
# IQR = Q3 - Q1
# Lower bound = Q1 - 1.5 * IQR
# Upper bound = Q3 + 1.5 * IQR
def detect_outliers(df:pd.DataFrame):
    result={}
    # only numeric columns required
    numeric_cols=df.select_dtypes(include=['number']).columns

    for column in numeric_cols:
        Q1=df[column].quantile(0.25)
        Q3=df[column].quantile(0.75)
        IQR=Q3-Q1
        
        lower=Q1-1.5*IQR
        upper=Q3+1.5*IQR

        outliers=df[ (df[column]>upper) | (df[column]<lower) ]
        
        result[column]=int(len(outliers))
    
    return result

# Metadata Generation
def generate_basic_statistics(df:pd.DataFrame):
    columns=df.columns
    result={}
    rows=len(df)
    cols=len(columns)
    result['rows']= rows
    result['columns']=cols
    result['column_names']=list(columns)
    result["numeric_columns"]= list(df.select_dtypes(include=['number']).columns)
    result["categorical_columns"]=list(df.select_dtypes(exclude=['number']).columns)
    return result

# Overall Quality check
def run_data_quality_checks(df: pd.DataFrame):
    data_quality={
        "meta_data": generate_basic_statistics(df),
        "data_types": detect_data_types(df),
        "missing_values": detect_missing_values(df),
        "duplicates": detect_duplicates(df),
        "outliers": detect_outliers(df)
    }
    logger.info("Data quality checks completed successfully")
    return data_quality
