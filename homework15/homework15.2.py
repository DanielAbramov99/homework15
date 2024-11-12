games_list: list[str] = ["V Auto Theft Grand ", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print(games_list)
print("games that contain more than 8 letters", list(filter(lambda game: len(game) > 8, games_list)))
print("games that starts with the letter "f" ", list(filter(lambda game: game.lower().startswith("f"), games_list)))
print("games that contain two words", list(filter(lambda game: len(game.split()) == 2, games_list)))
print("games that contain letter v", list(filter(lambda game: "v" in game.lower(), games_list)))
