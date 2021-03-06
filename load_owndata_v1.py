import os
import cv2
import numpy as np



def load_own_data(label):

    root_path = './emb_data/'+str(label)
    img_folder = './emb_data/'+str(label)+'/fp0'
    print(len(os.listdir(img_folder)))
    total_img=[]
    for num_img in range(len(os.listdir(img_folder))):
        image_array = []


        for i in range(7):
            fn = 'fp'+str(i)
            fd_path = os.path.join(root_path,fn)
            # print(fn)
            # print(sorted(os.listdir(fd_path))[num_img])
            filename_path = os.path.join(fd_path,sorted(os.listdir(fd_path))[num_img])
            image = cv2.imread(filename_path)
            image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            # print(np.array(image).shape) 
            # cv2.imshow('test',image)
            image = np.array(image,np.float32)
            image = np.expand_dims(image, axis=2)
            if i ==0:
                image_array=image
            else:
                image_array=np.concatenate([image_array,image], axis=2)
            # print(image_array.shape)

            # if cv2.waitKey(0) & 0xFF==ord('q'):
            #     break
        
        if num_img==0:
            image_array = np.expand_dims(image_array, axis=0)
            total_img=  image_array
        else:
            image_array = np.expand_dims(image_array, axis=0)
            total_img=np.concatenate([total_img,image_array], axis=0)
        # print(total_img.shape)

            # cv2.waitKey(0)
            # for filename in sorted(os.listdir(fd_path)):
            #     print(fn)
            #     filename_path = os.path.join(fd_path,filename)
            #     print(filename_path[0])

    return total_img



