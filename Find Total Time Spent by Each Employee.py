import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees['diff'] = employees['out_time'] - employees['in_time']

    employees = employees[['event_day','emp_id','diff']].groupby(['event_day','emp_id'])['diff'].sum().reset_index()
    
    

    #return employees.rename(columns = {'event_day' :'day','diff':'total_time'})
    return employees.rename({'event_day' :'day','diff':'total_time'}, axis = 1)
    