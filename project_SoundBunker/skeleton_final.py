### 함수로 넣을 코드 최종 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##  스켈레톤 , 좌표 이동 코드 취합 완료 코드 



import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np
import math
import os

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic


class Point2D:  # 거리이동 선언 추가해본거
    def __init__(self, x, y):
        self.x = x
        self.y = y

# For static images:


#------------------------------------------------------------------------------------
def distance(IMAGE_FILES):
    dots = {}
    #list에 캡쳐사진 넣는 방식 2-  --> 성공
    # 넣고나서 주석처리해놓기 
    # for i in range(1,352):
    #     IMAGE_FILES.append(f'./cap_HouseWork/capdishwash{i}.jpg')


    #필요한 리스트 선언
    xdotlist_face=[]
    ydotlist_face=[]
    xdotlistm_face = []
    ydotlistm_face = []
    arr_sqrt_face =[]

    xdotlist_leftwrist=[]
    ydotlist_leftwrist=[]
    xdotlistm_leftwrist = []
    ydotlistm_leftwrist = []
    arr_sqrt_leftwrist =[]
    
    xdotlist_rightwrist=[]
    ydotlist_rightwrist=[]
    xdotlistm_rightwrist = []
    ydotlistm_rightwrist = []
    arr_sqrt_rightwrist =[]
    
    xdotlist_lefthip=[]
    ydotlist_lefthip=[]
    xdotlistm_lefthip = []
    ydotlistm_lefthip= []
    arr_sqrt_lefthip =[]
    
    xdotlist_righthip=[]
    ydotlist_righthip=[]
    xdotlistm_righthip = []
    ydotlistm_righthip= []
    arr_sqrt_righthip =[]
    
    
    xdotlist_leftknee=[]
    ydotlist_leftknee=[]
    xdotlistm_leftknee = []
    ydotlistm_leftknee = []
    arr_sqrt_leftknee =[]
    
    xdotlist_rightknee=[]
    ydotlist_rightknee=[]
    xdotlistm_rightknee = []
    ydotlistm_rightknee = []
    arr_sqrt_rightknee =[]    
    
    
    xdotlist_leftshoulder=[]
    ydotlist_leftshoulder=[]
    xdotlistm_leftshoulder = []
    ydotlistm_leftshoulder = []
    arr_sqrt_leftshoulder =[]   
    
    xdotlist_rightshoulder=[]
    ydotlist_rightshoulder=[]
    xdotlistm_rightshoulder = []
    ydotlistm_rightshoulder = []
    arr_sqrt_rightshoulder =[]   
    
    
    with mp_holistic.Holistic(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            refine_face_landmarks=True) as holistic:
        for idx in range(len(IMAGE_FILES)):
            image = IMAGE_FILES[idx]
            plt.imshow(image)
            plt.show()
            image_height, image_width, _ = image.shape


            #Convert the BGR image to RGB before processing.
            results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            
 

    #얼굴        
            if results.pose_landmarks:
               
                #얼굴

                globals()['x_{}nose'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y , 4))    # 얼굴

                xdotlist_face.append(globals()['x_{}nose'.format(idx)].x)
                ydotlist_face.append(globals()['x_{}nose'.format(idx)].y)
                
                #왼쪽손목

                globals()['x_{}leftwrist'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST].y , 4))    # 왼쪽손목

                xdotlist_leftwrist.append(globals()['x_{}leftwrist'.format(idx)].x)
                ydotlist_leftwrist.append(globals()['x_{}leftwrist'.format(idx)].y) 
                
                #오른쪽손목


                globals()['x_{}rightwrist'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].y , 4))    # 얼굴


                xdotlist_rightwrist.append(globals()['x_{}rightwrist'.format(idx)].x)
                ydotlist_rightwrist.append(globals()['x_{}rightwrist'.format(idx)].y)
  
                #왼쪽어깨

                globals()['x_{}leftshoulder'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].y , 4))    # 왼쪽손목

                xdotlist_leftshoulder.append(globals()['x_{}leftshoulder'.format(idx)].x)
                ydotlist_leftshoulder.append(globals()['x_{}leftshoulder'.format(idx)].y) 
                
                #오른쪽어깨


                globals()['x_{}rightshoulder'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].y , 4))    # 얼굴


                xdotlist_rightshoulder.append(globals()['x_{}rightshoulder'.format(idx)].x)
                ydotlist_rightshoulder.append(globals()['x_{}rightshoulder'.format(idx)].y)
                
                
               # 왼쪽골반

                globals()['x_{}lefthip'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HIP].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HIP].y , 4))    # 얼굴


                xdotlist_lefthip.append(globals()['x_{}lefthip'.format(idx)].x)
                ydotlist_lefthip.append(globals()['x_{}lefthip'.format(idx)].y)
                
                #오른쪽골반

                globals()['x_{}righthip'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP].y , 4))    # 얼굴


                xdotlist_righthip.append(globals()['x_{}righthip'.format(idx)].x)
                ydotlist_righthip.append(globals()['x_{}righthip'.format(idx)].y)
                
                #왼쪽 다리

                globals()['x_{}leftknee'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_KNEE].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_KNEE].y , 4))    # 얼굴


                xdotlist_leftknee.append(globals()['x_{}leftknee'.format(idx)].x)
                ydotlist_leftknee.append(globals()['x_{}leftknee'.format(idx)].y)

                #오른쪽다리
                
                globals()['x_{}rightknee'.format(idx)]= Point2D(x=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_KNEE].x,4)
                             , y=round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_KNEE].y , 4))    # 얼굴


                xdotlist_rightknee.append(globals()['x_{}rightknee'.format(idx)].x)
                ydotlist_rightknee.append(globals()['x_{}rightknee'.format(idx)].y)                
                
                
                
                
                if idx >= 1:
                    xdotlistm_face.append((globals()['x_{}nose'.format(idx -1)].x) - (globals()['x_{}nose'.format(idx)].x))
                    ydotlistm_face.append((globals()['x_{}nose'.format(idx -1)].y) - (globals()['x_{}nose'.format(idx)].y))
                    
                    xdotlistm_leftwrist.append((globals()['x_{}leftwrist'.format(idx -1)].x) - (globals()['x_{}leftwrist'.format(idx)].x))
                    ydotlistm_leftwrist.append((globals()['x_{}leftwrist'.format(idx -1)].y) - (globals()['x_{}leftwrist'.format(idx)].y))
                    
                    xdotlistm_rightwrist.append((globals()['x_{}rightwrist'.format(idx -1)].x) - (globals()['x_{}rightwrist'.format(idx)].x))
                    ydotlistm_rightwrist.append((globals()['x_{}rightwrist'.format(idx -1)].y) - (globals()['x_{}rightwrist'.format(idx)].y))
                    
                    xdotlistm_leftshoulder.append((globals()['x_{}leftshoulder'.format(idx -1)].x) - (globals()['x_{}leftshoulder'.format(idx)].x))
                    ydotlistm_leftshoulder.append((globals()['x_{}leftshoulder'.format(idx -1)].y) - (globals()['x_{}leftshoulder'.format(idx)].y))
                    
                    xdotlistm_rightshoulder.append((globals()['x_{}rightshoulder'.format(idx -1)].x) - (globals()['x_{}rightshoulder'.format(idx)].x))
                    ydotlistm_rightshoulder.append((globals()['x_{}rightshoulder'.format(idx -1)].y) - (globals()['x_{}rightshoulder'.format(idx)].y))                    
                    
                    xdotlistm_lefthip.append((globals()['x_{}lefthip'.format(idx -1)].x) - (globals()['x_{}lefthip'.format(idx)].x))
                    ydotlistm_lefthip.append((globals()['x_{}lefthip'.format(idx -1)].y) - (globals()['x_{}lefthip'.format(idx)].y))
                    
                    xdotlistm_righthip.append((globals()['x_{}righthip'.format(idx -1)].x) - (globals()['x_{}righthip'.format(idx)].x))
                    ydotlistm_righthip.append((globals()['x_{}righthip'.format(idx -1)].y) - (globals()['x_{}righthip'.format(idx)].y))

                    xdotlistm_leftknee.append((globals()['x_{}leftknee'.format(idx -1)].x) - (globals()['x_{}leftknee'.format(idx)].x))
                    ydotlistm_leftknee.append((globals()['x_{}leftknee'.format(idx -1)].y) - (globals()['x_{}leftknee'.format(idx)].y))

                    xdotlistm_rightknee.append((globals()['x_{}rightknee'.format(idx -1)].x) - (globals()['x_{}rightknee'.format(idx)].x))
                    ydotlistm_rightknee.append((globals()['x_{}rightknee'.format(idx -1)].y) - (globals()['x_{}rightknee'.format(idx)].y))


                    
                    
                    result_face = math.sqrt((xdotlistm_face[idx - 1]*xdotlistm_face[idx  - 1]) + (ydotlistm_face[idx - 1]*ydotlistm_face[idx - 1]))
                    
                    result_leftwrist = math.sqrt((xdotlistm_leftwrist[idx - 1]*xdotlistm_leftwrist[idx  - 1]) + (ydotlistm_leftwrist[idx - 1]*ydotlistm_leftwrist[idx - 1]))
                    result_rightwrist = math.sqrt((xdotlistm_rightwrist[idx - 1]*xdotlistm_rightwrist[idx  - 1]) + (ydotlistm_rightwrist[idx - 1]*ydotlistm_rightwrist[idx - 1]))
                    
                    result_leftshoulder = math.sqrt((xdotlistm_leftshoulder[idx - 1]*xdotlistm_leftshoulder[idx  - 1]) + (ydotlistm_leftshoulder[idx - 1]*ydotlistm_leftshoulder[idx - 1]))
                    result_rightshoulder = math.sqrt((xdotlistm_rightshoulder[idx - 1]*xdotlistm_rightshoulder[idx  - 1]) + (ydotlistm_rightshoulder[idx - 1]*ydotlistm_rightshoulder[idx - 1]))     
                    
                    result_lefthip = math.sqrt((xdotlistm_lefthip[idx - 1]*xdotlistm_lefthip[idx  - 1]) + (ydotlistm_lefthip[idx - 1]*ydotlistm_lefthip[idx - 1]))
                    result_righthip = math.sqrt((xdotlistm_righthip[idx - 1]*xdotlistm_righthip[idx  - 1]) + (ydotlistm_righthip[idx - 1]*ydotlistm_righthip[idx - 1]))
                    result_leftknee = math.sqrt((xdotlistm_leftknee[idx - 1]*xdotlistm_leftknee[idx  - 1]) + (ydotlistm_leftknee[idx - 1]*ydotlistm_leftknee[idx - 1]))
                    result_rightknee = math.sqrt((xdotlistm_rightknee[idx - 1]*xdotlistm_rightknee[idx  - 1]) + (ydotlistm_rightknee[idx - 1]*ydotlistm_rightknee[idx - 1]))
                    
                    dots = {
                            'face' : result_face,
                            'leftwrist' : result_leftwrist,
                            'rightwrist' : result_rightwrist,
                            'leftshoulder' : result_leftshoulder,
                            'rightshoulder' : result_rightshoulder,
                            'leftknee' : result_leftknee,
                            'rightknee' : result_rightknee,
                            'lefthip' : result_lefthip,
                            'righthip' : result_righthip
                           }
                  

                
                else:
                     dots = {
                            'face' : 0,
                            'leftwrist' :0,
                            'rightwrist' : 0,
                            'leftshoulder' : 0,
                            'rightshoulder' : 0,
                            'leftknee' : 0,
                            'rightknee' : 0,
                            'lefthip' : 0,
                            'righthip' : 0
                           }
            else:
                dots = {
                            'face' : 0,
                            'leftwrist' :0,
                            'rightwrist' : 0,
                            'leftshoulder' : 0,
                            'rightshoulder' : 0,
                            'leftknee' : 0,
                            'rightknee' : 0,
                            'lefthip' : 0,
                            'righthip' : 0
                           }
                

    return dots


#.close


    

