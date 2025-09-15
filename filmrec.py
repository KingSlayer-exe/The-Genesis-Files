import random

def get_recommendations(genre, type_choice, language):
    suggestions = []
    
    if genre == "action":
        if type_choice == "movie":
            if language == "anime":
                suggestions = ["Akira", "Sword of the Stranger", "Redline"]
            elif language == "foreign":
                suggestions = ["The Raid", "Rurouni Kenshin", "Ong-Bak"]
            else:
                suggestions = ["Mad Max: Fury Road", "John Wick", "Gladiator"]
        elif type_choice == "show":
            if language == "anime":
                suggestions = ["Attack on Titan", "Cowboy Bebop", "Samurai Champloo"]
            elif language == "foreign":
                suggestions = ["Kingdom", "Banshee", "Lupin"]
            else:
                suggestions = ["Daredevil", "Vikings", "The Mandalorian"]
    
    elif genre == "drama":
        if type_choice == "movie":
            if language == "anime":
                suggestions = ["Your Name", "Grave of the Fireflies", "A Silent Voice"]
            elif language == "foreign":
                suggestions = ["Parasite", "A Separation", "Cinema Paradiso"]
            else:
                suggestions = ["Schindler's List", "The Green Mile", "Forrest Gump"]
        elif type_choice == "show":
            if language == "anime":
                suggestions = ["Steins;Gate", "Monster", "Violet Evergarden"]
            elif language == "foreign":
                suggestions = ["Tokyo Vice", "Dark", "Money Heist"]
            else:
                suggestions = ["Breaking Bad", "The Crown", "This Is Us"]
    
    elif genre == "comedy":
        if type_choice == "movie":
            if language == "anime":
                suggestions = ["My Neighbor Totoro", "The Disastrous Life of Saiki K.", "Konosuba"]
            elif language == "foreign":
                suggestions = ["Amélie", "Kung Fu Hustle", "OSS 117"]
            else:
                suggestions = ["Superbad", "The Grand Budapest Hotel", "Dumb and Dumber"]
        elif type_choice == "show":
            if language == "anime":
                suggestions = ["Gintama", "One Punch Man", "Nichijou"]
            elif language == "foreign":
                suggestions = ["The IT Crowd", "Lupin", "Extraordinary Attorney Woo"]
            else:
                suggestions = ["Brooklyn Nine-Nine", "The Office", "Parks and Recreation"]
    
    elif genre == "horror":
        if type_choice == "movie":
            if language == "anime":
                suggestions = ["Perfect Blue", "Paprika", "Vampire Hunter D"]
            elif language == "foreign":
                suggestions = ["Train to Busan", "Ju-On: The Grudge", "REC"]
            else:
                suggestions = ["Hereditary", "The Conjuring", "It Follows"]
        elif type_choice == "show":
            if language == "anime":
                suggestions = ["Higurashi no Naku Koro ni", "Parasyte", "Another"]
            elif language == "foreign":
                suggestions = ["Kingdom", "Marianne", "Alice in Borderland"]
            else:
                suggestions = ["The Haunting of Hill House", "American Horror Story", "Stranger Things"]
    
    elif genre == "sci-fi":
        if type_choice == "movie":
            if language == "anime":
                suggestions = ["Ghost in the Shell", "Akira", "Psycho-Pass"]
            elif language == "foreign":
                suggestions = ["Snowpiercer", "Timecrimes", "The Wandering Earth"]
            else:
                suggestions = ["Blade Runner 2049", "Inception", "The Matrix"]
        elif type_choice == "show":
            if language == "anime":
                suggestions = ["Ergo Proxy", "Steins;Gate", "Cowboy Bebop"]
            elif language == "foreign":
                suggestions = ["Dark", "3%", "The Expanse"]
            else:
                suggestions = ["Stranger Things", "Black Mirror", "Westworld"]
    
    elif genre == "anime":
        if type_choice == "movie":
            suggestions = ["Spirited Away", "Your Name", "A Silent Voice", "Ghost in the Shell", "Akira"]
        elif type_choice == "show":
            suggestions = ["Attack on Titan", "Death Note", "Steins;Gate", "Cowboy Bebop", "Fullmetal Alchemist: Brotherhood"]
    
    return random.choice(suggestions) if suggestions else "Sorry, no recommendations found for that choice."

print("Welcome to the Movie & Show Recommender!")
genre = input("Choose a genre (action, drama, comedy, horror, sci-fi, anime): ").strip().lower()
type_choice = input("Do you want a movie or a show? ").strip().lower()
language = input("Do you prefer anime, foreign, or any? ").strip().lower()

suggestion = get_recommendations(genre, type_choice, language)
print(f"We recommend: {suggestion}")

