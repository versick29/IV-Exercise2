class TeamStats:
    def __init__(self, team_id, team_name, num_players, height, weight, num_birth_places,
                 total_games, total_minutes_played, field_goals, field_goals_attempted,
                 field_goal_percent, three_pointers, three_pointers_attempted, three_point_percent,
                 two_pointers, two_pointers_attempted, two_point_percent, free_throws,
                 free_throws_attempted, free_throw_percent, offensive_rebounds, defensive_rebounds,
                 total_rebounds, assists, steals, blocks, turnovers, personal_fouls, points):
        self.team_id = team_id
        self.team_name = team_name
        self.num_players = num_players
        self.height = height
        self.weight = weight
        self.num_birth_places = num_birth_places
        self.total_games = total_games
        self.total_minutes_played = total_minutes_played
        self.field_goals = field_goals
        self.field_goals_attempted = field_goals_attempted
        self.field_goal_percent = field_goal_percent
        self.three_pointers = three_pointers
        self.three_pointers_attempted = three_pointers_attempted
        self.three_point_percent = three_point_percent
        self.two_pointers = two_pointers
        self.two_pointers_attempted = two_pointers_attempted
        self.two_point_percent = two_point_percent
        self.free_throws = free_throws
        self.free_throws_attempted = free_throws_attempted
        self.free_throw_percent = free_throw_percent
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.total_rebounds = total_rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
        self.points = points

