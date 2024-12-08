import pandas as pd
import os
import requests
import pyreadstat

# Disable SSL verification
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_nhanes_data():
    """
    Download NHANES datasets for demographics and examination data
    """
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Download demographic data
    demo_url = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT'
    demo_response = requests.get(demo_url, verify=False)
    with open('data/demographics.xpt', 'wb') as f:
        f.write(demo_response.content)

    # Download body measures data
    body_url = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.XPT'
    body_response = requests.get(body_url, verify=False)
    with open('data/body_measures.xpt', 'wb') as f:
        f.write(body_response.content)

    # Read XPT files
    demo_data, _ = pyreadstat.read_xport('data/demographics.xpt')
    body_measures, _ = pyreadstat.read_xport('data/body_measures.xpt')

    # Save to CSV files
    demo_data.to_csv('data/demographics.csv', index=False)
    body_measures.to_csv('data/body_measures.csv', index=False)
    
    return demo_data, body_measures

if __name__ == "__main__":
    demo_data, body_measures = download_nhanes_data()
