#!/usr/bin/env python

"""Test ability to set the series name by series id
"""

from functional_runner import run_tvnamer, verify_out_data
from helpers import attr


@attr("functional")
def test_ambiguity_fix():
    """Test ambiguous episode number fix
    """

    conf = """
    {"always_rename": true,
    "titlecase_filename": false,
    "select_first": true}
    """

    out_data = run_tvnamer(
        with_files = ['[ANBU-AonE]_Naruto_43_[3811CBB5].avi'],
        with_config = conf,
        with_flags = [],
        with_input = "")

    expected_files = ['[ANBU-AonE] Naruto - 43 - Killer Kunoichi and a Shaky Shikamaru [3811CBB5].avi']

    verify_out_data(out_data, expected_files)
