# players_data.py

class Player:
    def __init__(self, name, position, cost, points):
        self.name = name
        self.position = position
        self.cost = cost
        self.points = points

    def value_density(self):  # <-- Lines up directly under def __init__
        """Points per million spent - our greedy metric"""
        return self.points / self.cost


# Sample pool of Premier League players
PLAYER_POOL = [
    # Forwards
    Player("Haaland", "FWD", 14.0, 240),
    Player("Isak", "FWD", 8.5, 160),
    Player("Watkins", "FWD", 9.0, 175),
    Player("Joao Pedro", "FWD", 5.5, 110),
    Player("Vardy", "FWD", 5.0, 95),

    # Midfielders
    Player("Palmer", "FWD", 10.5, 210),  # categorized for simplicity
    Player("Saka", "MID", 10.0, 200),
    Player("Salah", "MID", 13.0, 230),
    Player("Son", "MID", 9.5, 180),
    Player("Bowen", "MID", 7.5, 145),
    Player("Gordon", "MID", 7.0, 135),
    Player("Rogers", "MID", 5.5, 105),
    Player("Diallo", "MID", 5.0, 90),

    # Defenders
    Player("Gabriel", "DEF", 6.0, 140),
    Player("Saliba", "DEF", 6.0, 135),
    Player("Virgil", "DEF", 6.5, 130),
    Player("Pedro Porro", "DEF", 5.5, 115),
    Player("Konsa", "DEF", 4.5, 95),
    Player("Burn", "DEF", 4.5, 90),
    Player("Mykolenko", "DEF", 4.0, 80),

    # Goalkeepers
    Player("Raya", "GKP", 5.5, 130),
    Player("Pickford", "GKP", 5.0, 115),
    Player("Fabianski", "GKP", 4.0, 70),
]
