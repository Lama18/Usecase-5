import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# تحميل البيانات من ملف CSV
df = pd.read_csv(r"C:\Users\Lama\OneDrive\سطح المكتب\Twaiq\week1\Usecase-5\Jadarat_data2.csv")

# عرض الصورة في Streamlit
st.image("gra.jpg", width=200, use_column_width=True)

# النصوص التقديمية
st.markdown("<h1 style='text-align: right;'>خريج وتايه بين إعلانات الوظايف !؟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right;'>جيت للمكان الصح</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right;'>بناخذ بيدك للطريق الي بتبدا فيه مسيرتك المهنية وبنوضح لك وش هي توجهات سوق العمل وتطمن احنا معك خطوة بخطوة</h4>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: right;'>اول خطوة خلينا نعرف قد ايش سوق العمل مهتم بالخريجين حديثا</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right;'>مثل ما تشوف بالرسم البياني 60% من الوظايف الحالية لا تتطلب خبرة يعني ودهم فيك وبمهاراتك</h4>", unsafe_allow_html=True)

# حساب نسبة سنوات الخبرة
experience_counts = df['exper'].value_counts(normalize=True) * 100
experience_df = experience_counts.reset_index()
experience_df.columns = ['experience_years', 'percentage']

# إنشاء الشارت باستخدام Plotly
fig_experience = px.bar(
    experience_df, 
    x='experience_years', 
    y='percentage', 
    title='Job Opportunities: Experience vs Fresh Graduates',
    labels={'experience_years': 'Years of Experience', 'percentage': 'Percentage of Job Postings'}
)

# عرض الشارت في Streamlit
st.plotly_chart(fig_experience)

