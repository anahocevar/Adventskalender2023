import streamlit as st

def app():
    # UPDATE index every day
    index = 2
    day_picked = str(index+1) + " December"

    # UPDATE days dict every day
    days = {"1 December": "https://media.tenor.com/SX4QflcMDKsAAAAd/baby-snow.gif",
            "2 December": "https://64.media.tumblr.com/2a6a2c0be28ab9b42f83c9ce45cb69a3/6d71e206c2329a31-77/s250x400/b5c7d4d5bddb0c733f65ef06897d652728ea1609.gif",
            "3 December": "https://i.redd.it/qtf4widt5w771.gif"}

    # UPDATE the tuple of days in the radio every day
    with st.sidebar:
        day_picked = st.radio(
          "",
            ("1 December", "2 December", "3 December"), index=index
    )    
           
    st.title(day_picked)
    st.image(
            days[day_picked],
            width=300, # Manually Adjust the width of the image as per requirement
        )
    
if __name__ == '__main__':
    app()
