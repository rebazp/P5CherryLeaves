import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from src.machine_learning.evaluate_clf import load_test_evaluation

labels = ["healthy", "powdery_mildew"]
my_data_dir = '/workspace/P5CherryLeaves/inputs/cherry-leaves'
train_path = os.path.join(my_data_dir, 'train')
val_path = os.path.join(my_data_dir, 'validation')
test_path = os.path.join(my_data_dir, 'test')

def plot_rgb_channels(pil_image):
    r, g, b = pil_image.split()
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    axes[0].imshow(r, cmap='Reds')
    axes[0].set_title('Red Channel')
    axes[0].axis('off')

    axes[1].imshow(g, cmap='Greens')
    axes[1].set_title('Green Channel')
    axes[1].axis('off')

    axes[2].imshow(b, cmap='Blues')
    axes[2].set_title('Blue Channel')
    axes[2].axis('off')

    plt.tight_layout()
    return fig

def page_ml_performance_metrics():
    version = '4'
    output_dir = os.path.join("outputs", version)

    st.write("### Train, Validation, and Test Set: Labels Frequencies")
    labels_distribution_path = os.path.join(output_dir, "labels_distribution.png")
    if os.path.exists(labels_distribution_path):
        st.image(labels_distribution_path, caption='Labels Distribution on Train, Validation, and Test Sets')
    else:
        st.write("Error: Image file not found at path:", labels_distribution_path)
    st.write("---")

    st.write("### Model History")

    st.write(" **Model Training Accuracy**")
    model_acc_path = os.path.join(output_dir, "model_training_acc.png")
    if os.path.exists(model_acc_path):
        st.image(model_acc_path, caption='Model Training Accuracy')
    else:
        st.write("Error: Image file not found at path:", model_acc_path)

    st.write(" **Model Training Losses**")
    model_loss_path = os.path.join(output_dir, "model_training_losses.png")
    if os.path.exists(model_loss_path):
        st.image(model_loss_path, caption='Model Training Losses')
    else:
        st.write("Error: Image file not found at path:", model_loss_path)
    st.write("---")

    st.write("### Generalized Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.write("### RGB Channels")
    pointer = 66
    label = labels[0]  # Select healthy or powdery_mildew
    image_files = os.listdir(os.path.join(test_path, label))
    if image_files:
        image_path = os.path.join(test_path, label, image_files[pointer])
        pil_image = Image.open(image_path)
        fig = plot_rgb_channels(pil_image)
        st.pyplot(fig)
    else:
        st.write("Error: No image files found in directory:", os.path.join(test_path, label))