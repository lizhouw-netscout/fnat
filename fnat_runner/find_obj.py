#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2
from common import anorm, getsize
import sys, getopt


def init_feature():
    detector = cv2.ORB(400)
    norm = cv2.NORM_HAMMING
    matcher = cv2.BFMatcher(norm)
    return detector, matcher

def filter_matches(kp1, kp2, matches, ratio = 0.75):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, kp_pairs

def verify(kp_pairs):
    kp_size = len(kp_pairs)
    if kp_size < 4:
        return False
    else:
        total_span_x = 0
        total_span_y = 0
        bad_points = 0
        list_span = []
        for i in range(0, kp_size):
            span_x = kp_pairs[i][0].pt[0] - kp_pairs[i][1].pt[0]
            span_y = kp_pairs[i][0].pt[1] - kp_pairs[i][1].pt[1]
            total_span_x = total_span_x + span_x
            total_span_y = total_span_y + span_y
            list_span.append((span_x, span_y))
        total_span_x = total_span_x / kp_size
        total_span_y = total_span_y / kp_size
        for i in range(0, kp_size):
            if abs(list_span[i][0] - total_span_x) > 2 or abs(list_span[i][1] - total_span_y) > 2:
                bad_points = bad_points + 1
        if bad_points / kp_size >= 0.8:
            return False
        else:
            return True

def  match_similar_size_images (img1, img2, detector, matcher):
    kp1, desc1 = detector.detectAndCompute(img1, None)
    kp2, desc2 = detector.detectAndCompute(img2, None)

    raw_matches = matcher.knnMatch(desc1, trainDescriptors = desc2, k = 2) #2
    p1, p2, kp_pairs = filter_matches(kp1, kp2, raw_matches)

    if len(p1) >= 4:
        H, status = cv2.findHomography(p1, p2, cv2.RANSAC, 5.0)
        if True == verify(kp_pairs):
            return ((int)(img1.shape[1] / 2), (int)(img1.shape[0] / 2))
        else:
            return (-1, -1)
    else:
        H, status = None, None
        return (-1, -1)

def  match_similar_width_vary_height_images (img1, img2, detector, matcher):
    height_1 = img1.shape[0]
    height_2 = img2.shape[0]
    height_part = height_2
    height_span = (int)(height_2 / 2)
    for i in range(0, height_1 - height_span, height_span):
        party_img1 = img1[i : i + height_span, 0 : img1.shape[1] - 1]
        point_center = match_similar_size_images(party_img1, img2, detector, matcher)
        if point_center[0] >= 0 and point_center[1] >= 0:
            return (point_center[0], i + point_center[1])
    return (-1, -1)

def  match_similar_height_vary_width_images (img1, img2, detector, matcher):
    width_1 = img1.shape[1]
    width_2 = img2.shape[1]
    width_part = width_2
    width_span = (int)(width_2 / 2)
    for i in range(0, width_1 - width_span, width_span):
        party_img1 = img1[0 : img1.shape[0] - 1, i : i + width_span]
        point_center = match_similar_size_images(party_img1, img2, detector, matcher)
        if point_center[0] >= 0 and point_center[1] >= 0:
            return (point_center[0] + i, point_center[1])
    return (-1, -1)
    
def  match_vary_size_images (img1, img2, detector, matcher):
    height_1 = img1.shape[0]
    width_1 = img1.shape[1]
    height_2 = img2.shape[0]
    width_2 = img2.shape[1]
    height_part = height_2
    width_part = width_2
    height_span = (int)(height_2 / 2)
    width_span = (int)(width_2 / 2)
    for i in range(0, height_1 - height_span, height_span):
        for j in range(0, width_1 - width_span, width_span):
            party_img1 = img1[i : i + height_part, j : j + width_part]
            point_center = match_similar_size_images(party_img1, img2, detector, matcher)
            if point_center[0] >= 0 and point_center[1] >= 0:
                return (point_center[0] + j, point_center[1] + i)
                
    for i in range(0, height_1 - height_span, height_span):
        party_img1 = img1[i : i + height_span, width_1 - width_span - 1 : width_1 - 1]
        point_center = match_similar_size_images(party_img1, img2, detector, matcher)
        if point_center[0] >= 0 and point_center[1] >= 0:
            return (point_center[0] + width_1 - width_span - 1, point_center[1] + i)
        
    for i in range(0, width_1 - width_span, width_span):
        party_img1 = img1[height_1 - height_span - 1 : height_1 - 1, i : i + width_span]
        point_center = match_similar_size_images(party_img1, img2, detector, matcher)
        if point_center[0] >= 0 and point_center[1] >= 0:
            return (point_center[0] + i, point_center[1] + height_1 - height_span - 1)

    point_center = match_similar_size_images(img1[height_1 - height_span - 1 : height_1 - 1, width_1 - width_span - 1 : width_1 - 1], img2, detector, matcher)
    if point_center[0] >= 0 and point_center[1] >= 0:
        return (point_center[0] + width_1 - width_span - 1, point_center[1] + height_1 - height_span - 1)
    else:
        return (-1, -1)

def find_obj (fn1, fn2):
    img1 = cv2.imread(fn1, 0)
    img2 = cv2.imread(fn2, 0)
    detector, matcher = init_feature()

    height_1 = img1.shape[0]
    width_1 = img1.shape[1]
    height_2 = img2.shape[0]
    width_2 = img2.shape[1]

    if (height_1 > 2 * height_2) and (width_1 > 2 * width_2):
        return match_vary_size_images(img1, img2, detector, matcher)
    else:
        if  height_1 > 2 * height_2:
            return match_similar_width_vary_height_images(img1, img2, detector, matcher)
        else:
            if width_1 > 2 * width_2:
                return match_similar_height_vary_width_images(img1, img2, detector, matcher)
            else:
                return match_similar_size_images(img1, img2, detector, matcher)

