from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt,question])
    return response.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=['You are an expert in converting English questions to SQL query!',
 'The SQL database has the name EMPLOYEE and has the following columns - NAME, BIRTHDATE, LEVEL AND HIRING DATE',
 'For example,',
 'Example 1 - How many entries of records are present?',
 'The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;',
 'Example 2 - Tell me all the employees are of level 1?',
 'The SQL command will be something like this: SELECT * FROM EMPLOYEE WHERE LEVEL="ONE";',
 'Also, the SQL code should not have ``` in the beginning or end, and "sql" word should not be in the output.']


## Streamlit App

st.set_page_config(page_title="Text-to-Query-Gemini-Pro")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"samp_employee.db")
    st.subheader("Response from database")
    for row in response:
        print(row)
        st.header(row)