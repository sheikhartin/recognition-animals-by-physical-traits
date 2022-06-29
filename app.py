import subprocess
from pathlib import Path

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


def apply_model(model: str) -> None:
    """Applies the model with selected parameters to the data."""
    st.markdown(f'##### {model.title()}')
    model = {
        'logistic regression': LogisticRegression(),
        'k-nearest neighbors': KNeighborsClassifier(),
        'support vector machine': SVC(),
        'random forest': RandomForestClassifier(),
    }.get(model)
    if model is None:
        st.error('Error while applying model...')
        return None

    for _ in range(process_reps):
        X = df[features].values
        y = df['type'].values
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size_percentage/100)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.markdown(f"**Accuracy**: {model.score(X_test, y_test)*100:.3f}<br>"
                    f"**Confusion matrix**:", unsafe_allow_html=True)
        st.dataframe(pd.DataFrame([y_test, y_pred], index=['actual', 'predicted']))


dataset_filepath = Path('data/zoo.csv')
dataset_url = 'https://raw.githubusercontent.com/sheikhartin/recognition-animals-by-physical-traits/master/data/zoo.csv'
# If the data file doesn't exist or is empty, it will be downloaded.
if not dataset_filepath.exists() or dataset_filepath.stat().st_size == 0:
    st.warning('Downloading the dataset... This may take a while.')
    dataset_filepath.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        'wget', '-q', '-O', str(dataset_filepath), dataset_url
    ])

st.set_page_config(
    page_title='Classify Animals by Their Physical Traits', page_icon='🐙',
    layout='wide', menu_items={
        'Get help': 'https://github.com/sheikhartin/recognition-animals-by-physical-traits',
        'Report a bug': 'https://github.com/sheikhartin/recognition-animals-by-physical-traits/issues/new',
        'About': ("Discover the world of animals and get to know their species. After this "
                  "I hope you do not go to the zoo to watch the imprisoned animals anymore!")})

st.title('Recognition Animals by Physical Traits')
st.markdown("""This simple app predicts the class of an animal based on its physical traits,
    and have no commercial purpose. Sorry about my dirty codes and also poor design,
    but I'm learning how to use [Streamlit](https://streamlit.io) — I don't like to work
    clean on my side projects. 🤫""")

st.sidebar.header('Manipulate Options')
classifiers = st.sidebar.multiselect(
    label='Classifiers:',
    options=['logistic regression', 'k-nearest neighbors',
             'support vector machine', 'random forest'],
    default=['logistic regression', 'k-nearest neighbors'])

features = st.sidebar.multiselect(
    label='Features:',
    options=['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic',
             'predator', 'toothed', 'backbone', 'breathes', 'venomous',
             'fins', 'legs', 'tail', 'domestic', 'catsize'],
    default=['hair', 'milk', 'breathes', 'venomous', 'legs', 'tail'])

test_size_percentage = st.sidebar.slider(
    label='Test size percentage:', min_value=10, max_value=90, value=20)

process_reps = st.sidebar.slider(
    label='Process repetitions:', min_value=1, max_value=10, value=1)

st.markdown("""
    ### Dataset

    You can download the original and pure dataset from [here](https://archive.ics.uci.edu/ml/datasets/zoo).
    The zoo dataset contains the following information:

    - **Animal name**: Unique for each instance
    - **Hair**: Boolean
    - **Feathers**: Boolean
    - **Eggs**: Boolean
    - **Milk**: Boolean
    - **Airborne**: Boolean
    - **Aquatic**: Boolean
    - **Predator**: Boolean
    - **Toothed**: Boolean
    - **Backbone**: Boolean
    - **Breathes**: Boolean
    - **Venomous**: Boolean
    - **Fins**: Boolean
    - **Legs**: Numeric (set of values between 0, 2, 4, 6, 8)
    - **Tail**: Boolean
    - **Domestic**: Boolean
    - **Catsize**: Boolean
    - **Type**: Numeric (an integer in range 1-7)""")
df = pd.read_csv(dataset_filepath)
st.dataframe(df[['animal name', *features, 'type']])

st.markdown("""
    ### Predictions

    Choose some classification models and features from the sidebar and click on the **Predict** button
    to see the models predictions and accuracy down below.

    <span style='color:orange'>*Note: This section will refresh every time you change the sidebar options.*</span>""",
    unsafe_allow_html=True)
if st.sidebar.button(label='Predict'):
    for classifier in classifiers:
        apply_model(classifier)
    st.success('All done! 🎉')

st.markdown("""
    <style>
      footer { visibility: hidden; }
      footer:after {
        visibility: visible;
        content:'Made with Streamlit and also 💙 by Artin Mohammadi from 🇮🇷';
      }
    </style>""", unsafe_allow_html=True)
