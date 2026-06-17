import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# إعداد الصفحة
st.set_page_config(layout="wide")
st.title("⚡ المختبر الهندسي الاحترافي")

# تقسيم الواجهة (تحكم في اليسار، دارة في اليمين)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🛠️ إعدادات الدارة")
    v1 = st.slider("جهد المصدر الأول (V)", 0, 20, 15)
    r1 = st.slider("المقاومة (R1)", 10, 500, 150)
    
    st.info("قم بتغيير القيم لملاحظة التغير اللحظي في توزيع التيار.")

with col2:
    st.subheader("🌐 تمثيل الدارة والنتائج")
    
    # رسم بياني احترافي للدارة باستخدام Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # رسم خطوط التوصيل
    ax.plot([0, 2, 2, 0], [0, 0, 1, 1], 'k-', lw=3) # الهيكل الأساسي
    ax.plot([1, 1], [0, 1], 'k-', lw=3) # التفرع الأوسط
    
    # إضافة النقاط (العقد)
    ax.plot([0, 1, 2], [0, 0, 0], 'ro', markersize=10)
    ax.text(1, 0.1, f"V_A = {v1/2:.2f}V", fontsize=12, fontweight='bold')
    
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 1.5)
    ax.axis('off')
    
    st.pyplot(fig)
    
    # عرض النتائج الرياضية بشكل أكاديمي
    st.latex(r"I_{total} = \frac{V}{R_1 + R_2} = \frac{" + str(v1) + "}{" + str(r1) + "} = " + str(round(v1/r1, 3)) + " A")

