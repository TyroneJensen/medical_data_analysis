import pandas as pd
from sqlalchemy import create_engine

def clean_and_process_data():
    """
    Clean and process NHANES datasets
    """
    # Load the datasets
    demo_data = pd.read_csv('data/demographics.csv')
    body_measures = pd.read_csv('data/body_measures.csv')

    # Create an SQLite database
    engine = create_engine('sqlite:///nhanes_data.db')

    # Save dataframes to SQL tables
    demo_data.to_sql('demographics', con=engine, if_exists='replace', index=False)
    body_measures.to_sql('body_measures', con=engine, if_exists='replace', index=False)

    # Example data processing: Join tables on participant ID
    query = """
    SELECT d.*, b.*
    FROM demographics d
    JOIN body_measures b ON d.SEQN = b.SEQN
    """
    combined_data = pd.read_sql(query, con=engine)

    # Handle missing values by filling with a placeholder
    combined_data.fillna(value={'RIAGENDR': -1, 'BMXBMI': combined_data['BMXBMI'].mean()}, inplace=True)

    # Ensure correct data types
    combined_data['RIAGENDR'] = combined_data['RIAGENDR'].astype(int)
    combined_data['BMXBMI'] = combined_data['BMXBMI'].astype(float)

    # Save the cleaned data
    combined_data.to_csv('data/cleaned_data.csv', index=False)

    return combined_data

if __name__ == "__main__":
    cleaned_data = clean_and_process_data()
