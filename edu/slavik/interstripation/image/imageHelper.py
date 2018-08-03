import numpy

from PIL import Image
from random import randint

"""
Consist operations with images

@author: oleksii.slavik
"""


def getImageData(fileName: str):
    """
    Create matrix of image

    :param fileName: path to image
    :return: matrix of image
    """
    imageData = Image.open('../resources/' + fileName)
    grayscale = imageData.convert('L')
    return numpy.array(grayscale)


def saveImageData(data, fileName: str, imageFormat='PNG'):
    """
    Save image data into file

    :param data:        image data
    :param fileName:    path to file
    :param imageFormat: image format
    """
    imageData = Image.fromarray(data, 'L')
    imageData.save('../resources/' + fileName, imageFormat)


# def removeStripes(image, countV, countH, maxWidth, maxHeight):
#    for i in range(image.shape[0]):

def removeVerticalStripes(imageData, count, maxWidth):
    """
    Delete vertical stripes from image

    :param imageData: initial image data
    :param count:     count of stripes
    :param maxWidth:  maximum value of stripe width
    :return: image data with removed stripes
    """
    width = imageData.shape[0]
    height = imageData.shape[1]
    step = int(width / count)
    for k in range(count):
        for i in createRandomRange(k * step, (k + 1) * step, maxWidth):
            for j in range(height):
                imageData[j, i] = -1
    return imageData


def removeHorizontalStripes(imageData, count, maxHeight):
    """
    Delete horizontal stripes from image

    :param imageData:  initial image data
    :param count:      count of stripes
    :param maxHeight:  maximum value of stripe width
    :return: image data with removed stripes
    """
    width = imageData.shape[0]
    height = imageData.shape[1]
    step = int(height / count)
    for k in range(count):
        for i in createRandomRange(k * step, (k + 1) * step, maxHeight):
            for j in range(width):
                imageData[i, j] = -1
    return imageData


def createRandomRange(leftValue, rightValue, maxWidth):
    """
    Create random range

    :param leftValue:  left range value
    :param rightValue: right range value
    :param maxWidth:   maximum range width
    :return: generated range
    """
    width = randint(1, maxWidth)
    left = randint(leftValue, rightValue - maxWidth)
    return range(left, left + width)
