'''AVL Tree drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw


class AVLTreeDrawer(Drawer):
    '''Drawer for the AVLTree data structure using the PIL.'''

    WIDTH = 512
    HEIGHT = 512

    BACKGROUND_COLOR = '#FFFFFF'

    HEADER_HEIGHT = 32

    NODE_WIDTH = 50
    NODE_HEIGHT = 50

    @staticmethod
    def draw(tree):
        '''Draws an image of an AVL Tree.

        Args:
            tree: The tree to be drawn.

        Returns:
            A PIL image representing the current state of the tree.
        '''
        width, height = AVLTreeDrawer.WIDTH, AVLTreeDrawer.HEIGHT
        bg_color = AVLTreeDrawer.BACKGROUND_COLOR
        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        header_height = AVLTreeDrawer.HEADER_HEIGHT

        ## Draw header
        util.draw_text_centered(
            draw,
            tree.name,
            [0, width, 0, header_height],
            color='#000000',
            bold=True
        )

        if tree.is_empty():
            return image

        ## Draw nodes



        return image
