# coding: utf-8

import os
import random
import string

from PIL import Image, ImageSequence


def generate_frame_name(image_filename, frame_index):
    """
    """
    image_filename_base = image_filename.split('.')[0]
    return '{}_{:0>4}.png'.format(image_filename_base, frame_index)


def generate_gif_name():
    """
    """
    random_filename = ''.join(
        random.sample(string.ascii_letters + string.digits, 8)
    )
    return '{}.gif'.format(random_filename)


def analys_image(image_path):
    """
    source: https://gist.github.com/BigglesZX/4016539

    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode
    before processing all frames.
    """
    image = Image.open(image_path)
    results = {
        'size': image.size,
        'mode': 'full',
    }
    for frame in ImageSequence.Iterator(image):
        if frame.tile:
            tile = frame.tile[0]
            update_region = tile[1]
            update_region_dimensions = update_region[2:]
            if update_region_dimensions != frame.size:
                results['mode'] = 'partial'
                break
    return results


def split_gif2frame(image_path):
    """
    Iterate the GIF, extracting each frame.
    """
    mode = analys_image(image_path)['mode']

    image_dirname = os.path.dirname(image_path)
    image_filename = os.path.basename(image_path)
    image = Image.open(image_path)

    frame_file_list = []
    palette = image.getpalette()
    last_frame = image.convert('RGBA')

    for frame_index, frame in enumerate(ImageSequence.Iterator(image)):
        if not frame.getpalette():
            frame.putpalette(palette)

        new_frame = Image.new("RGBA", frame.size)
        if mode == 'partial':
            new_frame.paste(last_frame)

        new_frame.paste(frame, (0, 0), frame.convert('RGBA'))
        # new_frame_filename = generate_frame_name(image_filename, frame_index)
        # new_frame_path = os.path.join(image_dirname, new_frame_filename)
        # new_frame.save(new_frame_path, 'PNG')
        # frame_file_list.append(new_frame_path)
        frame_file_list.append(new_frame)

        last_frame = new_frame

    return frame_file_list


def create_gif(frame_file_list, image_path):
    """
    """
    # first_frame = Image.open(frame_file_list[0])
    # images = []
    # for frame_file in frame_file_list[1:]:
    #     images.append(Image.open(frame_file))
    first_frame = frame_file_list[0]
    images = frame_file_list[1:]

    gif_filename = generate_gif_name()
    # gif_dirname = os.path.dirname(frame_file_list[0])
    gif_dirname = os.path.dirname(image_path)
    gif_path = os.path.join(gif_dirname, gif_filename)
    first_frame.save(
        gif_path,
        save_all=True,
        append_images=images,
        loop=1,
        duration=0.1,
        comment=''
    )
    return gif_path


def reverse_gif(image_path):
    """
    """
    frame_file_list = split_gif2frame(image_path)
    frame_file_list.reverse()
    new_gif_path = create_gif(frame_file_list, image_path)
    return new_gif_path


