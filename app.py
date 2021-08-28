import streamlit as st
import pickle 
import numpy as np
from sklearn.linear_model import LogisticRegression
import tensorflow as tf
import keras

json_model = open("model.json","r").read()
model = keras.models.model_from_json(json_model,custom_objects={'Functional':tf.keras.models.Model})
model.load_weights("model.h5")
#model = keras.models.load_model('AutoEncoder.h5' ,custom_objects={'Functional':tf.keras.models.Model})
#model = pickle.load(open('saved_model.pb','rb'))

def predict_recepie(Recepies_list_ip):
    #input=np.array([Recepies]).astype(np.float64)
    input1=Recepies_list_ip
    vec=np.random.rand(1,10)
    prediction = model.predict([vec,input1])
    
    return prediction
    
def main():
    st.title("Pizza Predictor")
    Recepies=("None","bbq topping", "havarti kryddostur", "almond", "pineapple", "apple", "artichoke", "asparagus", "avocado", "banana", "basil", "bean", "bean_black", "beef", "bacon", "bell_pepper", "black_pepper", "black_tea", "blue_cheese", "broccoli", "rice", "buckwheat", "butter", "buttermilk", "cabbage", "caraway", "caraway_seed", "carrot", "cauliflower", "cayenne", "celery", "cheddar", "cherry", "chicken", "chile_oil", "chili", "chive_mince", "clove", "coconut", "cilantro", "corn", "cornmeal", "cornstarch", "crab", "cracker", "cranberry", "cream", "cream_cheese", "cucumber", "cumin", "dill", "dried_tomato", "dried_parsley", "egg", "eggplant", "fennel", "fenugreek", "feta_cheese", "fig", "garlic", "garlic_oil", "ginger", "gluten_flour", "goat_cheese", "grape", "green", "green_bell_pepper", "green_olive", "gum", "ham", "honey", "jalapeno", "ketchup", "lamb", "lemon", "lettuce", "lime", "lobster", "macaroni", "mango", "marjoram", "mashed_potato", "mayonnaise", "meat", "date", "mint", "mozzarella", "mushroom", "nachos", "nut_pine", "nutmeg", "olive", "olive_oil", "onion", "orange", "oregano", "oyster", "parsley", "pasta", "peach", "peanut", "peanut_butter", "pear", "pecan", "pepperoni", "pesto", "pimento", "piparostur", "pistachio", "plum", "pork", "potato", "powder", "provolone_cheese", "pumpkin", "red_lentil", "red_onion", "red_pepper", "rosemary", "rye_bread", "salad", "salami", "salsa", "salt", "sauce_pesto", "sauerkraut", "sausage", "scallion", "seafood", "seed", "sesame_oil", "sesame_seed", "shallot", "shiitake", "shortening", "shrimp", "smoked_salmon", "soy_sauce", "spaghetti", "spinach", "squash", "sriracha", "starch", "steak", "sugar", "sweet_potato", "taco", "tarragon", "thyme", "tofu", "tomato", "tortilla", "turkey", "turmeric", "vegan_cheese", "vegetable_oil", "vinegar", "walnut", "wine", "yeast", "yogurt", "zucchini")
    Recepies_duplicate=("None","bbq topping", "havarti kryddostur", "almond", "pineapple", "apple", "artichoke", "asparagus", "avocado", "banana", "basil", "bean", "bean_black", "beef", "bacon", "bell_pepper", "black_pepper", "black_tea", "blue_cheese", "broccoli", "rice", "buckwheat", "butter", "buttermilk", "cabbage", "caraway", "caraway_seed", "carrot", "cauliflower", "cayenne", "celery", "cheddar", "cherry", "chicken", "chile_oil", "chili", "chive_mince", "clove", "coconut", "cilantro", "corn", "cornmeal", "cornstarch", "crab", "cracker", "cranberry", "cream", "cream_cheese", "cucumber", "cumin", "dill", "dried_tomato", "dried_parsley", "egg", "eggplant", "fennel", "fenugreek", "feta_cheese", "fig", "garlic", "garlic_oil", "ginger", "gluten_flour", "goat_cheese", "grape", "green", "green_bell_pepper", "green_olive", "gum", "ham", "honey", "jalapeno", "ketchup", "lamb", "lemon", "lettuce", "lime", "lobster", "macaroni", "mango", "marjoram", "mashed_potato", "mayonnaise", "meat", "date", "mint", "mozzarella", "mushroom", "nachos", "nut_pine", "nutmeg", "olive", "olive_oil", "onion", "orange", "oregano", "oyster", "parsley", "pasta", "peach", "peanut", "peanut_butter", "pear", "pecan", "pepperoni", "pesto", "pimento", "piparostur", "pistachio", "plum", "pork", "potato", "powder", "provolone_cheese", "pumpkin", "red_lentil", "red_onion", "red_pepper", "rosemary", "rye_bread", "salad", "salami", "salsa", "salt", "sauce_pesto", "sauerkraut", "sausage", "scallion", "seafood", "seed", "sesame_oil", "sesame_seed", "shallot", "shiitake", "shortening", "shrimp", "smoked_salmon", "soy_sauce", "spaghetti", "spinach", "squash", "sriracha", "starch", "steak", "sugar", "sweet_potato", "taco", "tarragon", "thyme", "tofu", "tomato", "tortilla", "turkey", "turmeric", "vegan_cheese", "vegetable_oil", "vinegar", "walnut", "wine", "yeast", "yogurt", "zucchini")
    Recepies_list_ip=np.zeros((1,len(Recepies)-1))
    html_temp = """
    <div style="background:#fa8e72 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Get your Pizza!!! </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    option1 = st.selectbox('Would you like to ban any receipe',Recepies,key = "1")
    if option1!='None':
        Recepies_duplicate=list(Recepies_duplicate)
        Recepies_duplicate.remove(option1)
        Recepies_list_ip[0,Recepies.index(option1)-1]=-1
    option2 = st.selectbox('Would you like to ban any receipe',Recepies_duplicate,key = "2")
    if option2!='None':
        Recepies_duplicate=list(Recepies_duplicate)
        Recepies_duplicate.remove(option2)
        Recepies_list_ip[0,Recepies.index(option2)-1]=-1
    option3 = st.selectbox('Would you like to ban any receipe',Recepies_duplicate,key = "3")
    if option3!='None':
        Recepies_duplicate=list(Recepies_duplicate)
        Recepies_duplicate.remove(option3)
        Recepies_list_ip[0,Recepies.index(option3)-1]=-1
    option4 = st.selectbox('Would you like to ban any receipe',Recepies_duplicate,key = "4")
    if option4!='None':
        Recepies_duplicate=list(Recepies_duplicate)
        Recepies_duplicate.remove(option4)
        Recepies_list_ip[0,Recepies.index(option4)-1]=-1
    option5 = st.selectbox('Would you like to ban any receipe',Recepies_duplicate,key = "5")
    if option5!='None':
        Recepies_duplicate=list(Recepies_duplicate)
        Recepies_duplicate.remove(option5)
        Recepies_list_ip[0,Recepies.index(option5)-1]=-1
    
    #option11 = st.selectbox('Would you like to ban any receipe',Recepies,key = "11")
    #option12 = st.selectbox('Would you like to ban any receipe',Recepies,key = "12")
    #option13 = st.selectbox('Would you like to ban any receipe',Recepies,key = "13")
    #option14 = st.selectbox('Would you like to ban any receipe',Recepies,key = "14")
    #option15 = st.selectbox('Would you like to ban any receipe',Recepies,key = "15")
    
    #if option1!='None':
      #  Recepies=list(Recepies)
     #   Recepies.remove(option1)
    #if option2!='None':
      #  Recepies=list(Recepies)
     #   Recepies.remove(option2)
    #if option3!='None':
      #  Recepies=list(Recepies)
     #   Recepies.remove(option3)
    #if option4!='None':
        #Recepies=list(Recepies)
       # Recepies.remove(option4)
    #if option5!='None':
      #  Recepies=list(Recepies)
     #   Recepies.remove(option5)
    
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
        output = predict_recepie(Recepies_list_ip)
        
        ingredients=[]
        hated=[]
        pizza=list(range(len(Recepies)-1))
        pizza.sort(key=lambda i : output[0,i],reverse=True)
        Recepies=list(Recepies)
        for i in range(len(Recepies)-1):
            if output[0,i]>0.8 or len(ingredients)<5:
                ingredients.append(Recepies[i+1])
            if Recepies_list_ip[0,i]==-1:
                hated.append(Recepies[i+1])
        
        st.text(hated)
        st.success('Hey! here are your recipe ingredients {}'.format(ingredients))
        #st.markdown(display_receipe_html,unsafe_allow_html=True)
        #st.text(output)
        #if output == 1:
         #   st.markdown(safe_html,unsafe_allow_html=True)
        #else:
         #   st.markdown(danger_html,unsafe_allow_html=True)
            
if __name__=='__main__':
    main()
