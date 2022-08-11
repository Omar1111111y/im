import cv2 #استدعاء المكتبة
def omar(ms):
	PH1 = cv2.imread('basic.jpg')
	PH2 = cv2.imread('ba.jpg')
	if PH1.shape == PH2.shape :
		bot.reply_to(ms,'The image have same size and channels')
