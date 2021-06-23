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
        #Side_Paddle = cast["Side_Paddle"][0]
        Bottom_Paddle = cast["Bottom_Paddle"][0]
        bricks = cast["brick"]
        #marquee.set_text("")
        actor= Actor()
        point = Point(0,0)
        i = 0
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                x2 = ball._velocity.get_x()
                y2 = ball._velocity.get_y()
                ball.set_velocity(Point(x2 * 1, y2 * -1))
                del bricks[i]

                #marquee.set_text(description)
            i +=1 
            """
        bottom_left_point = Point(0,0)
        bottom_right_point = Point(constants.MAX_X, 0)
        if ball.get_position().inbetween_X(Bottom_Paddle.get_position(), 10):
            x2 = ball._velocity.get_x()
            y2 = ball._velocity.get_y()
            ball.set_velocity(Point(x2 * 1, y2 * -1))

        if ball.get_position().inbetween_X(bottom_left_point, constants.MAX_X):
            x2 = ball._velocity.get_x()
            y2 = ball._velocity.get_y()

            #end game
        
        #Walls
        if ball.get_position().inbetween_Y(bottom_left_point, constants.MAX_Y):
            x2 = ball._velocity.get_x()
            y2 = ball._velocity.get_y()
            ball.set_velocity(Point(x2 * -1, y2 * 1))
        
        if ball.get_position().inbetween_Y(bottom_right_point, constants.MAX_Y):
            x2 = ball._velocity.get_x()
            y2 = ball._velocity.get_y()
            ball.set_velocity(Point(x2 * -1, y2 * 1))
            """