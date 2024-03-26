import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_leaf_visualizer_body():
    st.write("### Leaf Visualizer")
    st.info(
        f"* The client is interested in having a study that visually"
        f"shows the difference between a mildew infected from an uninfected leaf.")
    
    version = '1'
    if st.checkbox("Difference between average and variability image"):
      
      avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

      st.warning(
        f"* We can notice that there is a difference between the average"
        f"and the variablitiy image. Either way the shapes are recognizable.")

      st.image(avg_powdery_mildew, caption='Mildew Infected Leaf - Average and Variability')
      st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
      st.write("---")

    if st.checkbox("Differences between average mildew infected and average uninfected leaves"):
          diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

          st.warning(
            f"* We notice that there is a difference in color between the healthy"
            f"leaves and those who are infected." 
            f"The healthy leaves are clearly greener.")
          st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      my_data_dir = 'inputs/cherry-leaves/'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
            image_montage(dir_path=my_data_dir+ 'validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
      st.write("---")

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    label_path = os.path.join('inputs/cherry-leaves/', 'validation', label_to_display)
    if os.path.exists(label_path):
        images_list = os.listdir(label_path)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        list_rows = range(nrows)
        list_cols = range(ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(nrows * ncols):
            img = imread(os.path.join(label_path, img_idx[x]))
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {os.listdir(os.path.join(dir_path, 'validation'))}")

page_leaf_visualizer_body()