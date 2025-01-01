from enums.colors import Colors

class Player:
    color: Colors

    def __init__(self) -> None:
        return

    def update_color(self, color: Colors) -> None:
        self.color = color

    def is_player(self) -> bool:
        return True
