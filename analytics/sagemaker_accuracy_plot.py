import re
import logging
import pandas as pd
import seaborn as sns
from typing import List
import matplotlib.pyplot as plt
import plotly.graph_objects as go

logging.basicConfig(format='[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample DataFrame
def plot_accuracy(df: pd.DataFrame, output_filename: str) -> go.Figure:

    """
    Creates an interactive bar chart to visualize the accuracy of all candidate models. 

    Args:
        df (pd.DataFrame): Input accuracy dataframe. 
        output_filename (str): Name of the file to save the plot.

    Returns:
        go.Figure: Plotly figure object.
    """
    df["accuracy"] = [str(i)+"%" for i in df["majority_voting_accuracy"]]
    fig = go.Figure()
    
    # Create bar traces for each year
    fig = go.Figure(data=[
        go.Bar(x=df['candidate_model'], y=df['majority_voting_accuracy'], 
               text=df['accuracy'], textposition='auto')
    ])
    
    # Customize the layout
    fig.update_layout(title='Candidate Model Accuracy',
                      xaxis_title='Candidate Model',
                      yaxis_title='Accuracy'
                     )
    
    fig.write_html(output_filename)
    
    logger.info("======================================")
    logger.info(f"Interactive accuracy plot saved as {output_filename}")
    logger.info("======================================")
    
    return fig