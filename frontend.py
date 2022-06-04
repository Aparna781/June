import streamlit as st
import firebase_admin
from firebase_admin import db
@st.cache
def runonce():
    cred=firebase_admin.credentials.Certificate('key.json')
    app=firebase_admin.initialize_app(cred,{"databaseURL":"https://june-819f7-default-rtdb.firebaseio.com/"})

runonce()
mymenu=st.sidebar.selectbox("MENU",("Home","Exam","Marksheet","Information"))
st.title("Student Management System")
if(mymenu=="Exam"):
    st.text("This Project is Developed by Aparna Mishra")
    st.markdown('<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSetmK33qwQjGSfe93f7b3HyFdpe_tDppabOcnOHrcLBDsw9vQ/viewform?embedded=true" width="640" height="1484" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>',unsafe_allow_html=True)
elif(mymenu=="Marksheet"):
    with st.form("Marksheet Form"):
        rollno=st.text_input("Enter Your Roll No")
        k=st.form_submit_button("Submit")  
        if k:
            ref=db.reference('/Marks/'+rollno).get()
            st.header("Marksheet") 
            st.table({'Marks':{"English":ref['English'],"Science":ref['Science'],"Maths":ref['Maths']},'Total':{"English":100,"Science":100,"Maths":100}})
            st.write("English:",ref['English']) 
            st.write("Maths:",ref['Maths'])       
            st.write("Science:",ref['Science'])       
            st.subheader("Result:"+ref['Result'])       
                   
    st.image("https://miro.medium.com/max/1400/1*1F2CGO_OyhOnp397-1ysNw.gif")
elif(mymenu=="Information"):
    with st.form("Information"):
        rollno=st.text_input("Enter Your Roll No")
        k=st.form_submit_button("Submit")  
        if k:
            ref=db.reference('/Information/'+rollno).get()
            st.header("Student Information") 
            st.write("Name:",ref['Name']) 
            st.write("Age:",ref['Age'])       
            st.write("City:",ref['City'])       
            st.write("Email id:"+ref['Email id'])      
            st.video("https://www.youtube.com/watch?v=HseGVOM85W4")

