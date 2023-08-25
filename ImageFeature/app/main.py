
from fastapi import FastAPI, Response
from pydantic import BaseModel
import base64

import cv2
import numpy as np

# สร้าง class เพื่อแปลงจาก json ข้อมูลมาเป็น object
class ImageClass(BaseModel):
    image_base64: str
def readb64(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)


    return img

app = FastAPI()

# api แบบ get ที่รอรับค่าต่างๆ เมื่อส่งผ่านมาทาง URL
@app.get("/api/{input_values}")
def read_values(input_values):
    return {"is to" : input_values}

@app.post("/api/gethog/")
async def read_image(image: ImageClass):
    img =  readb64(image.image_base64)

    print(img)

    # เปรี่ยนขนาดของรูปภาพ
    img = cv2.resize(img, (128, 128), cv2.INTER_AREA)
    win_size = img.shape
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    num_bins = 9

    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, num_bins)
    hog_descriptor = hog.compute(img)

    return {"HOG Length" : len(hog_descriptor),
            "HOG Descriptor" : hog_descriptor.tolist()
            }