from pyray import *
from raylib import *
from Settings import *
import os
from StackDataStructure import *

class Button():

    def __init__(self, pos, width, height, text, font, font_size):
        """
        Each button has a rectangular object associated with it,
        along with position, width, height, font and font size, text, 
        as well as a boolean to track whether or not it is hovered
        """
        self._pos = pos
        self._text = text
        self._font = font
        self._font_size = font_size
        self._width = width
        self._height = height
        self._rectangle = Rectangle(self._pos.x, self._pos.y, self._width, self._height)
        self.reposition_button()
        
    def reposition_button(self):
        # accepts a pos Point2D object parameter used to reposition the buttons rectangle
        # repositions so that it can be placed relative to its center rather than the top left corner
        self._pos.x -= self._width / 2
        self._pos.y -= self._height / 2
        self._rectangle = Rectangle(self._pos.x, self._pos.y, self._width, self._height)
        
    def is_hovered(self):
        # returns true if cursor is hovering over the button
        mouse_pos = get_mouse_position()
        in_rectangle_width = self._pos.x <= mouse_pos.x <= self._pos.x + self._width
        in_rectangle_height = self._pos.y <= mouse_pos.y <= self._pos.y + self._height
        return in_rectangle_width and in_rectangle_height
        

    def draw_button(self, hovered_button_color, hovered_text_color, og_button_color, og_text_color):
        # get dimensions of the text to be drawn on the button 
        text_dimensions = measure_text_ex(self._font, self._text, self._font_size, 0.0)
        text_width = text_dimensions.x
        text_height = text_dimensions.y
        if self.is_hovered():
            button_color = hovered_button_color
            text_color = hovered_text_color
        else:
            button_color = og_button_color
            text_color = og_text_color
        # draw button with centered text based on text size, use appropriate button color and text color for the rectangle     
        draw_rectangle_pro(self._rectangle, Vector2(0,0), 0, button_color)
        draw_text_pro(self._font, self._text, Vector2(self._pos.x + self._rectangle.width / 2 - text_width/2, 
        self._pos.y + self._rectangle.height / 2 - text_height/2), Vector2(0,0), 0, self._font_size, 0.0, text_color)
        draw_rectangle_lines_ex(self._rectangle, 5.0, WHITE)
        
    def get_rectangle(self):
        return self._rectangle

if __name__ == "__main__":
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'GAME')
    font_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../font/" + "slkscreb.ttf")) 
    slkscr_font = load_font(font_base_path)
    button_test = Button(Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), DEFAULT_BUTTON_WIDTH, DEFAULT_BUTTON_HEIGHT, "TESTING", slkscr_font,DEFAULT_BUTTON_FONT_SIZE)
    while not window_should_close():
        begin_drawing()
        clear_background(BG_COLOR)
        button_test.draw_button(GRAY, LIGHTGRAY, RED, BLACK)
        end_drawing()
    end_drawing()