import pytest
import pandas as pd

def test_DuplicateCheck():
    df = pd.read_csv('target.csv')
    assert df.duplicated().sum() == 0, "Duplicate rows found in target.csv"

def test_DataCompletenessCheck():
    df = pd.read_csv('target.csv')
    assert not df.empty, "Target.csv is empty"

def test_deptNoForNullValueCheck():
    target_df = pd.read_csv('target.csv')
    isDeptNoNULl = target_df[ 'deptno']. isnull().any()
    assert isDeptNoNULl == True,"deptno is having a null value - Please check"

def test_enoNoForUnigueValueCheck():
    target_df = pd.read_csv('target.csv')
    totalcount = target_df[ 'eno'] .count()
    deptNoUniqueValueCount = len(target_df['eno'].unique())
    assert totalcount == deptNoUniqueValueCount ,"eno column valuesTare not unigue - please check"