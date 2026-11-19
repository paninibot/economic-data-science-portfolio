# optimizer.py
from players_data import PLAYER_POOL


# ==========================================
# DAY 1: GREEDY HEURISTIC OPTIMIZER
# ==========================================
def greedy_fpl_selector(pool, max_budget=75.0, max_players=8):
    """
    Greedy strategy:
    1. Sort players by 'value_density' (points / cost) descending.
    2. Pick players one by one if they fit within budget and squad cap.
    """
    sorted_pool = sorted(pool, key=lambda p: p.value_density(), reverse=True)

    selected_squad = []
    total_cost = 0.0
    total_points = 0

    for player in sorted_pool:
        if len(selected_squad) < max_players and (total_cost + player.cost) <= max_budget:
            selected_squad.append(player)
            total_cost += player.cost
            total_points += player.points

    return selected_squad, total_cost, total_points


# ==========================================
# DAY 2: SEARCH TREE (DECISION TREE)
# ==========================================
def search_tree_fpl(to_consider, avail_budget, slots_left):
    """
    Explores Take vs. Leave branches recursively to find the highest-scoring
    squad within budget and remaining player slots.
    Returns: (best_points, best_squad)
    """
    if to_consider == [] or avail_budget <= 0 or slots_left == 0:
        return (0, [])

    next_player = to_consider[0]
    rest = to_consider[1:]

    # Branch 1: Take next_player (if affordable)
    if next_player.cost <= avail_budget:
        take_points, take_squad = search_tree_fpl(
            rest, avail_budget - next_player.cost, slots_left - 1
        )
        take_points += next_player.points
    else:
        take_points, take_squad = (-1, [])

    # Branch 2: Leave next_player
    leave_points, leave_squad = search_tree_fpl(rest, avail_budget, slots_left)

    if take_points > leave_points:
        return (take_points, [next_player] + take_squad)
    else:
        return (leave_points, leave_squad)


# ==========================================
# DAY 1 VS. DAY 2 COMPARISON
# ==========================================
if __name__ == "__main__":
    test_pool = PLAYER_POOL[:14]
    budget = 75.0
    max_squad = 8

    greedy_squad, greedy_cost, greedy_points = greedy_fpl_selector(
        test_pool, max_budget=budget, max_players=max_squad
    )
    opt_points, opt_squad = search_tree_fpl(test_pool, budget, max_squad)
    opt_cost = sum(p.cost for p in opt_squad)

    print("=" * 55)
    print(f"DAY 1 (GREEDY) vs DAY 2 (SEARCH TREE) — {len(test_pool)} PLAYERS")
    print("=" * 55)
    print(f"Day 1 Greedy      -> {greedy_points} pts | £{greedy_cost:.1f}m / £{budget:.1f}m")
    print(f"Day 2 Search Tree -> {opt_points} pts | £{opt_cost:.1f}m / £{budget:.1f}m")
    print(f"Difference        -> +{opt_points - greedy_points} pts")
    print("Day 2 Squad       ->", [f"{p.name} (£{p.cost}m)" for p in opt_squad])
    print("=" * 55)
