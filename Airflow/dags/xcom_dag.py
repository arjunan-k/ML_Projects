from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
 
from datetime import datetime
 
def _t1():
    return 43
 
def _t2(ti):
    ti.xcom_push(key='my_key', value=10)

def _t3(ti):
    print(ti.xcom_pull(key='my_key', task_ids='t2'))

def _branch(ti):
    value = ti.xcom_pull(key='my_key', task_ids='t2')
    if (value == 10):
        return 't3'
    return 't4'

with DAG("xcom_dag", start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
 
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )
    
    branch = BranchPythonOperator(
        task_id="branch",
        python_callable=_branch
    )

    t3 = BashOperator(
        task_id='t3',
        python_callable=_t3,
        bash_command="echo ''"
    )

    t4 = BashOperator(
        task_id='t4',
        bash_command="echo ''"
    )

    t5 = BashOperator(
        task_id='t5',
        bash_command="echo ''",
        trigger_rule='none_failed_min_one_success'
    )

    t1 >> branch >> [t3, t4] >> t5