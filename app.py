import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
st.title("Laptop Price Prediction")

Brand = st.selectbox('Brand', df['Brand'].unique())
ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32])
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
Processor = st.selectbox('Processor', df['Processor brand'].unique())
ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024, 2048])
os = st.selectbox('OS', df['OS'].unique())
screensize = st.selectbox('Screen Size(in inch)', ['15.60', '14.00', '16.00', '13.30', '13.40', '17.30',
                                                   '16.10', '14.96', '13.60'])

if st.button('Predict Price'):

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    query = np.array([os, screensize, Brand, ram, touchscreen, Processor, ssd])
    query = query.reshape(1, 7)
    st.title("The predicted price of this configuration is " + str(int(np.exp(model.predict(query)[0]))))
