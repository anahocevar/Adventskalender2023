import streamlit as st

def app():

    # UPDATE days dict every day
    days = {"1 December": "https://media.tenor.com/SX4QflcMDKsAAAAd/baby-snow.gif",
            "2 December": "https://64.media.tumblr.com/2a6a2c0be28ab9b42f83c9ce45cb69a3/6d71e206c2329a31-77/s250x400/b5c7d4d5bddb0c733f65ef06897d652728ea1609.gif",
            "3 December": "https://i.redd.it/qtf4widt5w771.gif",
            "4 December": "https://jungleroots.wpengine.com/wp-content/uploads/2022/08/ab3a60_1a955129a34441e5bd0492e8fb33617a_mv2.gif",
            "5 December": "https://media1.giphy.com/media/NVu7FsmRTtn2nyRwJr/giphy.gif",
            "6 December": "https://www.gannett-cdn.com/experiments/usatoday/polar-bears/static/img/surprise-baby-polar-bears-compressed.gif",
            "7 December": "https://i.imgur.com/I0Uktjg.gif",
            "8 December": "https://media2.giphy.com/media/Q3cJvgxtBUtqg/giphy.gif?cid=ecf05e47qalrhpvi5m7icbmzsm4fmekxphbx378al6ab8k5b&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "9 December": "https://i.gifer.com/ENwD.gif",
            "10 December": "https://media.tenor.com/Y7QklzR9M1oAAAAM/snow-dog.gif",
            "11 December": "https://giffiles.alphacoders.com/477/47727.gif",
            "12 December": "https://media4.giphy.com/media/140LiNgM0b5DVe/giphy.gif?cid=ecf05e470da0g2d06n8quhmlkv1knlwef4kw4ig2w5wuwgsp&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "13 December": "https://media.tenor.com/9i0ybGpGPoIAAAAC/fox.gif",
            "14 December": "https://i.gifer.com/OuBq.gif",
            "15 December": "https://i.pinimg.com/originals/28/94/50/2894501b7551293d410858b646cdccba.gif",
            "16 December": "https://media1.giphy.com/media/ZdlSqZuzzMB1JT3nwT/giphy.gif",
            "17 December": "https://i.chzbgr.com/full/8474428672/h87705AF7/dachshund-winter-fun",
            "18 December": "https://media2.giphy.com/media/133c9SJrrC2bni/giphy.gif",
            "19 December": "https://www.gannett-cdn.com/experiments/usatoday/polar-bears/static/img/baby-polar-bears-with-mom-compressed.gif",
            "20 December": "https://i.redd.it/fpai1w2l1y501.gif"}

    index = len(days) - 1
    day_picked = str(index+1) + " December"
    
    with st.sidebar:
        day_picked = st.radio(
          "",
            tuple(days.keys()), index=index
    )    
           
    st.title(day_picked)
    st.image(
            days[day_picked],
            width=300, # Manually Adjust the width of the image as per requirement
        )
    
if __name__ == '__main__':
    app()
