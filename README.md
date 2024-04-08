# Cherry Leaves
* Powdery mildew is a common fungal disease affecting a wide variety of plants, caused by diverse species of ascomycete fungi in the Erysiphales order. Its identification is relatively simple due to distinctive symptoms such as white powdery spots on leaves and stems. Although lower leaves are often most affected, the mildew can appear on any above-ground part of the plant. As the disease progresses, the spots enlarge and become denser due to the formation of numerous asexual spores, potentially spreading throughout the plant. This fungus thrives in environments with high humidity and moderate temperatures, making greenhouses particularly susceptible to its spread, posing a threat to agricultural and horticultural practices. Control methods include chemical treatments, bio-organic approaches, and genetic resistance.

* In agricultural settings, powdery mildew can be managed through various methods such as chemical control, genetic resistance, and employing careful farming practices. To prevent the disease, farmers can choose powdery mildew-resistant plant varieties and alternate between resistant and susceptible varieties to hinder pathogen adaptation. Additionally, reducing humidity by spacing plants for airflow and pruning foliage can help mitigate its spread. Conventional chemical control involves the use of standard fungicides, with spray programs recommended upon initial detection of symptoms. Regular application of fungicides like triadimefon, propiconazole, hexaconazole, myclobutanil, and penconazole is advised for optimal results. Non-conventional methods include utilizing substances like milk, natural sulfur, potassium bicarbonate, metal salts, and oils, each offering alternative modes of action against powdery mildew. Metal salt fungicides should be applied regularly until harvest, sulfur should be applied preemptively to inhibit spore germination, and copper sulfate, although effective in organic farming, may require lime to mitigate its adverse effects on plants.

* The goal is to create a ML model that can predict if a cherry leaf is infected with powdery mildew or uninfected. The model need to have a accuracy rate of minimum 97% and my model reached 100% accuracy.

## Dataset Content
* The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). I created a user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains over four thousand images taken from the client's cherry plantation. The images show healthy cherry leaves and leaves that have been infected with powdery mildew. Since the cherry plantation crop is one of the finest products in the client's portfolio, the quality of the product is of high concern for the company.

## Business Requirements

Farmy & Foods is grappling with powdery mildew affecting their cherry plantation crop, leading to inefficient manual inspection processes. Employees spend 30 minutes per tree visually identifying and treating infected trees with a specific compound. With thousands of cherry trees spread across multiple farms, scalability becomes a significant issue. To address this, the IT team proposes implementing a machine learning (ML) system to instantly detect powdery mildew in cherry trees using leaf images. Success in this endeavor could pave the way for similar initiatives in detecting pests in other crops, utilizing datasets comprising cherry leaf images provided by Farmy & Foods.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?

### Hypothesis
* Cherry tree foliage afflicted by powdery mildew displays unique visual characteristics when contrasted with the appearance of healthy cherry leaves.

### Validation
* Dataset Examination: Confirm the hypothesis through exploratory data analysis (EDA) of the dataset, employing techniques like visualizing samples of both healthy and powdery mildew-affected cherry leaves to detect any discernible patterns or distinctions.

* Model Creation: Develop a machine learning (ML) model utilizing Convolutional Neural Networks (CNNs) to discern between healthy and powdery mildew-infected cherry leaves. Validate the model's efficacy and performance using suitable validation methods.

* Assessment: Assess the model's effectiveness on an independent test set to verify its capacity to generalize. Utilize metrics like accuracy to gauge its proficiency in identifying powdery mildew.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

#### Business requirements
* Visual Discrimination: Utilize visual representations of cherry leaf images to distinguish between healthy leaves and those afflicted by powdery mildew. This facilitates the identification of any unique features present in affected leaves.

* Prediction: Construct a machine learning (ML) model capable of predicting whether a cherry leaf is healthy or infected with powdery mildew, based on visual cues extracted from the images.

#### Rationale
* Data Visualization: Employing visual analysis of the dataset aids in comprehending the characteristics and disparities within healthy and afflicted cherry leaves, facilitating the selection and extraction of relevant features for model development.

* ML Tasks: Implementing Convolutional Neural Networks (CNNs) harnesses the power of deep learning to automatically discern and recognize intricate patterns within images, thereby enabling precise classification between healthy and affected leaves.


## ML Business Case
* Enhanced Efficiency: The adoption of a machine learning (ML) system for immediate identification of powdery mildew on cherry leaves leads to a substantial reduction in manual inspection time, thereby enhancing the overall efficiency of the process.

* Scalability and Reproducibility: Achieving success in this initiative has the potential to facilitate the deployment of comparable ML-driven detection systems for various other crops. This would bolster scalability and reproducibility across diverse agricultural contexts.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

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


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
