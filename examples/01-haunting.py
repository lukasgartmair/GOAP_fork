from goap.action import Action
from goap.planner import RegressivePlanner


class Haunt(Action):
    effects = {"is_spooky": True}
    preconditions = {"is_undead": True}


class BecomeUndead(Action):
    effects = {"is_undead": True}
    preconditions = {"is_undead": False}


if __name__ == "__main__":
    world_state = {"is_spooky": False}
    goal_state = {"is_spooky": True}
    print("Initial State:", world_state)
    print("Goal State:   ", goal_state)

    actions = [BecomeUndead(), Haunt()]
    planner = RegressivePlanner(actions)

    plan = planner.find_plan(world_state, goal_state)
    print(plan)
