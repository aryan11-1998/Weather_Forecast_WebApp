import streamlit as st
import plotly.express as px
from backend import get_data

#Add title, text input, slider, selection box and subheader.
st.title("Weather ForeCast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days: ",min_value=1,max_value=5,help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("temperature","sky"))



if place:
    # Get the temperature/sky data
    try:
        data = get_data(place,days)
        st.subheader(f"{option} for the next {days} days in {place}")
        #Create temperature plot
        if option == "temperature":
            temp = [dict["main"]["temp"]/10 for dict in data]
            date = [dict["dt_txt"] for dict in data]

            figure = px.line(x = date,y=temp,labels={"x": "Date","y":"temperature(C)"})
            st.plotly_chart(figure)
        if option == "sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in data]
            images  = {"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            image_paths = [images[cond] for cond in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place doesn't exist.")