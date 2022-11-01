#!/usr/bin/env python
# coding: utf-8


# pip install --user torch
# pip install --user torchvision
# pip install --user pandas
# pip install --user seaborn
# pip install --user 



import skeleton_final
import yolo_final as yolo



# IMAGE_FILES =[]
# for i in range(1,207):
#     IMAGE_FILES.append(f'./Rest/rest{i}.jpg')


def getstatement(IMAGE_FILES):

    dots = skeleton_final.distance(IMAGE_FILES)



    sum(dots.values())




    result = sum(dots.values())/len(dots)
    skeleton_result=''


    if result > 0.1:
        skeleton_result = 'active'
        print("active한 상태입니다")   # 완전 신나는 노래
    elif result > 0.025 and result < 0.1 :
        skeleton_result = 'lessactive'
        print("less active한 상태입니다")   #어느정도 중간급 신나는 노래
    elif result < 0.025:
        skeleton_result = 'noactive'
        print("움직임이 거의 없습니다.")      # 발라드나 차분한 노래 
    elif result == 0:
        skeleton_result = 'noresult'
        print("사람이 없습니다")



    yolo_result=yolo.getYOLO(IMAGE_FILES)
    final_result = '분석'
        
        
    if skeleton_result =='active' and yolo_result == 'dumbbell':
        final_result = '운동' 
    elif skeleton_result == 'active' and yolo_result == 'cleaner':
        final_result = '청소'
    elif skeleton_result =='active' and yolo_result == 'noobject':
        final_result = '운동' 
    elif skeleton_result == 'lessactive' and yolo_result == 'noobject':
        final_result = '일'
    elif skeleton_result == 'lessactive' and yolo_result == 'cleaner':
        final_result = '청소'
    elif skeleton_result == 'lessactive' and yolo_result == 'openbook':
        final_result = '공부'
    elif skeleton_result == 'lessactive' and yolo_result == 'closedbook':
        final_result ='공부'
    elif skeleton_result == 'lessactive' and yolo_result == 'pen':
        final_result ='공부'
    elif skeleton_result =='lessactive' and yolo_result == 'monitor':
        final_result = '일'
    elif skeleton_result  =='lessactive' and yolo_result == 'keyboard':
        final_result = '일'
    elif skeleton_result =='lessactive'  and yolo_result == 'laptop':
        final_result = '일' 
    elif skeleton_result==  'noactive' and yolo_result == 'monitor':
        final_result = '일'
    elif skeleton_result  =='noactive' and yolo_result == 'keyboard':
        final_result = '일'
    elif skeleton_result== 'noactive'  and yolo_result == 'laptop':
        final_result = '일' 
 
    elif skeleton_result == 'noactive' and yolo_result =='noobject' :
        final_result = '휴식'
    elif skeleton_result == 'noactive' and yolo_result =='phone' :
        final_result = '휴식'
    elif skeleton_result == 'lessactive' and yolo_result =='phone' :
        final_result = '휴식'
        
    elif skeleton_result == 'noactive' and yolo_result == 'openbook':
        final_result = '공부'
    elif skeleton_result == 'noactive' and yolo_result == 'closedbook':
        final_result ='공부'
    elif skeleton_result == 'noactive' and yolo_result == 'pen':
        final_result ='공부'        
    elif skeleton_result == 'noresult':
        final_result = '분석'
    elif skeleton_result =='active' and yolo_result == 'noperson':
        final_result = '운동' 
    elif skeleton_result == 'lessactive' and yolo_result == 'noperson':
        final_result = '일'
    elif skeleton_result == 'noactive' and yolo_result =='noperson' :
        final_result = '휴식'



        
        
        
        
        
        
        
        
    print(final_result)



    return final_result



