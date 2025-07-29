import streamlit as st 
from analysis import analyze_resume
st.title('CV Analyzer')
st.header('''This page helps you compare 
          your resume with the given JD''')
st.sidebar.subheader('Drop your resume here')
pdf_doc = st.sidebar.file_uploader('CLick here to browse',type=['pdf'])

st.sidebar.markdown('Designed by Feroze')
st.sidebar.markdown('enter linkedIN url here')
job_des = st.text_area('Copy paste the JD here', max_chars=10000)

submit = st.button('Generate score')

if submit:
    with st.spinner('Getting results...'):
        analyze_resume(pdf_doc,job_des)
    