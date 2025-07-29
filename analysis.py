import os
import streamlit as st 
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

from pdf import extractpdf
# configure the api key
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

# call the model
model = genai.GenerativeModel('gemini-1.5-flash')

# create the def fn to analyze the pdf and JD

def analyze_resume(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc)
        st.write('Extracted successfully 🤩')
    else:
        st.warning('Drop file in PDF format')
    
    ats_score = model.generate_content(f'''Compare the resume {pdf_text} with job desc
                           {job_desc} and get ATS score''')
    good_fit = model.generate_content(f'''Compare the resume {pdf_text} with the job description 
                                       {job_desc} and say if I am a good fit for the job or not.
                                       Generate results in bullet points''')
    swot_analysis = model.generate_content(f'''Compare the resume {pdf_text} with the job description 
                                       {job_desc} and provide SWOT analysis. 
                                       Generate results in bullet points''')
    prob = model.generate_content(f'''Compare the resume {pdf_text} with the job description 
                                       {job_desc} and give the probability(in percent) of getting hired.
                                       Generate results in bullet points''')
    
    return {st.write(ats_score.text), st.write(good_fit.text),
            st.write(swot_analysis.text), st.write(prob.text)}