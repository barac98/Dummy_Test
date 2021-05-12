import logging
import time

# Needed for aetest script
import sys
from ats import aetest

# Get your logger for your script
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

tc_count = 0

class Testcase1(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count))

class Testcase41(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count) + " SHOULD FAIL")
        self.failed("yea")

class Testcase49(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count) + " SHOULD FAIL")
        self.failed("yea")

class Testcase50(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count) + " SHOULD FAIL")
        self.failed("yea")

class Testcase21(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count))

class Testcase24(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count))

class Testcase25(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count))

class Testcase26(aetest.Testcase):
    @aetest.test
    def pass_tc(self):
        global tc_count
        tc_count += 1
        log.info("TC: " + str(tc_count))

if __name__ == '__main__':  # pragma: no cover
    aetest.main()
    # end test file
