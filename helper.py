import random

def get_random_quote():
    quotes = [
        "The sun is a daily reminder that we too can rise again from the darkness, that we too can shine our own light.",
        "Write it on your heart that every day is the best day in the year.",
        "I get up every morning and it's going to be a great day. You never know when it's going to be over, so I refuse to have a bad day.",
        "Today's goals: Coffee and kindness. Maybe two coffees, and then kindness.",
        "An early-morning walk is a blessing for the whole day.",
        "Morning is an important time of day because how you spend your morning can often tell you what kind of day you are going to have.",
        "Lose an hour in the morning, and you will spend all day looking for it.",
        "When you arise in the morning, think of what a precious privilege it is to be alive - to breathe, to think, to enjoy, to love."
    ]
    return random.choice(quotes)

def get_random_image():
    image_urls = [
        "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8",
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
        "https://images.unsplash.com/photo-1494548162494-384bba4ab999",
        "https://images.unsplash.com/photo-1520038410233-7141be7e6f97",
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
        "https://images.unsplash.com/photo-1508575478422-c401c540a858"
    ]
    return random.choice(image_urls)
