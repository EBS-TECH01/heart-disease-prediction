
import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:Red;padding:16px">
    <h2 style="color:black;text-align:center">Heart Disease Prediction Using ML</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Load the model
    model = joblib.load('model_heart_disease')

    # Input fields
    p1 = st.slider('Enter your Age', 18, 100)
    
    s1 = st.selectbox('Sex', ('Male', 'Female'))
    p2 = 1 if s1 == 'Male' else 0  # Convert to numeric format
    
    p3 = st.slider('Enter your cp', 0, 3)
    
    p4 = st.number_input('Enter Your trestbps', min_value=0)
    
    p5 = st.number_input('Enter Your chol', min_value=0)
    
    p6 = st.number_input('Enter Your fbs (0 for False, 1 for True)', 0, 1)
    
    p7 = st.number_input('Enter your restecg', 0, 2)
    
    p8 = st.number_input('Enter Your thalach', min_value=0)
    
    p9 = st.number_input('Enter Your exang (0 for No, 1 for Yes)', 0, 1)
    
    p10 = st.number_input('Enter Your oldpeak', min_value=0.0, step=0.1)
    
    p11 = st.number_input('Enter Your slope', 0, 2)
    
    p12 = st.number_input('Enter Your ca', 0, 4)
    
    p13 = st.number_input('Enter Your thal', 0, 3)
    
    pred = None  # Initialize pred before use

    if st.button('Predict'):
        pred = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]])
        
        if pred[0] == 0:
            st.success('No Heart Disease Detected ✅')
        else:
            st.warning('Possible Heart Disease Detected ⚠️')

if __name__ == '__main__':
    main()
