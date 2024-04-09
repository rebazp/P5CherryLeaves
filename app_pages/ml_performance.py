import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from PIL import Image
import numpy as np

from src.machine_learning.evaluate_clf import load_test_evaluation

labels = ["healthy", "powdery_mildew"]
my_data_dir = '/workspace/P5CherryLeaves/inputs/cherry-leaves'
train_path = my_data_dir + '/train'
val_path = my_data_dir + '/validation'
test_path = my_data_dir + '/test'

def page_ml_performance_metrics():
    version = '4'
    output_dir = "outputs/" + version

    st.write("### Train, Validation, and Test Set: Labels Frequencies")
    labels_distribution_path = os.path.join(output_dir, "labels_distribution.png")
    st.image(labels_distribution_path, caption='Labels Distribution on Train, Validation, and Test Sets')
    st.write("---")

    st.write("### Model History")

    st.write(" **Model Training Accuracy**")
    model_acc_path = os.path.join(output_dir, "model_training_acc.png")
    st.image(model_acc_path, caption='Model Training Accuracy')

    st.write(" **Model Training Losses**")
    model_loss_path = os.path.join(output_dir, "model_training_losses.png")
    st.image(model_loss_path, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalized Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))