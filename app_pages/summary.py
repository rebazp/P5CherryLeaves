import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():

    st.write("### Project Summary")

    st.info(
    f"**General Information**\n"
    f"* Powdery mildew is a common fungal disease affecting a wide variety of plants, caused by diverse species of ascomycete fungi in the Erysiphales order.\n"
    f"* Its identification is relatively simple due to distinctive symptoms such as white powdery spots on leaves and stems.\n"
    f"Although lower leaves are often most affected, the mildew can appear on any above-ground part of the plant.\n"
    f"As the disease progresses, the spots enlarge and become denser due to the formation of numerous asexual spores, "
    f"potentially spreading throughout the plant.\n"
    f"This fungus thrives in environments with high humidity and moderate temperatures, " 
    f"making greenhouses particularly susceptible to its spread, posing a threat to agricultural and horticultural practices.\n"
    f"Control methods include chemical treatments, bio-organic approaches, and genetic resistance.\n"
    f"* In agricultural settings, powdery mildew can be managed through various methods such as chemical control, genetic resistance, "
    f" and employing careful farming practices. To prevent the disease, farmers can choose powdery mildew-resistant plant varieties and "
    f" alternate between resistant and susceptible varieties to hinder pathogen adaptation."
    f" Additionally, reducing humidity by spacing plants for airflow and pruning foliage can help mitigate its spread."
    f" Conventional chemical control involves the use of standard fungicides, with spray programs recommended upon initial detection of symptoms. "
    f" Regular application of fungicides like triadimefon, propiconazole, hexaconazole, myclobutanil, and penconazole is advised for optimal results. "
    f" Non-conventional methods include utilizing substances like milk, natural sulfur, potassium bicarbonate, metal salts, "
    f" and oils, each offering alternative modes of action against powdery mildew. "
    f" Metal salt fungicides should be applied regularly until harvest, sulfur should be applied preemptively to inhibit spore germination,"
    f" and copper sulfate, although effective in organic farming, may require lime to mitigate its adverse effects on plants.\n"

    f"\n**Project Dataset:**"
    f"\nThe dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). "
    f"The dataset contains +4 thousand images taken from the client's crop fields. "
    f"The images show healthy cherry leaves and cherry leaves that have been infected with powdery mildew."
)
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/rebazp/P5CherryLeaves/blob/main/README.md).")
    
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually show the difference of "
        f"a healthy cherry leaf from one infected with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
        )