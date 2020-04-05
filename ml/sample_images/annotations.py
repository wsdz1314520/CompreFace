from collections import namedtuple

from src.services.utils.pyutils import sort_coordinates

Row = namedtuple('Row', 'image_name noses')

SAMPLE_IMAGES = [
    Row('00.x5.jpg', [(219, 105), (300, 252), (392, 220), (469, 309), (600, 294)]),
    Row('01.A.jpg', [(2109, 2261)]),
    Row('02.A.jpg', [(2146, 2424)]),
    Row('03.A.jpg', [(3210, 1382)]),
    Row('04.A.jpg', [(1312, 1969)]),
    Row('05.A.jpg', [(2092, 2871)]),
    Row('06.A.jpg', [(1864, 3041)]),
    Row('07.B.jpg', [(210, 292)]),
    Row('08.B.jpg', [(225, 256)]),
    Row('09.C.jpg', [(166, 236)]),
    Row('10.x2.jpg', [(354, 232), (505, 258)]),
    Row('11.x3.jpg', [(295, 266), (484, 245), (385, 216)]),
    Row('12.x4.jpg', [(275, 196), (332, 188), (421, 197), (495, 188)]),
    Row('13.x4.jpg', [(212, 209), (319, 238), (443, 234), (629, 248)]),
    Row('14.x5.jpg', [(95, 283), (207, 262), (407, 175), (605, 270), (691, 305)]),
    Row('15.x6.jpg', [(164, 229), (269, 269), (352, 282), (453, 269), (557, 263), (635, 250)]),
    Row('16.x8.jpg', [(194, 277), (262, 169), (260, 292), (357, 278), (440, 213), (459, 287), (521, 161),
                      (691, 201)])
]

name_2_annotation = {r.image_name: sort_coordinates(r.noses) for r in SAMPLE_IMAGES}
