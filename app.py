import streamlit as st

def app():
    # UPDATE index every day
    index = 0
    day_picked = str(index+1) + " December"

    # UPDATE days dict every day
    days = {"1 December": "https://media.tenor.com/SX4QflcMDKsAAAAd/baby-snow.gif"}

    # UPDATE the tuple of days in the radio every day
    with st.sidebar:
        day_picked = st.radio(
          "",
            ("1 December",), index=0
    )    

    st.title(day_picked)
    st.image(
            days[day_picked],
            width=400, # Manually Adjust the width of the image as per requirement
        )
    
if __name__ == '__main__':
    app()
