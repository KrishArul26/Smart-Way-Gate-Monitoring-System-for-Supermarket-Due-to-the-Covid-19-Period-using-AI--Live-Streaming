import cv2
import numpy as np
from playsound import playsound
from utils import visualization_utils as vis_util


def draw_box_1(image, boxes, classes, scores, category_index):
    vis_util.visualize_boxes_and_labels_on_image_array(image,
                                                       np.squeeze(boxes),
                                                       np.squeeze(classes).astype(np.int32),
                                                       np.squeeze(scores),
                                                       category_index,
                                                       use_normalized_coordinates=True,
                                                       line_thickness=8,
                                                       min_score_thresh=0.75)
    cv2.imshow('Object detector', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_box_2(image, boxes, classes, scores, category_index):
    vis_util.visualize_boxes_and_labels_on_image_array(image,
                                                       np.squeeze(boxes),
                                                       np.squeeze(classes).astype(np.int32),
                                                       np.squeeze(scores),
                                                       category_index,
                                                       use_normalized_coordinates=True,
                                                       line_thickness=8,
                                                       min_score_thresh=0.75)
    cv2.putText(image, "ALERT", (0, 180), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

    cv2.imshow('Object detector', image)
    playsound(r"alert.wav")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
