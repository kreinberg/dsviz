'''Double Ended Queue Drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw


class DequeDrawer(Drawer):
    '''Drawer for the DoubleEndedQueue data structure using the PIL.'''

    @staticmethod
    def draw(deque):
        '''Draws an image of a double ended queue.

        Args:
            deque: The deque to be drawn.

        Returns:
            A PIL image representing the current state of the deque.
        '''
        bg_color        = '#FFFFFF'
        fg_color1       = '#000000'
        fg_color2       = '#000000'
        padding_x       = 25
        padding_y       = 25
        text_padding    = 20
        cell_count      = len(deque)
        cell_width      = 70
        cell_height     = 60
        bottom_gap      = 50
        width           = (padding_x * 2) + (cell_width * cell_count)
        height          = (padding_y * 2) + cell_height + text_padding + bottom_gap

        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        ## Draw header
        util.draw_text_centered(
            draw,
            deque.name,
            [0, width, 0, padding_y + text_padding],
            color=fg_color1,
            bold=True
        )

        if deque.is_empty():
            return image

        ## Draw cells
        xy = [
            padding_x,
            padding_y + text_padding,
            padding_x + cell_width,
            padding_y + cell_height + text_padding
        ]
        for value in deque:
            util.draw_rectangle_with_text(
                draw,
                str(value),
                xy
            )
            xy[0] += cell_width
            xy[2] += cell_width

        ## Draw arrow pointing to front of queue
        tail = (padding_x + (cell_width // 2), height - padding_y - (text_padding // 2))
        util.draw_arrow(draw, tail, 30, 'up')
        util.draw_text(draw, 'FRONT', (tail[0] - 20, tail[1] + 5))

        ## Draw arrow pointing to rear of quuee
        if len(deque) > 1:
            tail = (width - (padding_x + (cell_width // 2)), height - padding_y - (text_padding // 2))
            util.draw_arrow(draw, tail, 30, 'up')
            util.draw_text(draw, 'REAR', (tail[0] - 20, tail[1] + 5))

        return image

        '''
        ## Draw arrow pointing to back
        tail = (width - (cell_offset_x + (cell_width/2)), height - cell_offset_y + 10)
        util.draw_arrow(draw, tail, 30, 'up', width=2)
        util.draw_text(draw, 'Rear', (tail[0]-15, tail[1]+5))
        '''
