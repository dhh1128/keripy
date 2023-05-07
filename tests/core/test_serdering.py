# -*- encoding: utf-8 -*-
"""
tests.core.test_serdering module

"""
import dataclasses
import json
from collections import namedtuple

import cbor2 as cbor
import msgpack

import pytest

from keri.core import coring
from keri.core.serdering import Serder, Serdery



def test_serder():
    """
    Test Serder
    """

    # Test Serder

    assert Serder.Labels[None].saids == ['d']
    assert Serder.Labels[None].fields == ['v', 'd']

    # said field labels must be subset of all field labels
    assert set(Serder.Labels[None].saids) <= set(Serder.Labels[None].fields)


    with pytest.raises(ValueError):
        serder = Serder()

    sad = dict(v=coring.Vstrings.json, #
               d="")
    saider, sad = coring.Saider.saidify(sad=sad)
    assert sad == {'v': 'KERI10JSON00004c_',
                   'd': 'EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d'}

    assert saider.qb64 == sad["d"]

    serder = Serder(sad=sad)
    assert serder.raw == (b'{"v":"KERI10JSON00004c_",'
                          b'"d":"EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d"}')
    assert serder.sad == sad
    assert serder.proto == coring.Protos.keri
    assert serder.version == coring.Versionage(major=1, minor=0)
    assert serder.size == 76
    assert serder.kind == coring.Serials.json
    assert serder.said == saider.qb64
    assert serder.saidb == saider.qb64b
    assert serder.ilk == None
    assert serder._dcode == coring.DigDex.Blake3_256
    assert serder._pcode == coring.DigDex.Blake3_256

    assert serder.pretty() == ('{\n'
                                ' "v": "KERI10JSON00004c_",\n'
                                ' "d": "EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d"\n'
                                '}')

    assert serder.compare(said=saider.qb64)
    assert serder.compare(said=saider.qb64b)
    assert not serder.compare(said='EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8e')

    raw = serder.raw  # save for later tests

    serder = Serder(sad=sad, saidify=True)  # test saidify
    assert serder.raw == (b'{"v":"KERI10JSON00004c_",'
                          b'"d":"EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d"}')
    assert serder.sad == sad
    assert serder.proto == coring.Protos.keri
    assert serder.version == coring.Versionage(major=1, minor=0)
    assert serder.size == 76
    assert serder.kind == coring.Serials.json
    assert serder.said == saider.qb64
    assert serder.saidb == saider.qb64b
    assert serder.ilk == None
    assert serder._dcode == coring.DigDex.Blake3_256
    assert serder._pcode == coring.DigDex.Blake3_256

    assert serder.pretty() == ('{\n'
                                ' "v": "KERI10JSON00004c_",\n'
                                ' "d": "EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d"\n'
                                '}')

    assert serder.compare(said=saider.qb64)
    assert serder.compare(said=saider.qb64b)
    assert not serder.compare(said='EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8e')



    serder = Serder(raw=raw)
    assert serder.raw == (b'{"v":"KERI10JSON00004c_",'
                          b'"d":"EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d"}')
    assert serder.sad == sad
    assert serder.proto == coring.Protos.keri
    assert serder.version == coring.Versionage(major=1, minor=0)
    assert serder.size == 76
    assert serder.kind == coring.Serials.json
    assert serder.said == saider.qb64
    assert serder.saidb == saider.qb64b
    assert serder.ilk == None
    assert serder._dcode == coring.DigDex.Blake3_256
    assert serder._pcode == coring.DigDex.Blake3_256

    assert serder.pretty() == ('{\n'
                                ' "v": "KERI10JSON00004c_",\n'
                                ' "d": "EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d"\n'
                                '}')

    assert serder.compare(said=saider.qb64)
    assert serder.compare(said=saider.qb64b)
    assert not serder.compare(said='EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8e')


    serder = Serder(raw=raw, verify=True)  # test verify
    assert serder.raw == (b'{"v":"KERI10JSON00004c_",'
                          b'"d":"EN5gqodYDGPSYQvdixCjfD2leqb6zhPoDYcB21hfqu8d"}')
    assert serder.sad == sad
    assert serder.proto == coring.Protos.keri
    assert serder.version == coring.Versionage(major=1, minor=0)
    assert serder.size == 76
    assert serder.kind == coring.Serials.json
    assert serder.said == saider.qb64
    assert serder.saidb == saider.qb64b
    assert serder.ilk == None
    assert serder._dcode == coring.DigDex.Blake3_256
    assert serder._pcode == coring.DigDex.Blake3_256

    # test cbor and msgpack versions of Serder
    # make .verify() for real and test
    # make .saidify for real and test
    # make PreDex PrefixCodex of valid identifier prefix codes


    """End Test"""



if __name__ == "__main__":
    test_serder()
