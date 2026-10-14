import re
import random
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

# Destination and joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Keywords for new functionalities
weather_keywords = ["weather", "temperature", "forecast"]
news_keywords = ["news", "headlines", "updates"]
time_keywords = ["time", "clock", "local time"]

# Normalize user input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Travel recommendations
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = normalize_input(input(Fore.YELLOW + "You: "))

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

# Packing tips
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Simulated weather information
def weather_info():
    print(Fore.CYAN + "TravelBot: Which city do you want the weather for?")
    city = normalize_input(input(Fore.YELLOW + "You: "))

    weather = {
        "delhi": "Sunny, 32°C",
        "mumbai": "Cloudy, 29°C",
        "london": "Rainy, 15°C",
        "tokyo": "Clear, 22°C"
    }

    if city in weather:
        print(Fore.GREEN + f"TravelBot: Simulated weather for {city.title()}: {weather[city]}")
    else:
        print(Fore.RED + "TravelBot: Weather information is unavailable for that city.")

# Simulated news updates
def news_updates():
    news = [
        "Travel tip: Book flights early to find better prices.",
        "Travel update: Always check baggage rules before flying.",
        "Travel tip: Keep digital copies of important travel documents."
    ]
    print(Fore.GREEN + f"TravelBot: {random.choice(news)}")

# Local time information
def local_time():
    print(Fore.CYAN + "TravelBot: Which city do you want the time for?")
    city = normalize_input(input(Fore.YELLOW + "You: "))

    time_zones = {
        "delhi": "Asia/Kolkata",
        "mumbai": "Asia/Kolkata",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo"
    }

    if city in time_zones:
        from datetime import datetime
        from zoneinfo import ZoneInfo

        current_time = datetime.now(ZoneInfo(time_zones[city]))
        print(Fore.GREEN + f"TravelBot: Local time in {city.title()}: {current_time.strftime('%H:%M:%S')}")
    else:
        print(Fore.RED + "TravelBot: Time information is unavailable for that city.")

# Show help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (recommendation)")
    print(Fore.GREEN + "- Offer packing tips (packing)")
    print(Fore.GREEN + "- Tell a joke (joke)")
    print(Fore.GREEN + "- Provide simulated weather information (weather)")
    print(Fore.GREEN + "- Share travel news updates (news)")
    print(Fore.GREEN + "- Tell local time in different cities (time)")
    print(Fore.CYAN + "- Type 'help' to see commands")
    print(Fore.CYAN + "- Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))

        if re.search(r"\b(recommendation|recommend|suggest|destination)\b", user_input):
            recommend()
        elif re.search(r"\b(pack|packing)\b", user_input):
            packing_tips()
        elif re.search(r"\b(joke|funny)\b", user_input):
            tell_joke()
        elif any(keyword in user_input for keyword in weather_keywords):
            weather_info()
        elif any(keyword in user_input for keyword in news_keywords):
            news_updates()
        elif any(keyword in user_input for keyword in time_keywords):
            local_time()
        elif re.search(r"\bhelp\b", user_input):
            show_help()
        elif re.search(r"\b(exit|bye)\b", user_input):
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

# NLP Integration Notes:
# NLP could improve intent recognition by understanding the meaning of user messages
# instead of relying only on predefined keywords. It could also handle synonyms,
# spelling mistakes, and context across multiple messages.

# Run the chatbot
if __name__ == "__main__":
    chat()
