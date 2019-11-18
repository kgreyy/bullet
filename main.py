"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import two as second

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)
        self.sino_hatak = None
        self.last_mouse_position = 0, 0
        self.deck = second.deckGo()
        self.hand1, self.deck = second.drawfromDeck(4,self.deck)
        self.hand2, self.deck = second.drawfromDeck(4,self.deck)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.cards_list1 = arcade.SpriteList()
        self.cards_list2 = arcade.SpriteList()

        for x in self.hand1:
            card = arcade.Sprite(second.getimgStr(x))
            card.position = (70,145)
            self.cards_list1.move(143,0)
            self.cards_list1.append(card)
        self.cards_list1.move((SCREEN_WIDTH//2)-self.cards_list1.center[0],0)

        card = arcade.Sprite("C:/Users/james/AppData/Local/Programs/Python/Python36-32/cardClubsA.png")
        card.center_x = (SCREEN_WIDTH//2)
        card.center_y = (SCREEN_HEIGHT-145)
        self.cards_list2.append(card)

        self.playarea = arcade.Sprite("C:/Users/james/AppData/Local/Programs/Python/Python36-32/playarea.png")
        self.playarea.center_x = (SCREEN_WIDTH//2)
        self.playarea.center_y = (SCREEN_HEIGHT//2)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.cards_list1.draw()
        self.cards_list2.draw()
        self.playarea.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.sino_hatak is not None:
            self.sino_hatak.position = self.last_mouse_position
        self.playarea.update()
        self.cards_list1.update()
        self.cards_list2.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        if self.sino_hatak is not None:
            self.last_mouse_position = x, y
            self.sino_hatak.position = self.last_mouse_position

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            clicked = arcade.get_sprites_at_point((x,y), self.cards_list1)
            print(clicked)
            if len(clicked) > 0:
                self.sino_hatak = clicked[0]
                self.last_mouse_position = x, y
        """
        Called when the user presses a mouse button.
        """

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.sino_hatak = None
        if arcade.check_for_collision_with_list(self.playarea, self.cards_list1) == []:
            for card in self.cards_list1:
                card.position = (70,145)
                self.cards_list1.move(143,0)
            self.cards_list1.move((SCREEN_WIDTH//2)-self.cards_list1.center[0],0)
        else:
            for card in arcade.check_for_collision_with_list(self.playarea, self.cards_list1):
                card.position = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()