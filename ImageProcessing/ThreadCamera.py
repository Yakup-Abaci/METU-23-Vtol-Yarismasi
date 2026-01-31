import threading
import cv2
import math


class ThreadCamera:
    def __init__(self, src=0, name="ColorDetection"):
        threading.Thread.__init__(self)

        self.old_konum = (1806, 899)  # kameradaki piksel karşılğı
        self.alan_konum = {'lat': 0, 'long': 0}  # alanın hesaplanan dünya konumu
        self.oran = 0.00001

        # initialize the video camera stream and read the first frame
        # from the stream
        self.cap = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.cap.read()

        # initialize the thread name
        self.name = name

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        t = threading.Thread(target=self.update, name=self.name, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.cap.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

    def goruntu_isleme(self):
        # alan görülür ise piksel koordinatları ve araın o anki konumu parametre verilerek konum_bul çağırılacak.
        # thread ile çağırılır ise parametre vere nasıl olcak.
        # alınan görüntü cv2.size ile 1920,1080 olarak büyütülecek.
        pass


    def konum_bul(self, bulunan_alan: tuple, arac_konum: dict):
        old_konum = (1806, 899)
        arac_pusula = self.vehicle.heading
        if bulunan_alan[0] < old_konum[0] and bulunan_alan[1] < old_konum[1]:
            # 1. alan
            yatay_aci = math.atan(math.tan(70) * (old_konum[1] - bulunan_alan[1]))
            dikey_aci = math.atan(math.tan(41) * (old_konum[0] - bulunan_alan[0]))
            yatay_uzaklik_gercek = math.tan(yatay_aci) * 20
            dikey_uzaklik_gercek = math.tan(dikey_aci) * 20
            aracagore_gercek_uzaklik_dikey = math.sqrt(math.pow(yatay_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                dikey_aci)
            aracagore_gercek_uzaklik_yatay = math.sqrt(math.pow(dikey_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                yatay_aci)

            aradaki_aci = 90 - abs(arac_pusula % 90)
            gercek_uzaklik_yatay = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_yatay
            gercek_uzaklik_dikey = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_dikey


        elif bulunan_alan[0] > old_konum[0] and bulunan_alan[1] < old_konum[1]:
            # 2. alan
            yatay_aci = math.atan(math.tan(10) * (old_konum[1] - bulunan_alan[1]))
            dikey_aci = math.atan(math.tan(41) * (old_konum[0] - bulunan_alan[0]))
            yatay_uzaklik_gercek = math.tan(yatay_aci) * 20
            dikey_uzaklik_gercek = math.tan(dikey_aci) * 20

            aracagore_gercek_uzaklik_dikey = math.sqrt(math.pow(yatay_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                dikey_aci)
            aracagore_gercek_uzaklik_yatay = math.sqrt(math.pow(dikey_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                yatay_aci) * (-1)

            aradaki_aci = 90 - abs(arac_pusula % 90)
            gercek_uzaklik_yatay = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_yatay
            gercek_uzaklik_dikey = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_dikey

        elif bulunan_alan[0] < old_konum[0] and bulunan_alan[1] > old_konum[1]:
            # 3. alan
            yatay_aci = math.atan(math.tan(70) * (old_konum[1] - bulunan_alan[1]))
            dikey_aci = math.atan(math.tan(10) * (old_konum[0] - bulunan_alan[0]))
            yatay_uzaklik_gercek = math.tan(yatay_aci) * 20
            dikey_uzaklik_gercek = math.tan(dikey_aci) * 20

            aracagore_gercek_uzaklik_dikey = math.sqrt(math.pow(yatay_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                dikey_aci) * (-1)
            aracagore_gercek_uzaklik_yatay = math.sqrt(math.pow(dikey_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                yatay_aci)
            aradaki_aci = 90 - abs(arac_pusula % 90)
            gercek_uzaklik_yatay = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_yatay
            gercek_uzaklik_dikey = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_dikey

        elif bulunan_alan[0] > old_konum[0] and bulunan_alan[1] > old_konum[1]:
            # 4. alan
            yatay_aci = math.atan(math.tan(10) * (old_konum[1] - bulunan_alan[1]))
            dikey_aci = math.atan(math.tan(10) * (old_konum[0] - bulunan_alan[0]))
            yatay_uzaklik_gercek = math.tan(yatay_aci) * 20
            dikey_uzaklik_gercek = math.tan(dikey_aci) * 20

            aracagore_gercek_uzaklik_dikey = math.sqrt(math.pow(yatay_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                dikey_aci) * (-1)
            aracagore_gercek_uzaklik_yatay = math.sqrt(math.pow(dikey_uzaklik_gercek, 2) + math.pow(20, 2)) * math.tan(
                yatay_aci) * (-1)

            aradaki_aci = 90 - abs(arac_pusula % 90)
            gercek_uzaklik_yatay = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_yatay
            gercek_uzaklik_dikey = math.cos(aradaki_aci) * aracagore_gercek_uzaklik_dikey

        if 90 < arac_pusula < 270:
            self.alan_konum['lat'] = arac_konum['lat'] + gercek_uzaklik_dikey * self.oran
            self.alan_konum['long'] = arac_konum['long'] + gercek_uzaklik_yatay * self.oran

        else:
            self.alan_konum['lat'] = arac_konum['lat'] - gercek_uzaklik_dikey * self.oran
            self.alan_konum['long'] = arac_konum['long'] - gercek_uzaklik_yatay * self.oran

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cap.release()
