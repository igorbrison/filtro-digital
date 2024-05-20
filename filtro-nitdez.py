import cv2

imagem = cv2.imread("imagem.jpg")

kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

imagem_filtrada = cv2.filter2D(imagem, -1, kernel)

cv2.imshow("Imagem Filtrada", imagem_filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()
