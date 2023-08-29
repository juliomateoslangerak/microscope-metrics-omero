import logging

from microscopemetrics_omero import omero_tools
from omero.gateway import (
    ImageWrapper,
    DatasetWrapper,
    ProjectWrapper,
)
import numpy as np

# Creating logging services
logger = logging.getLogger(__name__)


def load_image(image: ImageWrapper) -> np.ndarray:
    """Load an image from OMERO and return it as a numpy array in the order desired by the analysis"""
    # OMERO order zctyx -> to microscope metrics order TZYXC
    return omero_tools.get_image_intensities(image).transpose((2, 0, 3, 4, 1))


def load_dataset(dataset):
    pass


def load_project(project):
    pass
