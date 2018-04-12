import cv2


def splitImage(inImg):
    h, w = inImg.shape[0], inImg.shape[1]
    off1X = 0
    off1Y = 0
    off2X = 0
    off2Y = 0

    if w >= h:  # split X
        off1X = 0
        off2X = w // 2
        img1 = inImg[0:h, 0:off2X]
        img2 = inImg[0:h, off2X:w]
    else:  # split Y
        off1Y = 0
        off2Y = h // 2
        img1 = inImg[0:off2Y, 0:w]
        img2 = inImg[off2Y:h, 0:w]

    return off1X, off1Y, img1, off2X, off2Y, img2


class theQTree:

    def qt(self, inImg, minStd, minSize, offX, offY):
        h, w = inImg.shape[0], inImg.shape[1]
        m, s = cv2.meanStdDev(inImg)

        if s >= minStd and max(h, w) > minSize:
            oX1, oY1, im1, oX2, oY2, im2 = splitImage(inImg)

            self.qt(im1, minStd, minSize, offX + oX1, offY + oY1)
            self.qt(im2, minStd, minSize, offX + oX2, offY + oY2)
        else:
            self.listRoi.append([offX, offY, w, h, m, s])

    def __init__(self, img, stdmin, sizemin):
        self.listRoi = []
        self.qt(img, stdmin, sizemin, 0, 0)


offx = 0
offy = 0


def quadtree(inImg, minStd, minSize, offX, offY, roiList):
    h, w = inImg.shape[0], inImg.shape[1]
    m, s = cv2.meanStdDev(inImg)

    if s >= minStd and max(h, w) > minSize:
        oX1, oY1, im1, oX2, oY2, im2 = splitImage(inImg)

        quadtree(im1, minStd, minSize, offX + oX1, offY + oY1, roiList)
        quadtree(im2, minStd, minSize, offX + oX2, offY + oY2, roiList)
    else:
        roiList.append([offX, offY, w, h, m, s])


def get_node_count(image_path, minDev=10, minSz=10.0):
    IMAGE_TO_LOAD = image_path
    minDev = minDev
    minSz = minSz

    raw = cv2.imread(IMAGE_TO_LOAD)

    if not type(raw) == type(None):
        if raw.ndim > 1:
            img = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
        else:
            img = raw
    else:
        print('Error on input image: ' + IMAGE_TO_LOAD)
        return 0

    qt = theQTree(img, minDev, minSz)
    rois = qt.listRoi
    return len(rois)


print(get_node_count('C:/Users/bunny/Desktop/images-227/1stsource.com/20030406124422.png'))
