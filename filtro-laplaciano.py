import cv2

imagem = cv2.imread("imagem.jpg")

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

imagem_bordas = cv2.Laplacian(imagem_cinza, cv2.CV_64F)

imagem_bordas = cv2.convertScaleAbs(imagem_bordas)

cv2.imshow("Imagem com Bordas Realçadas", imagem_bordas)
cv2.waitKey(0)
cv2.destroyAllWindows()
```