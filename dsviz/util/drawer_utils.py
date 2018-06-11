'''Utilities for data structure drawers.'''

import os

from dsviz import PROJECT_ROOT
from PIL import ImageFont


ROBOTO_REGULAR_14 = ImageFont.truetype(
        os.path.join(PROJECT_ROOT, 'fonts', 'ttf', 'Roboto-Regular.ttf'),
        14)
ROBOTO_BOLD_16 = ImageFont.truetype(
        os.path.join(PROJECT_ROOT, 'fonts', 'ttf', 'Roboto-Bold.ttf'),
        16)
DEFAULT_FONT = ROBOTO_REGULAR_14
BOLD_FONT = ROBOTO_BOLD_16


def get_textsize(draw, text, font=DEFAULT_FONT):
    '''Returns the text height and width of the text.

    Args:
        draw: The object to be drawn on.
        text: The text being evaluated.
        font: The font of the text.

    Returns:
        A 2-tuple containing both the width and height of the text.
    '''
    return draw.textsize(text, font=font)


def draw_text(
        draw,
        text,
        xy,
        color='#000000',
        bold=False):
    '''Draws text on an image starting at the given dimensions.

    Args:
        draw: The object to be drawn on.
        text: The text being drawn.
        xy: A pair of xy coordinates where the text will start.
        color: The color to use for the text.
        bold: A boolean that if true will draw the text in bold.
    '''
    font = DEFAULT_FONT
    if bold:
        font = BOLD_FONT
    draw.text(xy, text, font=font, fill=color)


def draw_text_centered(
        draw,
        text,
        xy,
        color='#000000',
        bold=False):
    '''Draws text on an image centered within the given dimensions.

    Args:
        draw: The object to be drawn on.
        text: The text being drawn.
        xy: The four points to define the bounding box.
        color: The color to use for the text.
        bold: A boolean that if true will draw the text in bold.
    '''
    font = DEFAULT_FONT
    if bold:
        font = BOLD_FONT
    text_width, text_height = get_textsize(draw, text, font)
    width, height = xy[1]-xy[0], xy[3]-xy[2]

    if text_width > width:
        text = text[:-3] + '...'
        text_width, text_height = get_textsize(draw, text, font)

    ## Delete characters from the right until text_width is less than width
    while text_width > width:
        text = text[:-4] + '...'
        text_width, text_height = get_textsize(draw, text, font)

    draw.text(
            (((width-text_width)/2)+xy[0], ((height-text_height)/2)+xy[2]),
            text,
            font=font,
            fill=color)


def draw_rectangle_with_text(
        draw,
        text,
        xy,
        fill_color='#FFFFFF',
        outline_color='#000000',
        text_color='#000000'):
    '''Draws a rectangle on an image with text centered inside.

    Args:
        draw: The object to be drawn on.
        text: The text being drawn.
        xy: The four points to define the bounding box.
        fill_color: The color to use for the fill.
        outline_color: The color to use for the outline.
        text_color: The color to use for the text.
    '''
    draw.rectangle(xy, fill=fill_color, outline=outline_color)
    xy = [xy[0], xy[2], xy[1], xy[3]]
    draw_text_centered(draw, text, xy, color=text_color)


def draw_ellipsis_with_text(
        draw,
        text,
        xy,
        fill_color='#FFFFFF',
        outline_color='#000000',
        text_color='#000000'):
    '''Draws an ellipsis on an image with text centered inside.

    Args:
        draw: The object to be drawn on.
        text: The text being drawn.
        xy: The four points to define the bounding box.
        fill_color: The color to use for the fill.
        outline_color: The color to use for the outline.
        text_color: The color to use for the text.
    '''
    draw.ellipsis(xy, fill=fill_color, outline=outline_color)
    xy = [xy[0], xy[2], xy[1], xy[3]]
    draw_text_centered(draw, text, xy, color=text_color)


def draw_arrow(
        draw,
        tail,
        size,
        direction,
        color='#000000',
        width=1):
    '''Draws an arrow in the left direction.

    Args:
        draw: The object to be drawn on.
        tail: A pair of coordinates where the tail of the arrow is.
        size: The length of the arrow.
        direction: A string representing the direction of the arrow (up, down, left, right).
        color: The color to use for the arrow.
        width: The width of the arrow.
    '''
    if direction == 'up':
        head = (tail[0], tail[1]-size)
        draw.line([tail, head], fill=color, width=width)
        draw.polygon([head, (head[0]-6, head[1]+10), (head[0]+6, head[1]+10)], fill=color)
    elif direction == 'down':
        head = (tail[0], tail[1]+size)
        draw.line([tail, head], fill=color, width=width)
        draw.polygon([head, (head[0]-6, head[1]-10), (head[0]+6, head[1]-10)], fill=color)
    elif direction =='left':
        head = (tail[0]-size, tail[1])
        draw.line([tail, head], fill=color, width=width)
        draw.polygon([head, (head[0]+10, head[1]-6), (head[0]+10, head[1]+6)], fill=color)
    elif direction == 'right':
        head = (tail[0]+size, tail[1])
        draw.line([tail, head], fill=color, width=width)
        draw.polygon([head, (head[0]-10, head[1]-6), (head[0]-10, head[1]+6)], fill=color)
