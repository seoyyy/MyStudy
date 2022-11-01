#!/usr/bin/env python
# coding: utf-8

# In[11]:


from matplotlib import scale
import torch
import numpy as np
import cv2
import pandas as pd
import math

yolo_result=''

def getYOLO(img) :

    try :
        # 모델 로드
        torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='0727last.pt', force_reload=True)

        # 이미지 받아오기 

        #for img in enumerate(IMAGE_FILES):



            # 모델 돌린 결과 중 라벨값 변수에 담아주기 
               
        results = model(img)

        findThing = results.pandas().xyxy[0]['name']
        findList=[]
        for find in findThing :
            findList.append(find)
        print(findList) 

        # 좌푯값 받아오기
        xmin = results.pandas().xyxy[0]['xmin']
        xmax = results.pandas().xyxy[0]['xmax']
        ymin = results.pandas().xyxy[0]['ymin']
        ymax = results.pandas().xyxy[0]['ymax']

        # 좌푯값 데이터 프레임에 저장

        dots = results.pandas().xyxy[0]
        dotsdf = pd.DataFrame(dots)
        dotsdf['xpoint'] = (xmin+xmax)/2
        dotsdf['ypoint'] = (ymin+ymax)/2

        # 라벨들 바운딩 박스 중앙 좌표값

        persondot = dotsdf[dotsdf['name']=='person'][['xpoint','ypoint']]
        notpersondot = dotsdf[dotsdf['name']!='person'][['name','xpoint','ypoint']]

        if notpersondot.empty :
            yolo_result = 'noobject'
            #continue

        if persondot.empty :
            yolo_result = 'noperson'
            #continue

        persondotlist = persondot.values.tolist()
        notpersondotlist = notpersondot.values.tolist()



        # 사람 좌표와 객체 좌표간 거리 구하기

        distance = []

        for i in range (len(notpersondotlist)) :
            distance.append(math.sqrt(math.pow(int(persondotlist[0][0]) - int(notpersondotlist[i][1]) , 2) + math.pow(int(persondotlist[0][1]) - int(notpersondotlist[i][2]) , 2) ) )

        # 가장 가까운 값 구하기 위해 객체와의 거리값 데이터프레임에 컬럼으로 추가 

        notpersondot['distance'] = distance

        # name값 변수로 담아주기

        yolo_result = notpersondot[notpersondot["distance"] == notpersondot["distance"].min()].iloc[0,0]
        print(yolo_result + '가 검출되었습니다')

        # if 문으로 스켈레톤 값과 YOLO name 값 취합해서 Str 형태 타입으로 반환해주기 


        # Results
        results.print()

    except IndexError:
        pass
        
    return yolo_result


# if yolo_result == 'book' and skeleton_result == 'less_active' :
#     final_result == 'reading'
# elif yolo_result == 'dumbbell' and skeleton_result == 'active' :
#     final_result == 'workout'

