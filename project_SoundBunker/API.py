#!/usr/bin/env python
# coding: utf-8

# In[14]:


# !pip install flask


# In[13]:


# !pip install flask_cors
get_ipython().system('pip install -U flask-cors')


# In[7]:


# !pip install torch
# !pip install torchvision
# !pip install pandas
#!pip3 install Flask-Cors
# !pip install --user Flask-Cors


# In[5]:


# !pip install --user seaborn


# In[4]:


get_ipython().system('pip install requests')


# In[6]:


import requests # pip install requests

res = requests.get("https://api.github.com/users/octocat",
    allow_redirects=True, auth=(<seoyyy>,<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>))
res.raise_for_status()
data = res.json()

print(data)


# In[ ]:





# # 최종연결코드

# In[ ]:


import skeleton_final
import yolo_final
import os
import json
from flask import Flask,render_template, request,jsonify, redirect, url_for
from flask_cors import CORS
import base64
from PIL import Image
import io
import matplotlib.pyplot as plt
import cv2
import numpy as np
import final_main

# Take in base64 string and return cv imageㅁ
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return opencv_img

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/post', methods=['GET','POST'])
def getimage():
    
    data = dict(request.form)

    jsonArray = json.loads(data['json'])
    print(jsonArray[0]['name'])
    
    IMAGE_FILES=[]
    
    # base64 이미지 코드
    for jsonObject in jsonArray:
        base = jsonObject['img'].split(",")[1]

        imArr = stringToRGB(base)

        IMAGE_FILES.append(imArr)
        
    
#     i = cv2.imread(IMAGE_FILES[0])
    
#     print(i.shape)
    
    getstatement = final_main.getstatement(IMAGE_FILES)
#     while True:
#         if img != None:
#             IMAGE_FILES.append(img)
            
#             if len(IMAGE_FILES)%2 ==0:    
#                 getstatment = final_main.getstatement(IMAGE_FILES)
#                 IMAGE_FILES=[]
    print(getstatement)    
    return getstatement
    
    # json 
    #return redirect(url_for('http://localhost:13743/web/post'),res = getstatement) 

if __name__=="__main__":
    app.run()


# # ------------최종코드 끝

# In[1]:


from flask import Flask #간단히 플라스크 서버를 만든다

import urllib.request

app = Flask(__name__)

@app.route("/tospring")
def spring():
    
    return "getstatement"
    
    
if __name__ == '__main__':
    app.run(debug=False,host="127.0.0.1",port=5000)


# In[ ]:





# In[ ]:



import skeleton_final
import yolo_final
import os
import json
from flask import Flask,render_template, request,jsonify
from flask_cors import CORS
import base64
from PIL import Image
import io
import matplotlib.pyplot as plt
import cv2
import numpy as np
import final_main

import urllib.request

# Take in base64 string and return cv imageㅁ
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return opencv_img

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/post', methods=['GET','POST'])
def getimage():
    
    data = dict(request.form)

    
    jsonArray = json.loads(data['json'])
    print(jsonArray[0]['name'])
    
    IMAGE_FILES=[]
    
    # base64 이미지 코드
    for jsonObject in jsonArray:
        base = jsonObject['img'].split(",")[1]

        imArr = stringToRGB(base)

        IMAGE_FILES.append(imArr)
        
    
#     i = cv2.imread(IMAGE_FILES[0])
    
#     print(i.shape)
    
    getstatement = final_main.getstatement(IMAGE_FILES)
#     while True:
#         if img != None:
#             IMAGE_FILES.append(img)
            
#             if len(IMAGE_FILES)%2 ==0:    
#                 getstatment = final_main.getstatement(IMAGE_FILES)
#                 IMAGE_FILES=[]
        
    print(getstatement)
    
    # json 
    return getstatement

# @app.route("/tospring")
# def spring():
    
#     print(getstatement)
#     return getstatement
    

if __name__=="__main__":
    app.run()


# In[ ]:





# In[1]:


import skeleton_final
import yolo_final
import os
import json
from flask import Flask,render_template, request,jsonify
from flask_cors import CORS
import base64
from PIL import Image
import io
import matplotlib.pyplot as plt
import cv2
import numpy as np
import final_main

# Take in base64 string and return cv imageㅁ
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return opencv_img

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/post', methods=['GET','POST'])
def getimage():
    
    data = dict(request.form)

    jsonArray = json.loads(data['json'])
    print(jsonArray[0]['name'])
    
    IMAGE_FILES=[]
    
    # base64 이미지 코드
    for jsonObject in jsonArray:
        base = jsonObject['img'].split(",")[1]

        imArr = stringToRGB(base)

        IMAGE_FILES.append(imArr)
        
    
#     i = cv2.imread(IMAGE_FILES[0])
    
#     print(i.shape)
    
    getstatment = final_main.getstatement(IMAGE_FILES)
#     while True:
#         if img != None:
#             IMAGE_FILES.append(img)
            
#             if len(IMAGE_FILES)%2 ==0:    
#                 getstatment = final_main.getstatement(IMAGE_FILES)
#                 IMAGE_FILES=[]
        
#     print(getstatement)
    
    # json 
    return getstatement

    
    
#if __name__ == '__main__':
#    app.run(debug=False,host="127.0.0.1",port=5000)

if __name__=="__main__":
    app.run()


# In[ ]:


import skeleton_final
import yolo_final
import os
import json
from flask import Flask,render_template, request,jsonify, redirect, url_for
from flask_cors import CORS
import base64
from PIL import Image
import io
import matplotlib.pyplot as plt
import cv2
import numpy as np
import final_main

# # Take in base64 string and return cv imageㅁ
# def stringToRGB(base64_string):
#     imgdata = base64.b64decode(str(base64_string))
#     img = Image.open(io.BytesIO(imgdata))
#     opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
#     return opencv_img

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/post', methods=['GET','POST'])
def getimage():
    
#     data = dict(request.form)

#     jsonArray = json.loads(data['json'])
#     print(jsonArray[0]['name'])
    
#     IMAGE_FILES=[]
    
#     # base64 이미지 코드
#     for jsonObject in jsonArray:
#         base = jsonObject['img'].split(",")[1]

#         imArr = stringToRGB(base)

#         IMAGE_FILES.append(imArr)
        
    
# #     i = cv2.imread(IMAGE_FILES[0])
    
# #     print(i.shape)
    
#     getstatement = final_main.getstatement(IMAGE_FILES)
# #     while True:
# #         if img != None:
# #             IMAGE_FILES.append(img)
            
# #             if len(IMAGE_FILES)%2 ==0:    
# #                 getstatment = final_main.getstatement(IMAGE_FILES)
# #                 IMAGE_FILES=[]
    test_data = 'HIHISY!!'
    print(test_data)    
    return test_data
    
    # json 
    #return redirect(url_for('http://localhost:13743/web/post'),res = getstatement) 

if __name__=="__main__":


# In[3]:


import skeleton_final
import yolo_final
import os
import json
from flask import Flask,render_template, request,jsonify, redirect, url_for
from flask_cors import CORS
import base64
from PIL import Image
import io
import matplotlib.pyplot as plt
import cv2
import numpy as np
import final_main    

IMAGE_FILES =['studying90.jpg','studying81.jpg','studying73.jpg']
getstatment = final_main.getstatement(IMAGE_FILES)

print(getstatement)


# In[ ]:




