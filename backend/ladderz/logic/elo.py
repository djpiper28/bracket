from ladderz.models.db.match import Match
from ladderz.models.db.round import Round, RoundWithMatches
from ladderz.utils.types import ELO


def calculate_elo_for_players_in_match(match: Match) -> dict[int, ELO]:
    return {}


def calculate_elo_for_player(rounds: list[RoundWithMatches]) -> ELO:
    player_x_elo: dict[int, ELO] = {}

    for round in rounds:
        for match in round.matches:
            print(match)

    return ELO(0)