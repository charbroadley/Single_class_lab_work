class Team:
    def __init__ (self, input_name, input_player_names, input_coach):
        self.name = input_name
        self.players = input_player_names
        self.coach = input_coach
    
    def add_player (self, name):
        self.players.append(name)

    def has_player (self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        return False
