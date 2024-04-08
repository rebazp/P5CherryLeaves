# Cherry Leaves
* Powdery mildew is a common fungal disease affecting a wide variety of plants, caused by diverse species of ascomycete fungi in the Erysiphales order. Its identification is relatively simple due to distinctive symptoms such as white powdery spots on leaves and stems. Although lower leaves are often most affected, the mildew can appear on any above-ground part of the plant. As the disease progresses, the spots enlarge and become denser due to the formation of numerous asexual spores, potentially spreading throughout the plant. This fungus thrives in environments with high humidity and moderate temperatures, making greenhouses particularly susceptible to its spread, posing a threat to agricultural and horticultural practices. Control methods include chemical treatments, bio-organic approaches, and genetic resistance.

* In agricultural settings, powdery mildew can be managed through various methods such as chemical control, genetic resistance, and employing careful farming practices. To prevent the disease, farmers can choose powdery mildew-resistant plant varieties and alternate between resistant and susceptible varieties to hinder pathogen adaptation. Additionally, reducing humidity by spacing plants for airflow and pruning foliage can help mitigate its spread. Conventional chemical control involves the use of standard fungicides, with spray programs recommended upon initial detection of symptoms. Regular application of fungicides like triadimefon, propiconazole, hexaconazole, myclobutanil, and penconazole is advised for optimal results. Non-conventional methods include utilizing substances like milk, natural sulfur, potassium bicarbonate, metal salts, and oils, each offering alternative modes of action against powdery mildew. Metal salt fungicides should be applied regularly until harvest, sulfur should be applied preemptively to inhibit spore germination, and copper sulfate, although effective in organic farming, may require lime to mitigate its adverse effects on plants.

* The goal is to create a ML model that can predict if a cherry leaf is infected with powdery mildew or uninfected. The model need to have a accuracy rate of minimum 97% and my model reached 100% accuracy.

[View Live Version Here]()

# Table of Contents
* [Dataset Content](#dataset-content)
* [Business Requirements](#business-requirements)
* [Hypothesis & How To Validate](#hypothesis--how-to-validate)
* [The Rationale To Map The Business Requirements To The Data Visualizations & ML Tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations--ml-tasks)
* [ML Business Case](#ml-business-case)
* [Dashboard Design](#dashboard-design)
* [Bugs](#bugs)
* [Unfixed Bugs](#unfixed-bugs)
* [Testing](#testing)
* [Deployment](#deployment)
* [Main Data Analysis & Machine Learning Libraries](#main-data-analysis--machine-learning-libraries)
* [Credits](#credits)
* [Content](#content)
* [Acknowledgements](#acknowledgements)

## Dataset Content
* The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). I created a user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains over 4,000 images taken from the client's cherry plantation. The images show healthy cherry leaves and leaves that have been infected with powdery mildew. Since the cherry plantation crop is one of the finest products in the client's portfolio, the quality of the product is of high concern for the company.

## Business Requirements

Farmy & Foods is grappling with powdery mildew affecting their cherry plantation crop, leading to inefficient manual inspection processes. Employees spend 30 minutes per tree visually identifying and treating infected trees with a specific compound. With thousands of cherry trees spread across multiple farms, scalability becomes a significant issue. To address this, the IT team proposes implementing a machine learning (ML) system to instantly detect powdery mildew in cherry trees using leaf images. Success in this endeavor could pave the way for similar initiatives in detecting pests in other crops, utilizing datasets comprising cherry leaf images provided by Farmy & Foods.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis & How To Validate

### Hypothesis
* Cherry tree foliage afflicted by powdery mildew displays unique visual characteristics when contrasted with the appearance of healthy cherry leaves.

### Validation
* **Dataset Examination**: Confirm the hypothesis through exploratory data analysis (EDA) of the dataset, employing techniques like visualizing samples of both healthy and powdery mildew-affected cherry leaves to detect any discernible patterns or distinctions.

* **Model Creation**: Develop a machine learning (ML) model utilizing Convolutional Neural Networks (CNNs) to discern between healthy and powdery mildew-infected cherry leaves. Validate the model's efficacy and performance using suitable validation methods.

* **Assessment**: Assess the model's effectiveness on an independent test set to verify its capacity to generalize. Utilize metrics like accuracy to gauge its proficiency in identifying powdery mildew.


## The Rationale To Map The Business Requirements To The Data Visualizations & ML Tasks

#### Business Requirements
* **Visual Discrimination**: Utilize visual representations of cherry leaf images to distinguish between healthy leaves and those afflicted by powdery mildew. This facilitates the identification of any unique features present in affected leaves.

* **Prediction**: Construct a machine learning (ML) model capable of predicting whether a cherry leaf is healthy or infected with powdery mildew, based on visual cues extracted from the images.

#### Rationale
* **Data Visualization**: Employing visual analysis of the dataset aids in comprehending the characteristics and disparities within healthy and afflicted cherry leaves, facilitating the selection and extraction of relevant features for model development.

* **ML Tasks**: Implementing Convolutional Neural Networks (CNNs) harnesses the power of deep learning to automatically discern and recognize intricate patterns within images, thereby enabling precise classification between healthy and affected leaves.


## ML Business Case
* **Enhanced Efficiency**: The adoption of a machine learning (ML) system for immediate identification of powdery mildew on cherry leaves leads to a substantial reduction in manual inspection time, thereby enhancing the overall efficiency of the process.

* **Scalability & Reproducibility**: Achieving success in this initiative has the potential to facilitate the deployment of comparable ML-driven detection systems for various other crops. This would bolster scalability and reproducibility across diverse agricultural contexts.


## Dashboard Design

### **Project Overview**

* Provides an extensive summary of powdery mildew, a fungal disease impacting cherry trees, detailing its characteristics, effects, and management approaches.
* Describes powdery mildew as a fungal infection affecting various plants, notably cherry trees, thriving in warm, humid conditions.
* Explains its appearance as a powdery, white growth on leaves, shoots, and sometimes on the fruit.
* Notes that the dataset is acquired from Kaggle and includes images of both healthy cherry leaves and leaves affected by powdery mildew.
* Encourages readers to refer to the Project README file for additional information.
* Highlights the project's primary business requirements: 
* Visually differentiating between healthy and powdery mildew-infected cherry leaves 
* Developing a predictive model for leaf health assessment.

#### **Dataset Details**

* Obtained from Kaggle, comprising over 4,000 images from the client's crop fields, showcasing healthy and powdery mildew-infected cherry leaves.
* Promotes exploration of the dataset and encourages reading of the README file for deeper insights.

#### **Business Objectives**

* The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### **Project Hypothesis**

* States that powdery mildew-affected cherry leaves display distinct visual patterns, particularly along the leaf edges, distinguishing them from healthy leaves.
* Emphasizes the identification of these unique patterns and proposes validation through exploratory data analysis (EDA) on the dataset, including visualization of healthy and affected cherry leaf samples.

### **Leaf Visualizer**

* Generates healthy and mildew-infected leaves for visual comparison, aiding in distinguishing between the two.
* Allows users to refresh the montage, select labels for viewing specific subsets of images, and adjust montage sizes.
* Provides a grid of randomly selected images based on chosen labels for visual inspection.

#### **Visual Contrast**

* Discernible variances are noted between typical and variant images.
* The shapes of both powdery mildew-infected and healthy leaves remain identifiable.
* Notable variations in color distinguish between healthy and powdery mildew-infected leaves, with healthy leaves displaying a more vibrant green hue.
* Users can update the montage by activating the 'Create Montage' option.
* The tool permits users to choose labels to view specific image subsets.
* It presents a grid of randomly selected images corresponding to the selected label.
* Users can customize montage dimensions by adjusting the number of rows and columns.

### **Mildew Identification**

* The client's aim is to ascertain whether a specific leaf is afflicted by mildew.

#### **Real-Time Prediction & Data Retrieval**
* Enables users to upload samples of mildew-infected leaves for immediate prediction.

* Offers the choice to acquire a collection of mildew-infected and healthy leaf images from Kaggle.

#### **Real-Time Prediction Feature**
* Users have the option to upload individual or multiple leaf images for assessment.

* Provides details regarding the uploaded image(s) such as name and size.

* Adjusts the size of the uploaded image(s) to fit the prediction model (via the resize_input_image function).

* Utilizes a pre-existing model to forecast the likelihood and classification of mildew infection (through the load_model_and_predict function).

* Visualizes the predictions and their corresponding probabilities (via the plot_predictions_probabilities function).

#### **Analysis Report**

* Produces a report table presenting the names of uploaded images alongside their respective prediction outcomes.

* Offers the choice to download the report as a CSV file.

### **ML Performance**

#### **Train, Validation, & Test Set Label Distribution**
* Illustrates the distribution of labels across the training, validation, and test datasets through an image display.

#### **Model Progression**
* Graphically represents the training accuracy and losses of the model throughout its training period.

* Consists of distinct images illustrating the model's training accuracy (model_training_acc.png) and training losses (model_training_losses.png).

#### **Overall Performance on Test Set**
* Offers a structured presentation of the model's evaluation metrics on the test dataset.

* Retrieves and showcases the evaluation outcomes for loss and accuracy using the load_test_evaluation function.


## Bugs
* I didn't encounter any bugs during this project.

## Unfixed Bugs
* There is no unfixed bugs.

## Testing
* In this project, only manual testing has been conducted. The functionality of all aspects of the application has been verified on Heroku, and they operate as intended.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis & Machine Learning Libraries
* NumPy: NumPy stands as a cornerstone package for scientific computation in Python, furnishing comprehensive support for arrays, matrices, and a suite of mathematical functions tailored for operation on these arrays. In this project, NumPy is extensively employed during data preparation tasks.

* Pandas: Integral for data manipulation, cleansing, and analysis, Pandas is instrumental in facilitating various operations such as loading datasets, refining data, conducting exploratory data analysis (EDA), and structuring data for modeling purposes.

* Matplotlib, employed in conjunction with Seaborn, is utilized to craft customizable and high-quality plots and visualizations, offering precise control over the visual aspects of graphical representations.

* Seaborn: Seaborn, renowned for its capacity to craft visually captivating statistical visualizations, plays a pivotal role in producing diverse plots and statistical graphics to elucidate patterns or relationships inherent within the data.

* Streamlit: Streamlit, a Python library, is employed to develop web applications tailored for data science and machine learning ventures, streamlining the conversion of data scripts into accessible web applications. Within this project, Streamlit serves as a dashboard interface.

* Jupyter: Jupyter, an open-source web application, allows users to author and distribute documents containing live code, mathematical equations, visualizations, and narrative text. Throughout this project, Jupyter serves as an open integrated development environment (IDE) utilized during data collection and machine learning phases to enhance visualization of the processes.

* Tensorflow: TensorFlow, an open-source machine learning framework created by Google, is extensively utilized for constructing and training machine learning models. Within this project, TensorFlow played a crucial role in the machine learning phase, particularly during the training of the model.

## Credits 

* The entirety of the code utilized in this project originates from the Malaria Detector tutorial video series included in the course material. I followed the video series to create the notebooks and dashboard, making adjustments to the code to suit my project's requirements. The initial template for starting the project is based on the one provided in the course material.

### Content 

The content presented on the project summary page draws inspiration from:
- [Treefruit](https://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/#:~:text=Powdery%20mildew%20of%20sweet%20and,1)
- [Garden Design](https://www.gardendesign.com/how-to/powdery-mildew.html)
- [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew)

## Acknowledgements
* Thank the people that provided support throughout this project.
