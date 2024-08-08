import cv2
import numpy as np

# HSV renklerini ayarlamak için trackbar fonksiyonunu kullanıyoruz.
def update_image(x=None):
    # HSV değerlerini trackbarlardan alma işlemi
    h = cv2.getTrackbarPos('Hue', 'Adjustments')
    s = cv2.getTrackbarPos('Saturation', 'Adjustments')
    v = cv2.getTrackbarPos('Value', 'Adjustments')
    
    # HSV değerlerini güncellemek için kullanıyoruz.
    hsv_adjusted = hsv_image.copy()
    hsv_adjusted[:, :, 0] = np.clip(hsv_adjusted[:, :, 0] + h - 50, 0, 179)  # Hue ayarı
    hsv_adjusted[:, :, 1] = np.clip(hsv_adjusted[:, :, 1] + s - 50, 0, 255)  # Saturation ayarı
    hsv_adjusted[:, :, 2] = np.clip(hsv_adjusted[:, :, 2] + v - 50, 0, 255)  # Value ayarı

    result_adjusted = cv2.cvtColor(hsv_adjusted, cv2.COLOR_HSV2BGR)
    
    # Güncellenmiş görüntüyü göstermek için.
    cv2.imshow('Adjusted Image', result_adjusted)



image = cv2.imread('result_image.jpg')


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Başlangıç görüntüsünü göstermek için oluşturulan pencere
cv2.imshow('Adjusted Image', image)

# Ayar penceresini oluştur
cv2.namedWindow('Adjustments')

# Trackbar'ları oluştur
cv2.createTrackbar('Hue', 'Adjustments', 50, 100, lambda x: None)
cv2.createTrackbar('Saturation', 'Adjustments', 50, 100, lambda x: None)
cv2.createTrackbar('Value', 'Adjustments', 50, 100, lambda x: None)

# Trackbar hareketlerini güncellemek için bir döngü
while True:
    
    update_image()

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # HSV değerlerini trackbarlardan alma  işlemi
        h = cv2.getTrackbarPos('Hue', 'Adjustments')
        s = cv2.getTrackbarPos('Saturation', 'Adjustments')
        v = cv2.getTrackbarPos('Value', 'Adjustments')

        # HSV değerlerini güncellemek için
        hsv_adjusted = hsv_image.copy()
        hsv_adjusted[:, :, 0] = np.clip(hsv_adjusted[:, :, 0] + h - 50, 0, 179)  # Hue ayarı
        hsv_adjusted[:, :, 1] = np.clip(hsv_adjusted[:, :, 1] + s - 50, 0, 255)  # Saturation ayarı
        hsv_adjusted[:, :, 2] = np.clip(hsv_adjusted[:, :, 2] + v - 50, 0, 255)  # Value ayarı

     
        result_adjusted = cv2.cvtColor(hsv_adjusted, cv2.COLOR_HSV2BGR)
        
        save_filename = 'mor_gul.jpg'
        cv2.imwrite(save_filename, result_adjusted)
        print(f"Image saved as {save_filename}")

    elif key == 27:  #Esc basarak çıkıyoruz.
        break

cv2.destroyAllWindows()
