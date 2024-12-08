# Medical Data Science Project

## Overview
This project utilizes the CDC's NHANES dataset to perform medical data analysis, including data processing, analysis, and visualization.

## Technical Stack
- **Languages**: Python
- **Libraries**:
  - Pandas
  - SQLite
  - Matplotlib/Seaborn
  - Dash/Plotly
  - Requests
  - Pyreadstat

## Project Structure
- `data_download.py`: Script to download NHANES datasets.
- `data_processing.py`: Script for data cleaning and processing.
- `analysis.py`: Script for data analysis and visualization.
- `dashboard.py`: Dash app for interactive data visualization.
- `airflow_dag.py`: Apache Airflow DAG to automate the execution of scripts at a set interval, including data download, processing, analysis, and dashboard visualization.
- `requirements.txt`: List of project dependencies.

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up Apache Airflow and add the DAG file `airflow_dag.py` to your Airflow DAGs directory.
4. Run the Airflow scheduler and web server to activate the DAG.
5. Alternatively, you can run the scripts manually:
   - Run `data_download.py` to download the datasets.
   - Run `data_processing.py` to clean and process the data.
   - Run `analysis.py` to perform data analysis.
   - Run `dashboard.py` to view the interactive dashboard.

## Security Considerations
- SSL verification is disabled for dataset downloads. Ensure proper SSL handling in production.

## Future Work
- Implement advanced data analysis techniques.
- Add more interactive visualizations.
- Integrate machine learning models.
