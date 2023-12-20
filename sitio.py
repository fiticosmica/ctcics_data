import streamlit as st 
import requests 
from streamlit_lottie import st_lottie
from PIL import Image 

# funcion wea de animacion de lottie
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None #si la solicitud no está disponible
  return r.json()

lottie_coding = load_lottieurl("https://lottie.host/622dd294-8daf-4b01-b724-2afe598896f2/OpsEJSLUwN.json")
img_ctci = Image.open("/content/Marca-CTCI.png")

with st.container():
  st.image(img_ctci, width=200)
  st.title("CTCI Nodo centro sur")
  st.write("El objetivo general es co-crear un modelo de Ciencia Abierta para fortalecer el desarrollo de la ciencia y tecnología en la Macrozona Centro Sur de Chile en concordancia con su territorio y sociedad.")
  st.write("[Más información >](https://www.ctci.cl/)") #vinculo web
  st.write("---")

with st.container():
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("lorem ipsum")
    st.write("texto texto texto")
  with right_column:
    st.header("lorem impsu")
    st.write("texto texto texto")
