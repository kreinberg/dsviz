'''Binary Heap Drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw

class HeapDrawer(Drawer):
    '''Drawer for the BinaryHeap data structure using the PIL.'''

    WIDTH = 512
    HEIGHT = 512

    BACKGROUND_COLOR = '#FFFFFF'

    HEADER_HEIGHT = 32


    @staticmethod
    def draw(heap):
        '''Draws an image of a heap.

        Args:
            heap: The heap to be drawn.

        Returns:
            A PIL image representing the current state of the heap.
        '''
        width, height = HeapDrawer.WIDTH, HeapDrawer.HEIGHT
        bg_color = HeapDrawer.BACKGROUND_COLOR
        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        header_height = HeapDrawer.HEADER_HEIGHT



        ## Draw header
        util.draw_text_centered(
            draw,
            heap.name,
            [0, width, 0, header_height],
            color='#000000',
            bold=True
        )

        if heap.is_empty():
            pass

        ## Draw nodes


        return image
