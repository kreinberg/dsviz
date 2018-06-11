'''Binary Search Tree Drawer.'''


from dsviz.bases import Drawer
import dsviz.util.drawer_utils as util

from PIL import Image, ImageDraw


class BSTDrawer(Drawer):
    '''Drawer for the BinarySearchTree data structure using the PIL.'''

    @staticmethod
    def calc_width(tree):
        return 6

    @staticmethod
    def calc_height(tree):
        return 5

    @staticmethod
    def draw_node(draw, node, coords, level_height, depth):
        pass
        '''
        util.draw_ellipsis(
        '''

    @staticmethod
    def draw(tree):
        '''Draws an image of a binary search tree.

        Args:
            tree: The tree to be drawn.

        Returns:
            A PIL image representing the current state of the tree.
        '''
        bg_color        = '#FFFFFF'
        fg_color1       = '#000000'
        fg_color2       = '#000000'
        padding_x       = 25
        padding_y       = 25
        text_padding    = 20
        tree_width      = BSTDrawer.calc_width(tree)
        tree_height     = BSTDrawer.calc_height(tree)
        node_width      = 60
        node_height     = 60
        level_height    = 120
        width           = (padding_x * 2) + (tree_width * 100)
        height          = (padding_y * 2) + (level_height * tree_height)

        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        ## Draw header
        util.draw_text_centered(
            draw,
            tree.name,
            [0, width, 0, padding_y + text_padding],
            color=fg_color1,
            bold=True
        )

        ## Draw nodes
        start_coords = (200, 100)
        BSTDrawer.draw_node(draw, tree.get_root(), start_coords, level_height, 0)

        return image
