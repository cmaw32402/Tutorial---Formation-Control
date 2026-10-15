import numpy as np
import cv2
import settings
from scipy.optimize import linear_sum_assignment
#returns robots' positions in ideal formation
def p_star():


    p_star = np.zeros((settings.ROBOTS_N, 2))
    for k in range(settings.ROBOTS_N):

        #evenly spaced points around circle
        th = 2 * np.pi * k / settings.ROBOTS_N
        p_star[k] = [
            settings.SHAPE_R * np.cos(th),
            settings.SHAPE_R * np.sin(th)
        ]
    return p_star



        