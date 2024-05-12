from minigrid.core.grid import Grid
from minigrid.core.mission import MissionSpace
from minigrid.core.world_object import Goal
from minigrid.minigrid_env import MiniGridEnv
from numpy.random import randint
import gymnasium as gym

class RandomGoalEmptyEnv(MiniGridEnv):
    """
    Empty grid environment, same as EmptyEnv, but with the goal position randomized.
    """

    def __init__(self, size=8, agent_start_pos=(1, 1), agent_start_dir=0, max_steps=None, **kwargs):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir
        self.size = size

        mission_space = MissionSpace(mission_func=lambda: "get to the green goal square")


        if max_steps is None:
            max_steps = 4 * size**2

        super().__init__(
            mission_space=mission_space,
            grid_size=size,
            see_through_walls=True,
            max_steps=max_steps,
            **kwargs,
        )

    @staticmethod
    def _gen_mission(self):
        return "get to the green goal square"
    
    def _gen_grid(self, width, height):
        # Create an empty grid
        #width, height = self.size
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place a goal square at a random position, avoiding the outer walls
        goal_x = randint(1, width - 2)
        goal_y = randint(1, height - 2)
        self.put_obj(Goal(), goal_x, goal_y)

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "get to the green goal square"


    # Added
    # def get_goal_position(self):
    #     for x in range(self.env.width):
    #         for y in range(self.env.height):
    #             if self.env.grid.get(x, y) is not None and isinstance(self.env.grid.get(x, y), Goal):
    #                 return (x, y)
    #     return None