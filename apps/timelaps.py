import streamlit as st
from pathlib import Path
import os
import ast
import ee, geemap
import geemap.foliumap as geemap
geemap.ee_initialize()

## change loop to include more loops xD
st.session_state['roi'] = None
st.session_state['frequency'] = None
st.session_state['data_collection'] = None
st.session_state['file_name'] = None
st.session_state['start_year'] = None
st.session_state['end_year'] = None
st.session_state['start_date'] = None
st.session_state['end_date'] = None
st.session_state['end_date'] = None

work_dir = "./artefacts"
if not os.path.exists(work_dir):
    os.makedirs(work_dir)


def app():

    st.title("Time Laps")
    st.info('Draw a rectangle on the map and customize timelaps parameters, and then click on the submit button.', icon=None)
    Map = geemap.Map() 
    Map.to_streamlit()

    with st.form("timelaps parameters", clear_on_submit=False):
        col1, col2, col3 = st.columns(3)
        st.session_state['data_collection']  = col1.selectbox("Select a satellite image collection", 
                                                              ["Landsat TM-ETM-OLI Surface Reflectance", 
                                                              "Sentinel-2 MSI Surface Reflectance"
                                                              ]) 
        
        st.session_state['frequency'] = col2.selectbox("Select the data frequency", 
                                                              ["month", 
                                                               "quarter", 
                                                               "year"
                                                               ]) 
        
        st.session_state['file_name'] = col3.text_input("File Name", "")
    
        geometry_coords = st.text_input("ROI", "")
        if geometry_coords:
            st.session_state['roi'] = ee.FeatureCollection([ee.Feature(ee.Geometry.Polygon(
                ast.literal_eval(geometry_coords)
                ))])   

        col1, col2, col3, col4 = st.columns(4)
        st.session_state['start_year'] = col1.text_input("Steart Year", "YYYY")
        st.session_state['start_date'] = col2.text_input("Start Date of the Year", "MM-DD")

        st.session_state['end_year'] = col3.text_input("End Year", "YYYY")
        st.session_state['end_date'] = col4.text_input("End Date of the Year", "MM-DD")

        create_account_button = st.form_submit_button("Create Timelaps")


        
        if create_account_button: 
            out_gif = os.path.join(work_dir, st.session_state['file_name'] + ".gif")

            if st.session_state['data_collection'] == "Landsat TM-ETM-OLI Surface Reflectance":
                st.write('Landsat')
                collection = geemap.landsat_timeseries(roi=st.session_state['roi'], 
                                                        start_year=int(st.session_state['start_year']), 
                                                        end_year=int(st.session_state['end_year']), 
                                                        start_date=st.session_state['start_date'], 
                                                        end_date=st.session_state['end_date'],
                                                        frequency = st.session_state['frequency']
                                                    )
                # Define arguments for animation function parameters.
                video_args = {
                    'dimensions': 768,
                    'region': st.session_state['roi'],
                    'framesPerSecond': 120,
                    'bands': ['Red', 'Green', 'Blue'],
                    'min': 0,
                    'max': 0.3,
                    'gamma': [1, 1, 1],
                }
                geemap.download_ee_video(collection, video_args, out_gif)

            else:
                st.write('S2')
                collection = geemap.sentinel2_timelapse(roi=st.session_state['roi'], 
                                                        out_gif=out_gif, 
                                                        start_year=int(st.session_state['start_year']), 
                                                        end_year=int(st.session_state['end_year']), 
                                                        start_date=st.session_state['start_date'], 
                                                        end_date=st.session_state['end_date'], 
                                                        bands=['Red', 'Green', 'Blue'], 
                                                        frames_per_second=120,  
                                                        frequency=st.session_state['frequency'], 
                                                        title=st.session_state['file_name'],
                                                        mp4=True)
                                                
            # create a Path object with the path to the file
            path = Path(out_gif)
            if path.is_file():
                st.success("The timelaps is successfully saved!")
                geemap.gif_to_mp4(out_gif, out_gif.replace('.gif', '.mp4'))
                video_file = open(out_gif.replace('.gif', '.mp4'), 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)
            
            else:
                st.error('An error occurred while downloading. User memory limit exceeded.')
