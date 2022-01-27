    MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []
chcking = []


def am():
    nr = len(movies) + 1
    title = input("Enter the movie title: ")
    if title == "":
        print("You can't leave the title empty")
    else:
        director = input("Enter the movie director: ")
        if director == "":
            director = "-"
        year = input("Enter the movie release year: ")
        if year == "":
            year = "-"
        movies.append({
        'nr': nr,
        'title': title.lower(),
        'director': director.lower(),
        'year': year.lower()
    })


def lm():
    if len(movies) == 0:
        print("Your list is empty")
    else:
        for movie in movies:
            print(f"{movie['nr']}.Title: {movie['title'].title()}   Director: {movie['director'].title()}   Year of release: {movie['year']}")


def fm():
    if len(movies) == 0:
        print("Your list is empty")
    else:
        tl = input("Enter the title to find your movie: ")
        if tl.lower() == "":
            print("You can't leave the title empty")
        else:
            for movie in movies:
                if movie['title'] == f"{tl.lower()}":
                    print(f"{movie['nr']}.Title: {movie['title'].title()}   Director: {movie['director'].title()}   Year of release: {movie['year']}")
                else:
                    chcking.append("1")
            if len(movies) == len(chcking):
                print("No such movie in your list")
                chcking.clear()
            else:
                chcking.clear()

user_options = {
    "a": am,
    "l": lm,
    "f": fm
}

selection = input(MENU_PROMPT)
while selection != 'q':
    if selection in user_options:
        selected_function = user_options[selection]
        selected_function()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)