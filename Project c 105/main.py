import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

#reading first image from images array

frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
print(size)
#creating a file reference to save the video
out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
# for sunset
for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()
print("done") 