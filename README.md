# AI Day Planner

AI Day Planner is a Streamlit web application that helps users plan their day with personalized weather updates, news summaries, and smart itineraries based on their city and interests.

## Features

- **Home Page:** Start your day with a motivational quote and a beautiful morning image.
- **Weather Updates:** Get a friendly, detailed weather report for your city, including practical suggestions on what to wear or carry.
- **News by Interest:** Fetch and summarize the latest news articles based on your chosen topic.
- **Smart Planner:** Receive a personalized day itinerary with weather forecasts, local events, and recommended places to visit.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Shivani-781/AI-Day-Planner.git
   cd AI_Day_Planner
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure API keys:**
   - Create a `.env` file in the project root.
   - Add your API keys for Google Gemini, OpenWeather, NewsAPI, and SerpAPI.

4. **Run the app:**
   ```sh
   streamlit run app.py
   ```

## File Structure

- `app.py` — Streamlit UI and page routing.
- `main.py` — Core logic for weather, news, events, and planning.
- `helper.py` — Utility functions for quotes and images.
- `.env` — API keys and environment variables.
- `requirements.txt` — Python dependencies.

## APIs Used

- [Google Gemini](https://ai.google.dev/)
- [OpenWeather](https://openweathermap.org/api)
- [NewsAPI](https://newsapi.org/)
- [SerpAPI](https://serpapi.com/)

## Demo
Access the app here: https://ai-day-planner.streamlit.app/

---

*Enjoy planning your day with AI Day Planner!*
