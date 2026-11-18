# optimizer.py
from players_data import PLAYER_POOL


def greedy_fpl_selector(pool, max_budget=80.0, max_players=8):
    """
    Greedy Strategy:
    1. Sort players by 'value density' (Points / Cost) descending.
    2. Pick players one by one if they fit within the remaining budget and squad limit.
    """
    # Sort by points per million (descending)
    sorted_pool = sorted(pool, key=lambda p: p.value_density(), reverse=True)

    selected_squad = []
    total_cost = 0.0
    total_points = 0

    print("--- EVALUATING PLAYERS VIA GREEDY HEURISTIC ---")
    for player in sorted_pool:
        if len(selected_squad) < max_players and (total_cost + player.cost) <= max_budget:
            selected_squad.append(player)
            total_cost += player.cost
            total_points += player.points
            print(
                f"Picked: {player.name:<12} | Cost: £{player.cost}m | Points: {player.points} | Density: {player.value_density():.2f}")

    return selected_squad, total_cost, total_points


if __name__ == "__main__":
    budget = 75.0  # Let's build an 8-player core under £75m
    squad, cost, points = greedy_fpl_selector(
        PLAYER_POOL, max_budget=budget, max_players=8)

    print("\n" + "="*40)
    print(f"FINAL GREEDY SQUAD RESULTS:")
    print(f"Total Squad Cost: £{cost:.1f}m / £{budget}m budget")
    print(f"Total Expected Points: {points}")
    print("="*40)
