#!/usr/bin/env python

"""Tests the FileParser API
"""

from tvnamer.files import FileParser
from tvnamer.data import EpisodeInfo, DatedEpisodeInfo, NoSeasonEpisodeInfo
from helpers import assertType, assertEquals


def test_episodeinfo():
    """Parsing a s01e01 episode should return EpisodeInfo class
    """
    p = FileParser("/foo/bar/scrubs.s01e01.avi").parse()
    assertType(p, EpisodeInfo)


def test_datedepisodeinfo():
    """Parsing a 2009.06.05 episode should return DatedEpisodeInfo class
    """
    p = FileParser("/foo/bar/scrubs.2009.06.05.avi").parse()
    assertType(p, DatedEpisodeInfo)


def test_noseasonepisodeinfo():
    """Parsing a e23 episode should return NoSeasonEpisodeInfo class
    """
    p = FileParser("/foo/bar/scrubs - e23.avi").parse()
    assertType(p, NoSeasonEpisodeInfo)


def test_episodeinfo_naming():
    """Parsing a s01e01 episode should return EpisodeInfo class
    """
    p = FileParser("/foo/bar/scrubs.s01e01.avi").parse()
    assertType(p, EpisodeInfo)
    assertEquals(p.generate_filename().lower(), "scrubs - [01x01].avi".lower())


def test_datedepisodeinfo_naming():
    """Parsing a 2009.06.05 episode should return DatedEpisodeInfo class
    """
    p = FileParser("/foo/bar/scrubs.2009.06.05.avi").parse()
    assertType(p, DatedEpisodeInfo)
    assertEquals(p.generate_filename().lower(), "scrubs - [2009-06-05].avi".lower())


def test_noseasonepisodeinfo_naming():
    """Parsing a e23 episode should return NoSeasonEpisodeInfo class
    """
    p = FileParser("/foo/bar/scrubs - e23.avi").parse()
    assertType(p, NoSeasonEpisodeInfo)
    assertEquals(p.generate_filename().lower(), "scrubs - [23].avi".lower())
