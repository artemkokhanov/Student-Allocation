from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from AALst import *
from SALst import *
from Read import *

from pytest import *


class TestSeqADT:

    def test_start(self):
        seq = SeqADT([1, 2])
        seq.start()
        assert seq.i == 0

    def test_next(self):
        seq = SeqADT([1, 2])
        assert seq.next() == 1
        assert seq.next() == 2

    def test_stopiteration_next(self):
        seq = SeqADT([1, 2])
        seq.next()
        seq.next()
        with raises(StopIteration):
            seq.next()

    def test_end(self):
        seq = SeqADT([1, 2])
        seq.next()
        assert seq.end() is not True
        seq.next()
        assert seq.end() is True


class TestDCapALst:

    def test_constructor_s(self):
        DCapALst.init()
        assert DCapALst.s == []

    def test_add(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        assert DCapALst.s[0] == (DeptT.civil, 2)

    def test_keyerror_add(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        with raises(KeyError):
            DCapALst.add(DeptT.civil, 2)

    def test_remove(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        assert len(DCapALst.s) == 1
        DCapALst.remove(DeptT.civil)
        assert len(DCapALst.s) == 0

    def test_keyerror_remove(self):
        DCapALst.init()
        with raises(KeyError):
            DCapALst.remove(DeptT.civil)

    def test_elm(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        assert DCapALst.elm(DeptT.civil) is True
        assert DCapALst.elm(DeptT.chemical) is False
        DCapALst.init()
        assert DCapALst.elm(DeptT.civil) is False

    def test_capacity(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        assert DCapALst.capacity(DeptT.civil) == 2

    def test_keyerror_capacity(self):
        DCapALst.init()
        with raises(KeyError):
            DCapALst.capacity(DeptT.civil)


class TestSALst:

    def test_constructor_s(self):
        SALst.init()
        assert SALst.s == []

    def test_add(self):
        sinfo1 = SInfoT("f", "l", GenT.male, 9.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.init()
        SALst.add("stdnt1", sinfo1)
        assert SALst.s[0] == ("stdnt1", sinfo1)

    def test_keyerror_add(self):
        sinfo1 = SInfoT("f", "l", GenT.male, 9.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.init()
        SALst.add("stdnt1", sinfo1)
        with raises(KeyError):
            SALst.add("stdnt1", sinfo1)

    def test_remove(self):
        sinfo1 = SInfoT("f", "l", GenT.male, 9.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.init()
        SALst.add("stdnt1", sinfo1)
        assert len(SALst.s) == 1
        SALst.remove("stdnt1")
        assert len(SALst.s) == 0

    def test_keyerror_remove(self):
        SALst.init()
        with raises(KeyError):
            SALst.remove("stdnt1")

    def test_elm(self):
        sinfo1 = SInfoT("f", "l", GenT.male, 9.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.init()
        SALst.add("stdnt1", sinfo1)
        assert SALst.elm("stdnt1") is True
        assert SALst.elm("stdnt2") is False
        SALst.init()
        assert SALst.elm("stdnt1") is False

    def test_info(self):
        sinfo1 = SInfoT("f", "l", GenT.male, 9.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.init()
        SALst.add("stdnt1", sinfo1)
        assert SALst.info("stdnt1") == sinfo1

    def test_keyerror_info(self):
        SALst.init()
        with raises(KeyError):
            SALst.info("stdnt1")

    def test_sort(self):
        load_stdnt_data("src/StdntData.txt")
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ["macid1"]

    def test_average(self):
        load_stdnt_data("src/StdntData.txt")
        assert SALst.average(lambda x: x.gender == GenT.male) == 6.7

    def test_allocate(self):
        load_stdnt_data("src/StdntData.txt")
        load_dcap_data("src/DeptCap.txt")
        SALst.allocate()
        assert AALst.lst_alloc(DeptT.software) == ["macid1"]
        assert AALst.lst_alloc(DeptT.civil) == ["smithj"]
        assert AALst.lst_alloc(DeptT.mechanical) == ["smithj2"]

    def test_runtimeerror_allocate(self):
        sinfo1 = SInfoT("f", "l", GenT.male, 9.0, SeqADT([DeptT.civil]), False)
        SALst.init()
        SALst.add("stdnt1", sinfo1)
        SALst.info("stdnt1").choices.next()
        DCapALst.init()
        DCapALst.add(DeptT.civil, 0)
        with raises(RuntimeError):
            SALst.allocate()
