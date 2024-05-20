import cv2

imagem = cv2.imread("imagem.jpg")

imagem_suavizada = cv2.blur(imagem, (5, 5))

cv2.imshow("Imagem Suavizada", imagem_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
