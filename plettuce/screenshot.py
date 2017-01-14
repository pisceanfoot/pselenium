"""Steps and utility functions for taking screenshots."""

import uuid

from lettuce import (
    after,
    step,
    world,
)
import os
import os.path
import json

def set_save_from_env():
    root = os.getenv('pselenium_screenshot_save_path', None)
    if root:
        if not os.path.isdir(root):
            os.makedirs(root)
        world.screenshot_root = root

def set_save_directory(base, source):
    """Sets the root save directory for saving screenshots.
    
    Screenshots will be saved in subdirectories under this directory by
    browser window size. """
    root = os.path.join(base, source)
    if not os.path.isdir(root):
        os.makedirs(root)

    world.screenshot_root = root


def resolution_path(world):
    window_size = world.browser.get_window_size()
    return os.path.join(
        world.screenshot_root,
        '{}x{}'.format(window_size['width'], window_size['height']),
    )


@step(r' screenshot$')
def capture_screenshot(step):
    if not getattr(world, 'screenshot_root', None):
        set_save_from_env()

    if not getattr(world, 'screenshot_root', None):
        return

    feature = step.scenario.feature
    step.shot_name = '{}.png'.format(uuid.uuid4())
    if getattr(feature, 'dir_path', None) is None:
        feature.dir_path = resolution_path(world)

    if not os.path.isdir(feature.dir_path):
        os.makedirs(feature.dir_path)

    filename = os.path.join(
        feature.dir_path,
        step.shot_name,
    )
    world.browser.get_screenshot_as_file(filename)
