import streamlit as st
import time
<<<<<<< Updated upstream
=======
import os
from pathlib import Path
import streamlit as st
from pathlib import PurePath
from model import final, preproc
>>>>>>> Stashed changes


st.set_page_config(
    page_title = 'Sentimental Boys Project',
    page_icon= "👦🏻",
)

st.title('The Sentimental Boys Project')
st.header('A Multimodal Sentiment Analysis on Video Clips')
st.subheader('50.038 Computational Data Science')
st.divider()


def load_video(video_file):
    vdo = open(video_file)
    return vdo

class howto():
    st.header('How to?')
    st.markdown('''
    How to use our Sentiment Analysis:
    1. Upload a video of your choice
    2. Wait for the Sentimental Boys to process your video
    3. Once processing is done, we will return you the sentiment of your video!
    
    '''            )
    st.divider()

class main():
    st.header("Please upload your video here")
    video_file = st.file_uploader('Upload',type=['mp4'])

    if video_file is not None:
        with st.spinner("Uploading..."):
            time.sleep(3)
            file_details = {"filename": video_file.name, "filetype": video_file.type, "filesize": video_file.size}
            st.write(file_details)
            video_bytes = video_file.read()
            st.video(video_bytes)
        if st.button('Process Video Now', on_click=None, type='primary'):
            with st.spinner('Processing Video...'):
<<<<<<< Updated upstream
                time.sleep(5)
                st.write("Video Processed Successfully")
                st.write("The Video Sentiment is:")
        
=======

                # audio = preproc.proc_audio('../proc_csv/raw_videos/{}'.format(video_file.name))
                # st.markdown(f"{audio}")
                # st.markdown("**The audio is sucessfully Uploaded.**")

                # face = preproc.proc_face('../proc_csv/raw_videos/{}'.format(video_file.name))
                # st.markdown(f"{face}")
                # st.markdown("**The facial is sucessfully Uploaded.**")
                
                

                # text = preproc.proc_text('../proc_csv/raw_videos/{}'.format(video_file.name))
                # st.markdown(f"{text}")
                # st.markdown("**The text is sucessfully Uploaded.**")

                video_path = '../proc_csv/raw_videos/{}'.format(video_file.name)
                video_data = final.preprocess_video(video_path)
                sentiment = final.predict_sentiment(video_path)
                st.markdown(f"Video Processed Successfully! The video sentiment is: {sentiment}")

        
                # Save uploaded file to 'F:/tmp' folder.
                save_folder = 'F:/tmp'
                save_path = Path(save_folder, video_file.name)
                with open(save_path, mode='wb') as w:
                    w.write(video_file.getvalue())

                if save_path.exists():
                    st.success(f'File {video_file.name} is successfully saved!')

                time.sleep(5)


>>>>>>> Stashed changes

