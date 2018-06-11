'''Doubly Linked List Drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw


class DLLDrawer(Drawer):
    '''Drawer for the DoublyLinkedList data structure using the PIL.'''

    @staticmethod
    def draw(linked_list):
        '''Draws an image of a doubly linked list.

        Args:
            linked_list: The linked list to be drawn.

        Returns:
            A PIL image representing the current state of the linked list.
        '''
        bg_color        = '#FFFFFF'
        fg_color1       = '#000000'
        fg_color2       = '#000000'
        padding_x       = 25
        padding_y       = 25
        text_padding    = 20
        cell_count      = len(linked_list)
        cell_width      = 130
        cell_height     = 50
        node_width      = 50
        next_width      = 30
        gap_width       = 20
        null_width      = 50
        arrow_size      = 35
        width           = (padding_x * 2) + (cell_width * cell_count) + (null_width * 2) + gap_width
        height          = (padding_y * 2) + cell_height + text_padding

        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        ## Draw header
        util.draw_text_centered(
            draw,
            linked_list.name,
            [0, width, 0, padding_y + text_padding],
            color=fg_color1,
            bold=True
        )

        ## Cease drawing if linked list is empty
        if linked_list.is_empty():
            return image

        ## Draw cells
        xy = [
            padding_x,
            padding_y + text_padding,
            padding_x + null_width,
            padding_y + text_padding + cell_height
        ]

        ## First NULL CELL
        util.draw_text_centered(
            draw,
            'NULL',
            [xy[0], xy[2], xy[1], xy[3]],
            color=fg_color1
        )
        xy[0] += null_width + gap_width
        xy[2] += gap_width

        for i, value in enumerate(linked_list):
            ## Draw prev box
            xy[2] += next_width
            draw.rectangle(
                xy,
                fill=bg_color,
                outline=fg_color1
            )
            ## Draw prev arrow
            arrow_y = ((xy[1] + xy[3]) // 2) + (cell_height // 4)
            ## Make arrow centered if first prev arrow
            if i == 0:
                arrow_y -= (cell_height // 4)
            arrow_x = xy[0] + (next_width // 2)
            util.draw_arrow(
                draw,
                (arrow_x, arrow_y),
                arrow_size,
                'left',
                fg_color2
            )
            ## Draw node with data
            xy[0] += next_width
            xy[2] += node_width
            util.draw_rectangle_with_text(
                draw,
                str(value),
                xy,
                fill_color=bg_color,
                outline_color=fg_color1,
                text_color=fg_color2
            )
            ## Draw next box
            xy[0] += node_width
            xy[2] += next_width
            draw.rectangle(
                xy,
                fill=bg_color,
                outline=fg_color1
            )
            ## Draw next arrow
            arrow_y = ((xy[1] + xy[3]) // 2) - (cell_height // 4)
            ## Make arrow centered if last next arrow
            if i == len(linked_list) - 1:
                arrow_y += (cell_height // 4)
            arrow_x = xy[0] + (next_width // 2)
            util.draw_arrow(
                draw,
                (arrow_x, arrow_y),
                arrow_size,
                'right',
                fg_color2
            )
            xy[0] += next_width
            xy[0] += gap_width
            xy[2] += gap_width

        ## Last NULL cell
        xy[2] += null_width
        util.draw_text_centered(
            draw,
            'NULL',
            [xy[0], xy[2], xy[1], xy[3]],
        )

        return image
