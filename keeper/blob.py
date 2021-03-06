#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

DISCLAIMER

This is crap code that works. I wrote it 3 years ago.

"""

import cv2
import numpy as np
from point import Point


class Blob:

    def __init__(self, centroid, convexHull, convexHullArea,\
            contour, contourArea):

        self.centroid = centroid
        self.convexHull = convexHull
        self.contour = contour
        self.convexHullArea = convexHullArea
        self.contourArea = contourArea

    def get_centroid(self):
        retCentroid = Point(
            self.centroid[0],
            self.centroid[1]
        )
        return retCentroid

    def get_convex_hull(self):
        return self.convexHull

    def get_contour(self):
        return self.contour

    def get_convex_hull_area(self):
        return self.convexHullArea

    def get_contour_area(self):
        return self.contourArea


def get_blobs(BW, minSize, maxSize=None):

    cs, _ = cv2.findContours(
        BW.astype(np.uint8),
        mode = cv2.RETR_EXTERNAL,
        method = cv2.CHAIN_APPROX_SIMPLE
    )

    blobList = list()
    for con in cs:
        if maxSize == None:
            _maxSize = abs(cv2.contourArea(con)) + 1
        else:
            _maxSize = maxSize

        if abs(cv2.contourArea(con)) > minSize and\
                abs(cv2.contourArea(con)) < _maxSize:

            m = cv2.moments(con)
            try:
                # image moments
                m10 = m['m10']
                m00 = m['m00']
                m01 = m['m01']

                cHull = cv2.convexHull(con)

                blobList += [Blob(
                    (int(m10/m00), int(m01/m00)),
                    cHull, cv2.contourArea(cHull),
                    con, cv2.contourArea(con)
                )]
            except:
				pass

    return blobList

