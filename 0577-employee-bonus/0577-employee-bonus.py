import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    #join operation
    merged=pd.merge(employee,bonus,on='empId',how='left')
    #where
    result=merged[(merged['bonus'].isnull()) | (merged['bonus']<1000)]
    #select name,bonus
    result=result[['name','bonus']]
    return result
    
    