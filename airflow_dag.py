from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# Define default arguments for the DAG
default_args = {
    'owner': 'Arthur',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'medical_data_analysis_dag',
    default_args=default_args,
    description='A DAG to coordinate medical data analysis scripts',
    schedule_interval=timedelta(days=1),  # Set interval to run daily
) as dag:

    def run_data_download():
        os.system('python c:/Users/Arthur/CODE/DataProjects/medical_data_analysis/data_download.py')

    def run_data_processing():
        os.system('python c:/Users/Arthur/CODE/DataProjects/medical_data_analysis/data_processing.py')

    def run_analysis():
        os.system('python c:/Users/Arthur/CODE/DataProjects/medical_data_analysis/analysis.py')

    def run_dashboard():
        os.system('python c:/Users/Arthur/CODE/DataProjects/medical_data_analysis/dashboard.py')

    # Define tasks
    download_task = PythonOperator(
        task_id='download_data',
        python_callable=run_data_download,
    )

    process_task = PythonOperator(
        task_id='process_data',
        python_callable=run_data_processing,
    )

    analysis_task = PythonOperator(
        task_id='run_analysis',
        python_callable=run_analysis,
    )

    dashboard_task = PythonOperator(
        task_id='run_dashboard',
        python_callable=run_dashboard,
    )

    # Set task dependencies
    download_task >> process_task >> analysis_task >> dashboard_task
