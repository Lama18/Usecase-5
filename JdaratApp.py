import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# CSV
df = pd.read_csv(r"C:\Users\Lama\OneDrive\سطح المكتب\Twaiq\week1\Usecase-5\Jadarat_data2.csv")

st.image("gra.jpg", width=200, use_column_width=True)

st.markdown("<h1 style='text-align: right;'>خريج وتايه بين إعلانات الوظايف !؟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right;'>جيت للمكان الصح</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right;'>بناخذ بيدك للطريق الي بتبدا فيه مسيرتك المهنية وبنوضح لك وش هي توجهات سوق العمل وتطمن احنا معك خطوة بخطوة</h4>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: right;'>اول خطوة خلينا نعرف قد ايش سوق العمل مهتم بالخريجين حديثا</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right;'>مثل ما تشوف بالرسم البياني 60% من الوظايف الحالية لا تتطلب خبرة يعني ودهم فيك وبمهاراتك</h4>", unsafe_allow_html=True)

# experines year
experience_counts = df['exper'].value_counts(normalize=True) * 100
experience_df = experience_counts.reset_index()
experience_df.columns = ['experience_years', 'percentage']

# create Plotly
fig_experience = px.bar(
    experience_df, 
    x='experience_years', 
    y='percentage', 
    title='Job Opportunities: Experience vs Fresh Graduates',
    labels={'experience_years': 'Years of Experience', 'percentage': 'Percentage of Job Postings'}
)

# show Streamlit
st.plotly_chart(fig_experience)

st.markdown("<h4 style='text-align: right;'>نطمنك ان الوظايف في المملكة تبغاك سوى كنت بنت ولا ولد مثل ماتشوف بالرسم لبياني </h4>", unsafe_allow_html=True)

gender_counts = df['gender'].value_counts(normalize=True) * 100
gender_df = gender_counts.reset_index()
gender_df.columns = ['gender', 'percentage']

# create Plotly
fig = px.pie(gender_df, values='percentage', names='gender', title='Gender Preference in Job Postings')

# show Streamlit
st.plotly_chart(fig)

st.markdown("<h3 style='text-align: right;'>اخيرا ينشوف سلم الرواتب للموظفين حديثي التخرح </h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right;'>مثل ماواضح في الرسم البياني ان حديثي التخرج تراوح رواتبهم من 4000 الى 6000</h4>", unsafe_allow_html=True)

# salary for fresh graduating 
fresh_graduates_df = df[df['exper'] == 0]
fresh_graduates_df['salary'] = pd.to_numeric(fresh_graduates_df['salary'], errors='coerce')
fresh_graduates_df = fresh_graduates_df.dropna(subset=['salary'])
st.write("Number of rows for fresh graduates:", len(fresh_graduates_df))
fig_salary_box = px.box(
    fresh_graduates_df, 
    y='salary', 
    title='Salary Distribution for Fresh Graduates (Box Plot)', 
    labels={'salary': 'Salary'}
)
st.plotly_chart(fig_salary_box)
