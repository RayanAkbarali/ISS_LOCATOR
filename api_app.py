import streamlit as st
import requests as rq
import reverse_geocode as rg
import pandas as pd
url = "http://api.open-notify.org/iss-now.json"

def main():
    st.title("ISS location")
    st.markdown("This app tracks tracks ISS in real time")
    city, state, country, lat, lon = get_iss_location()
    st.write(f"Latitude: {lat}, Longtiude: {lon}")
    st.write(f"City: {city}")
    st.write(f"State: {state}")
    st.write(f"Country: {country}")
    df = pd.DataFrame({
        "lat":[float(lat)],
        "lon": [float(lon)]
    })
    st.map(df)
    st.write("developed by Rayan")

def get_iss_location():
    response = rq.get(url)
    data = response.json()
    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]
    # print(lat, lon)
    # print(lat, lon)
    place_dict = rg.get((lat, lon))
    city = place_dict["city"]
    state = place_dict["state"]
    country = place_dict["country"]
    return city,state,country,lat,lon

if __name__ == "__main__":
    main()