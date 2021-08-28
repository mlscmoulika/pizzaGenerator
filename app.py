import streamlit as st
import pickle 
import numpy as np
from sklearn.linear_model import LogisticRegression


model = pickle.load(open('Pickle_RL_Model.pkl','rb'))

def predict_recepie(Recepies):
    input=np.array([Recepies]).astype(np.float64)
    prediction = model.predict(input)
    
    return int(prediction)
    
def main():
    st.title("Pizza Predictor")
    Recepies=('None', 'cheese','banana','bacon')
    html_temp = """
    <div style="background:#fa8e72 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Get your Pizza!!! </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    option1 = st.selectbox('Would you like to ban any receipe',Recepies,key = "1")
    option2 = st.selectbox('Would you like to ban any receipe',Recepies,key = "2")
    option3 = st.selectbox('Would you like to ban any receipe',Recepies,key = "3")
    option4 = st.selectbox('Would you like to ban any receipe',Recepies,key = "4")
    option5 = st.selectbox('Would you like to ban any receipe',Recepies,key = "5")
    
    if option1!='None':
        Recepies=list(Recepies)
        Recepies.remove(option1)
    if option2!='None':
        Recepies=list(Recepies)
        Recepies.remove(option2)
    if option3!='None':
        Recepies=list(Recepies)
        Recepies.remove(option3)
    if option4!='None':
        Recepies=list(Recepies)
        Recepies.remove(option4)
    if option5!='None':
        Recepies=list(Recepies)
        Recepies.remove(option5)
    
    #safe_html ="""  
     #   <div style="background-color:#80ff80; padding:10px >
      #  <h2 style="color:white;text-align:center;"> The passenger will survive</h2>
       # </div>
        #"""
    #danger_html ="""  
     #   <div style="background-color:#80ff80; padding:10px >
      #  <h2 style="color:white;text-align:center;"> The passenger won't survive</h2>
       # </div>
        #"""
    display_receipe_html="""
        <div style="background-color:#80ff80; padding:10px >
         <h2> Here is your receipe!!
        </div>
        """
    
    if st.button("Click here and get your pizza recepie"):
        output = predict_recepie(Recepies)
        st.success('The is {}'.format(output))
        st.markdown(display_receipe_html,unsafe_allow_html=True)
        st.text(output)
        #if output == 1:
         #   st.markdown(safe_html,unsafe_allow_html=True)
        #else:
         #   st.markdown(danger_html,unsafe_allow_html=True)
            
if __name__=='__main__':
    main()