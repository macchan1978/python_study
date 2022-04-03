import cv2

img = cv2.imread("images/cat_image.jpeg", 1)   #Color is BGR not RGB
print(img.shape)     #(586, 415, 3)
#edges =cv2.Canny(img,100,200)
#resize = cv2.resize(img, dsize=None, fx=0.1, fy=0.1)

pyrNum = 4

for level in range(pyrNum):
    img = cv2.pyrDown(img)
    cv2.imshow("cat pic resized %d"%level, img)
    cv2.waitKey(0)          
    cv2.destroyAllWindows() 


for level in range(pyrNum):
    img = cv2.pyrUp(img)
    cv2.imshow("cat pic resized %d"%level, img)
    cv2.waitKey(0)          
    cv2.destroyAllWindows() 



cv2.destroyAllWindows() 
