import matplotlib.pyplot as plt # plt 用於顯示圖片
import matplotlib.image as mpimg # mpimg 用於讀取圖片
import numpy as np
global eight
def eig(eight):
    lena = mpimg.imread('question_image/'+eight+'.png')
 # 讀取和程式碼處於同一目錄下的 lena.png
 # 此時 lena 就已經是一個 np.array 了，可以對它進行任意處理
    lena.shape #(512, 512, 3)
    plt.imshow(lena) # 顯示圖片
    plt.axis('off') # 不顯示座標軸
    plt.show()
