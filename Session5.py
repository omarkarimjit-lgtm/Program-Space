import streamlit as st
tab1, tab2, tab3 ,tab4 = st.tabs(["Home","About Us","Survey","Education Options"])
with tab1:
    st.title(":blue[*Nasr School*]",text_alignment="center")
with tab2:
    st.title(":blue[*About Us*]",text_alignment="center")
    with st.expander("Click Here To Know More About Us"):
        st.write("Nasr School is a leading educational institution committed to providing high-quality education and fostering holistic development in students. Our dedicated faculty, state-of-the-art facilities, and innovative teaching methods ensure that every child receives a well-rounded education that prepares them for future success.")
    with st.expander("Click Here To Contact Us"):
        st.write("For inquiries, please reach out to us at info@nasrschool.edu.eg")

with tab3:
    st.title(":blue[*Survey*]",text_alignment="center")
    st.text_input("Enter Your  child's Name: ",placeholder="Enter Your Name Here",max_chars=30)
    st.slider("Enter Your child's Age: ",min_value=1,max_value=22,step=1)
    st.radio("Select Your Child's Education Level: ",options=["Primary School","Secondary School","High School","University"])
    st.selectbox("Select Your Child's Gender: ",options=["Male","Female"])
    

with tab4:
    st.title(":blue[*Education Options*]",text_alignment="center")
    st.slider("Select Your price range:",min_value=30000,max_value=245000,step=1000,value=(30000,245000))

