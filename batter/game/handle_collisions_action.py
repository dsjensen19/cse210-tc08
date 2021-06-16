import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #marquee = cast["marquee"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        Side_Paddle = cast["Side_Paddle"][0]
        Bottom_Paddle = cast["Bottom_Paddle"][0]
        bricks = cast["brick"]
        #marquee.set_text("")
        actor= Actor()
        point = Point(0,0)
        for brick in bricks:
            if ball.get_position().inbetween(brick.get_position()):
                x2 = ball._velocity.get_x()
                y2 = ball._velocity.get_y()
                ball.set_velocity(Point(x2 * 1, y2 * -1))
                #marquee.set_text(description) 
            elif ball.get_position().inbetween(Bottom_Paddle.get_position()):
                x2 = ball._velocity.get_x()
                y2 = ball._velocity.get_y()
                ball.set_velocity(Point(x2 * 1, y2 * -1))
            elif ball.get_position().inbetween(Side_Paddle.get_position()):
                x2 = ball._velocity.get_x()
                y2 = ball._velocity.get_y()
                ball.set_velocity(Point(x2 * -1, y2 * 1))