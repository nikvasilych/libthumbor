#!/usr/bin/python
# -*- coding: utf-8 -*-

# libthumbor - python extension to thumbor
# https://github.com/heynemann/libthumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

'''libthumbor URL composer tests'''

from thumbor.crypto import Crypto

from libthumbor.url import url_for

IMAGE_URL = 'my.server.com/some/path/to/image.jpg'
IMAGE_MD5 = '84996242f65a4d864aceb125e1c4c5ba'

def decrypt_in_thumbor(key, encrypted):
    '''Uses thumbor to decrypt libthumbor's encrypted URL'''
    crypto = Crypto(key)
    return crypto.decrypt(encrypted)

def test_no_options_specified():
    '''test_no_options_specified
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
    When
        I ask my library for an URL
    Then
        I get "84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(image_url=IMAGE_URL)

    assert url == IMAGE_MD5, url

def test_url_raises_if_no_url():
    '''test_url_raises_if_no_url
    Given
        An image URL of "" or null
    When
        I ask my library for an URL
    Then
        I get an exception that says image URL is mandatory
    '''
    try:
        url_for()
    except RuntimeError, err:
        assert str(err) == 'The image_url argument is mandatory.'
        return True
    assert False, 'Should not have gotten this far'

def test_url_width_height_1():
    '''test_url_width_height_1
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a width of 300
    When
        I ask my library for an URL
    Then
        I get "300x0/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(width=300, image_url="my.server.com/some/path/to/image.jpg")

    assert url == "300x0/84996242f65a4d864aceb125e1c4c5ba", url

def test_url_width_height_2():
    '''test_url_width_height_2
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a height of 300
    When
        I ask my library for an URL
    Then
        I get "0x300/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(height=300, image_url="my.server.com/some/path/to/image.jpg")

    assert url == "0x300/84996242f65a4d864aceb125e1c4c5ba", url

def test_url_width_height_3():
    '''test_url_width_height_3
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a width of 200
        And a height of 300
    When
        I ask my library for an URL
    Then
        I get "200x300/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(width=200,
                  height=300,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "200x300/84996242f65a4d864aceb125e1c4c5ba", url

def test_smart_url():
    '''test_smart_url
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a width of 200
        And a height of 300
        And the smart flag
    When
        I ask my library for an URL
    Then
        I get "200x300/smart/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(width=200,
                  height=300,
                  smart=True,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "200x300/smart/84996242f65a4d864aceb125e1c4c5ba", url

def test_flip_1():
    '''test_flip_1
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And the flip flag
    When
        I ask my library for an URL
    Then
        I get "-0x0/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(flip=True,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "-0x0/84996242f65a4d864aceb125e1c4c5ba", url

def test_flip_2():
    '''test_flip_2
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a width of 200
        And the flip flag
    When
        I ask my library for an URL
    Then
        I get "-200x0/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(flip=True,
                  width=200,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "-200x0/84996242f65a4d864aceb125e1c4c5ba", url

def test_flop_1():
    '''test_flop_1
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And the flop flag
    When
        I ask my library for an URL
    Then
        I get "0x-0/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(flop=True,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "0x-0/84996242f65a4d864aceb125e1c4c5ba", url

def test_flop_2():
    '''test_flop_2
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a height of 200
        And the flop flag
    When
        I ask my library for an URL
    Then
        I get "0x-200/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(flop=True,
                  height=200,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "0x-200/84996242f65a4d864aceb125e1c4c5ba", url

def test_flip_flop():
    '''test_flip_flop
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And the flip flag
        And the flop flag
    When
        I ask my library for an URL
    Then
        I get "-0x-0/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(flip=True,
                  flop=True,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "-0x-0/84996242f65a4d864aceb125e1c4c5ba", url

def test_flip_flop2():
    '''test_flip_flop2
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a width of 200
        And a height of 300
        And the flip flag
        And the flop flag
    When
        I ask my library for an URL
    Then
        I get "-200x-300/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(flip=True,
                  flop=True,
                  width=200,
                  height=300,
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == "-200x-300/84996242f65a4d864aceb125e1c4c5ba", url

def test_horizontal_alignment():
    '''test_horizontal_alignment
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a 'left' horizontal alignment option
    When
        I ask my library for an URL
    Then
        I get "left/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(halign='left',
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == 'left/84996242f65a4d864aceb125e1c4c5ba', url

def test_horizontal_alignment2():
    '''test_horizontal_alignment2
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a 'center' horizontal alignment option
    When
        I ask my library for an URL
    Then
        I get "84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(halign='center',
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == '84996242f65a4d864aceb125e1c4c5ba', url

def test_vertical_alignment():
    '''test_vertical_alignment
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a 'top' vertical alignment option
    When
        I ask my library for an URL
    Then
        I get "top/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(valign='top',
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == 'top/84996242f65a4d864aceb125e1c4c5ba', url

def test_vertical_alignment2():
    '''test_vertical_alignment2
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a 'middle' vertical alignment option
    When
        I ask my library for an URL
    Then
        I get "84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(valign='middle',
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == '84996242f65a4d864aceb125e1c4c5ba', url

def test_both_alignments():
    '''test_both_alignments
    Given
        An image URL of "my.server.com/some/path/to/image.jpg"
        And a 'left' horizontal alignment option
        And a 'top' vertical alignment option
    When
        I ask my library for an URL
    Then
        I get "left/top/84996242f65a4d864aceb125e1c4c5ba" as URL
    '''
    url = url_for(halign='left',
                  valign='top',
                  image_url="my.server.com/some/path/to/image.jpg")

    assert url == 'left/top/84996242f65a4d864aceb125e1c4c5ba', url

def test_proper_haligns():
    '''test_proper_haligns'''
    try:
        url_for(halign='wrong', image_url=IMAGE_URL)
    except ValueError, err:
        assert str(err) == 'Only "left", "center" and "right"' + \
                           ' are valid values for horizontal alignment.'
        return True
    assert False, "Should not have gotten this far."

def test_proper_valigns():
    '''test_proper_haligns'''
    try:
        url_for(valign='wrong', image_url=IMAGE_URL)
    except ValueError, err:
        assert str(err) == 'Only "top", "middle" and "bottom"' + \
                           ' are valid values for vertical alignment.'
        return True
    assert False, "Should not have gotten this far."

