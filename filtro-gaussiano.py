import cv2

imagem = cv2.imread("imagem.jpg")

imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)

cv2.imshow("Imagem Suavizada", imagem_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
