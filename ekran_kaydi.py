import cv2
import pyautogui
import numpy as np

ekran_boyutu = pyautogui.size() # Ekranın boyutu
video = cv2.VideoWriter('Ekran Kaydı.avi', cv2.VideoWriter_fourcc(*'MJPG'), 18, ekran_boyutu) # Kayıtın yazılacağı objeler, ayarlar

print("Kayıt başladı!")

while True:
    ekran_kaydı_img = pyautogui.screenshot()
    cerceve = np.array(ekran_kaydı_img)

    cerceve = cv2.cvtColor(cerceve, cv2.COLOR_BGR2RGB) # BGR renk uzayından RGB renk uzayına geçiş yapılıyor.
    video.write(cerceve) # Kareleri yazdırma işlemi

    cv2.imshow("Kayıt Ekranı", cerceve) # Çıktıyı görme imkanı sağlanıyor.
    if cv2.waitKey(1) == ord("q"): # Kodu durdurmak için "q" tuşuna basılmalıdır aksi takdirde kod sürekli çalışmaya devam edecetir.
        break

cv2.destroyAllWindows
video.relase()

