'''Singly Linked List Drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw


class SLLDrawer(Drawer):
    '''Drawer for the SinglyLinkedList data structure using the PIL.'''

    @staticmethod
    def draw(linked_list):
        '''Draws an image of a singly linked list.

        Args:
            linked_list: The linked list to be drawn.

        Returns:
            A PIL image representing the current state of the linked list.
        '''
        bg_color     = '#FFFFFF'
        fg_color1    = '#000000'
        fg_color2    = '#000000'
        padding_x    = 25
        padding_y    = 25
        text_padding = 20
        cell_count   = len(linked_list)
        cell_width   = 100
        cell_height  = 50
        node_width   = 50
        next_width   = 30
        gap_width    = 20
        arrow_size   = 35
        width        = (padding_x * 2) + (cell_width * cell_count) + next_width + gap_width
        height       = (padding_y * 2) + cell_height + text_padding

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

        ## Draw nodes
        xy = [
            padding_x,
            padding_y + text_padding,
            padding_x,
            padding_y + text_padding + cell_height
        ]
        for value in linked_list:
            ## Draw node with data
            xy[2] += node_width
            util.draw_rectangle_with_text(
                draw,
                str(value),
                xy,
                fill_color=bg_color,
                outline_color=fg_color1,
                text_color=fg_color2
            )
            ## Draw next box with arrow
            xy[0] += node_width
            xy[2] += next_width
            draw.rectangle(
                xy,
                fill=bg_color,
                outline=fg_color1
            )
            arrow_y = (xy[1] + xy[3]) // 2
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
            xy[0] += cell_width - (node_width + next_width + gap_width)
            xy[2] += cell_width - (node_width + next_width + gap_width)

        ## Draw NULL cell
        null_width = xy[0] + (gap_width // 2)
        null_height = (xy[1] + xy[3]) // 2 - 10
        util.draw_text(
            draw,
            'NULL',
            (null_width, null_height),
            color=fg_color1
        )

        return image
