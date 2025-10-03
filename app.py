import streamlit as st
from helper import get_random_quote, get_random_image
from main import temperature_of_city, get_news, news_summarizer, smart_plan


# --- Page Definitions ---

def home_page():
    """Displays the home page with a quote and image."""
    st.title("☀️ Good Morning!")
    st.markdown("---")
    st.subheader("A Thought for Your Day")
    st.info(f'"{get_random_quote()}"')
    st.image(get_random_image(), caption="A beautiful morning to start your day", width=700)
    st.markdown("---")
    st.write("Use the sidebar on the left to get your daily updates!")


def weather_news_page():
    """Displays the page for getting weather and news by city."""
    st.header("Get Weather of the city")
    city = st.text_input("Enter your city name:")

    if st.button("Fetch Information"):
        if city:
            temperature_output = temperature_of_city(city)
            st.subheader(f"Weather Info: {temperature_output}")
        else:
            st.error("Please enter a city name.")
  

def interest_news_page():
    """Displays the page for getting news by interest."""
    st.header("Get News Based on Your Interests")
    interest = st.text_input("Enter your area of interest (e.g., Technology, Sports, Health):", "Technology")

    if st.button("Fetch News"):
        if interest:
            articles= get_news(interest)
            title=[]
            url=[]
            image_url=[]
            for i in articles:
                title.append(i["title"])
                url.append(i['url'])
                image_url.append(i["urlToImage"])

            if not articles:
                st.error("No news found.")

            cols = st.columns(len(articles))
            for idx, article in enumerate(articles):
                with cols[idx]:
                    st.subheader(article.get("title", "No Title"))
                    st.markdown("---")

                    if article.get("urlToImage"):
                        st.image(article["urlToImage"])
                    else:
                        st.image("https://via.placeholder.com/150", caption="No image available")

                    st.markdown("---")
                    st.write(f"[Read full article here]({article['url']})")
                    st.markdown("---")
                    st.write(news_summarizer(article['url']))

        else:
            st.error("Please enter an area of interest")


def smart_planner():
    """Displays the page for viewing the day's schedule."""
    st.header("Your Smart Planner Day")
    city = st.text_input("Enter your city name:")
    if st.button("Let's Plan"):
        if city:
            smart_plans= smart_plan(city)
            st.subheader(smart_plans)
            st.success("Have a nice day!")
        else:
            st.error("Please enter a city name")


# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
page_option = st.sidebar.radio("Choose a page:", ("Home", "Get Weather of your City", "News by Interest", "Smart Planner"))
st.sidebar.markdown("---")


# --- Page Routing ---
if page_option == "Home":
    home_page()
elif page_option == "Get Weather of your City":
    weather_news_page()
elif page_option == "News by Interest":
    interest_news_page()
elif page_option == "Smart Planner":
    smart_planner()
