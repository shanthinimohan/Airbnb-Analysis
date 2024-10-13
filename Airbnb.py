import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image


# Define a style for Garamond-Bold font with color and font size
garamond_bold_style = "font-family: Garamond, sans-serif; font-weight: bold; color: red; font-size: 30px;"
garamond_bold_style2 = "font-family: Garamond, sans-serif; font-weight: bold; color: blue; font-size: 25px;"

data = pd.read_csv(r"C:\Users\Naren\python projects\Airbnb\cleaned_airbnb_data.csv")

# Main Streamlit function
def main():
        st.set_page_config(
            page_title="AirBnB Data Analysis",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                "About": "<h1 style='" + garamond_bold_style + "'>About:</h1> The dashboard is created for user-friendly data visualization. Data has been retrieved from the MongoDB."
            }
        )
        
        
        st.markdown(f"<h1 style='{garamond_bold_style}'>AirBnB Dashboard</h1>", unsafe_allow_html=True)
        st.sidebar.markdown(f"<h2 style='{garamond_bold_style2}'>Hello!!!</h2>", unsafe_allow_html=True)

         # Load the image with PIL
        #image_path = r"C:\Users\shama\airbnb_image.png"
        #pil_image = Image.open(image_path)

        # Specify the image width 
        #image_width = 800

        # Display the PIL image with the specified width
        #st.image(pil_image, width=image_width) 
        
        
        with st.sidebar:
            selected = option_menu("Menu", ["Home","Charts","About"], 
                        icons=["house","graph-up-arrow","exclamation-circle"],
                        menu_icon= "menu-button-wide",
                        default_index=0,
                        styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                                "nav-link-selected": {"background-color": "#eb1328"}})
            
        if selected == 'Home':
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Welcome to the AirBnB Dashboard! 🏩</h1>", unsafe_allow_html=True)
           
            st.markdown("<h1 style='" + garamond_bold_style + "'>Airbnb Homes 🏘️</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Airbnb offers a wide variety of accommodations. These can range from entire houses or apartments to individual rooms in a home.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Diverse Options 👩‍🍳</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Airbnb provides diverse options for homes, catering to different preferences and budgets. Users can find cozy apartments, spacious houses, unique cottages, and more.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Amenities and Features 🛋️</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Airbnb listings usually showcase various amenities and features of the home, such as the number of bedrooms, bathrooms, kitchen facilities, internet availability, parking, and more.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Host Information 👩‍💻</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Users can also see information about the host, including reviews from previous guests, host response rate, and whether the host is a Superhost (an experienced host known for excellent service).</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Booking and Payment 💳</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Users can easily book a home through Airbnb's platform. The platform handles secure payments and booking processes, ensuring a smooth and safe transaction.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Reviews and Ratings ⭐</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Users can read reviews and ratings from previous guests to get an idea of the quality and experience offered by the home.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Location and Neighborhood 🌎</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Airbnb provides information about the home's location, nearby attractions, and the neighborhood's characteristics, helping users choose a home in a preferred area.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Customization 	😎</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Airbnb allows users to customize their search based on criteria such as price range, number of guests, specific dates, and desired amenities.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Safety Measures 🦸‍♀️</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Airbnb emphasizes safety and provides guidelines and information to hosts and guests to ensure a safe and secure stay.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Local Experience 🤝</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Staying in an Airbnb home often offers a more authentic and local experience compared to traditional hotels, allowing users to immerse themselves in the culture of the destination.</p>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>For further details click on Charts 👈.</h1>", unsafe_allow_html=True)
            
        if selected == 'Charts':
            st.markdown("<h1 style='" + garamond_bold_style + "'>Charts</h1>", unsafe_allow_html=True)

            # Create a Streamlit sub-menu for top charts
            chart_type = st.selectbox("Select Chart Type", ["Pie Chart", "Bar Chart", "Dot Plot", "Scatter Plot", "Bubble Plot", "Box Plot", "Map"])

            # Chart based on user selection
            if chart_type == "Pie Chart":
                # Create a pie chart
                fig = px.pie(data, names='property_type', title='Property Types Distribution', color_discrete_sequence=px.colors.qualitative.Pastel,
                             hover_data=['price'])
                fig.update_layout(height=900, width=800) 
                st.plotly_chart(fig)

            elif chart_type == "Bar Chart":
                # Create a bar chart
                fig = px.bar(data, x='property_type', y='price', title='Average Price by Property Type', color='property_type')
                st.plotly_chart(fig)

            elif chart_type == "Dot Plot":
                # Create a dot plot
                fig = px.scatter(data, x='room_type', y='price', color='property_type', title='Room_type vs Property_type', color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig)

            elif chart_type == "Scatter Plot":
                # Create a scatter plot
                fig = px.scatter(data, x='bedrooms', y='price', color='property_type', title='Bedrooms vs Price', color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig)

            elif chart_type == "Bubble Plot":
                # Create a bubble plot
                fig = px.scatter(data, x='country', y='property_type', color='property_type', size='price', title='country vs Property Type', color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig)

            elif chart_type == "Box Plot":
                # Create a box plot
                fig = px.box(data, x='property_type', y='weekly_price', title='Weekly Price Distribution by Property Type', color='property_type')
                st.plotly_chart(fig)
                
                
            elif chart_type == "Map":
                # Create a scatter plot on a map
                fig = px.scatter_mapbox(data, 
                                        lat='latitude', 
                                        lon='longitude', 
                                        color='price', 
                                        hover_data=['country', 'name', 'country_code'],
                                        zoom=2,  
                                        mapbox_style='carto-positron')

                # Update the layout for the map
                fig.update_layout(title='Scatter Plot on Map', 
                                mapbox=dict(
                                    center={'lat': data['latitude'].mean(), 'lon': data['longitude'].mean()},
                                    zoom=2),
                                autosize=True)

                # Display the map
                st.plotly_chart(fig)
        
        
        elif selected == "About":
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>About AirBnB Dashboard</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>AirBnB Dashboard is a comprehensive platform crafted to provide an intuitive and interactive experience for exploring AirBnB data. Here are some key points about this dashboard.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Purpose</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>The main purpose of this dashboard is to facilitate users in gaining insights into AirBnB listings and understanding various facets such as property types, prices, locations, and more.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>User-Friendly Interface</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>The interface is thoughtfully designed to be user-friendly, enabling users to effortlessly navigate and analyze data with just a few clicks.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Interactive Visualizations</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'> The dashboard offers a range of interactive charts and visualizations, allowing users to interpret data in a more engaging and informative way. Charts like Pie Chart, Bar Chart, Dot Plot, Scatter Plot, Bubble Plot, and Box Plot help in a detailed analysis of the dataset.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Informative Content</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Alongside visualizations, the dashboard provides informative content about AirBnB homes, diverse accommodation options, host information, booking process, and more.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)        

            st.markdown("<h1 style='" + garamond_bold_style + "'>Data Source</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>The data used in this dashboard is sourced from AirBnB and has been meticulously processed to present meaningful insights. The data reflects a curated selection of listings to showcase various features.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True) 
            
            st.markdown("<h1 style='" + garamond_bold_style + "'>Feedback and Suggestions</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>We value your feedback and suggestions to continuously improve and enhance this dashboard. Your insights help us enhance the user experience and add features that matter to you.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True) 

            st.markdown("<h1 style='" + garamond_bold_style + "'>Customization</h1>", unsafe_allow_html=True)
            st.markdown("<p style='" + garamond_bold_style2 + "'>Tailoring your experience is key. The dashboard allows you to choose the charts you want to explore and the parameters you want to analyze, making it a personalized tool.</p>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True) 

            st.markdown("<h1 style='" + garamond_bold_style + "'>Explore the various charts and sections to get a deeper understanding of AirBnB listings and make informed decisions. Your journey through this dashboard is a step towards enriching your AirBnB experience.</h1>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)
            
            st.markdown("<h1 style='" + garamond_bold_style2 + "'>Thankyou!!! 🙏</h1>", unsafe_allow_html=True)
            

if __name__ == "__main__":
    main()
