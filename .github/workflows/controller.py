from project_types import Feedback
from model import SubtractASquareModel
from view import SubtractASquareView

class SubtractASquareController:
    # model instantiated in main
    def start(self, model: SubtractASquareModel,
              view: SubtractASquareView):
        
        while not model.is_game_over:
            while True:
                num_str: str = view.take_player_num(model.current_player)
                if num_str.isnumeric():
                    num: int = int(num_str)
                    feedback: Feedback = model.subtract_square(num)
                    match feedback:
                        case Feedback.NOT_POSITIVE:
                            view.show_feedback_not_positive(num)
                        case Feedback.NOT_PERFECT_SQUARE:
                            view.show_feedback_not_perfect_square(num)
                        case Feedback.GREATER_THAN_N:
                            view.show_feedback_greater_than_n()
                        case Feedback.GAMEOVER:
                            assert model.n <= 0
                            view.show_game_over()
                            return
                        case Feedback.NEXT:
                            break
                        case _:
                            raise ValueError('should not reach here! ')




