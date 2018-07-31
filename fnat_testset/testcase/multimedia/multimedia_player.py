from testconfig import config
import time
import sys
import os


class multimedia_player:
    def setUp(self):
        print "Constructor of class multimedia_player"

    def tearDown(self):
        print "Disconstructor of class multimedia_player"

    def testmethod_1(self):
        print "Method testmethod_1 in class testclass_1"
        print "We will play media from " + config["path"] + " after " + config["play_delay"] + " seconds delay"
        assert True


