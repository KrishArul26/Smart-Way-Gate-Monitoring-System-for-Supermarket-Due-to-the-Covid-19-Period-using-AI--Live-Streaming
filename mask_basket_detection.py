

from mask_basket_detector import mask_detection, class_selection

from utils.draw_boxes import draw_box_1, draw_box_2

category_index, image, boxes, scores, classes, num = mask_detection('frozen_graphs',
                                                               '/frozen_inference_graph.pb',
                                                               '/labelmap.pbtxt',
                                                               3,'image8.jpg')

#print(category_index, image, boxes, scores, classes, num, sep="\n")
# draw_box_1(image, boxes, classes, scores, category_index)
#
# draw_box_2(image, boxes, classes, scores, category_index)

class_selection(scores, classes, image, category_index, boxes)

