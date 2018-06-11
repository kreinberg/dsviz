'''Single Ended Queue Drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw


class QueueDrawer(Drawer):
    '''Drawer for the SingleEndedQueue data structure using the PIL.'''

    @staticmethod
    def draw(queue):
        '''Draws an image of a single ended queue.

        Args:
            queue: The queue to be drawn.

        Returns:
            A PIL image representing the current state of the queue.
        '''
        bg_color        = '#FFFFFF'
        fg_color1       = '#000000'
        fg_color2       = '#000000'
        padding_x       = 25
        padding_y       = 25
        text_padding    = 20
        cell_count      = len(queue)
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
            queue.name,
            [0, width, 0, padding_y + text_padding],
            color=fg_color1,
            bold=True
        )

        if queue.is_empty():
            return image

        ## Draw cells
        xy = [
            padding_x,
            padding_y + text_padding,
            padding_x + cell_width,
            padding_y + cell_height + text_padding
        ]
        for value in queue:
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
        util.draw_text(draw, 'FRONT', (tail[0] - 20, tail[1]+5))

        return image
