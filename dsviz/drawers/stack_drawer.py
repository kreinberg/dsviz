'''Array Stack Drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw


class StackDrawer(Drawer):
    '''Drawer for the ArrayStack data structure using the PIL.'''

    @staticmethod
    def draw(stack):
        '''Draws an image of a stack. Stacks are drawn vertically and top-down.

        Args:
            stack: The stack to be drawn.

        Returns:
            A PIL image representing the current state of the stack.
        '''
        bg_color        = '#FFFFFF'
        fg_color1       = '#000000'
        fg_color2       = '#000000'
        padding_x       = 25
        padding_y       = 25
        text_padding    = 20
        cell_count      = len(stack)
        cell_width      = 100
        cell_height     = 60
        arrow_size      = 35
        right_gap        = 100
        width           = (padding_x * 2) + cell_width + right_gap
        height          = (padding_y * 2) + (cell_height * cell_count) + text_padding

        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        ## Draw header
        util.draw_text_centered(
            draw,
            stack.name,
            [0, width, 0, padding_y + text_padding],
            color=fg_color1,
            bold=True
        )

        if stack.is_empty():
            return image

        ## Draw cells
        xy = [
            padding_x,
            padding_y + text_padding,
            padding_x + cell_width,
            padding_y + cell_height + text_padding
        ]
        for value in stack:
            util.draw_rectangle_with_text(
                draw,
                str(value),
                xy
            )
            xy[1] += cell_height
            xy[3] += cell_height

        ## Draw arrow pointing to top of stack
        tail = (width - padding_x - 40, padding_y + text_padding + (cell_height // 2))
        util.draw_arrow(draw, tail, 50, 'left')
        util.draw_text(draw, 'TOP', (tail[0]+10, tail[1]-9))

        return image
