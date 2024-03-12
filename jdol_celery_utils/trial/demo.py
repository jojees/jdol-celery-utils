from jdol_celery_utils.celery_app import app, get_queue_name
import os
import pandas as pd


@app.task(queue=get_queue_name())
def process_file(filename):
    input_path = os.path.join('/data', filename)
    output_path = os.path.join('/results', f"processed_{filename}")
    
    # Perform processing on the file (example: read CSV file)
    data = pd.read_csv(input_path)
    
    # Perform some processing on the data (example: just copying it)
    processed_data = data.copy()
    
    # Save the processed data to the output file
    processed_data.to_csv(output_path, index=False)
    
    return output_path