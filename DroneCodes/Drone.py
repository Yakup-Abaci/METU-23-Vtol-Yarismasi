import dronekit
from pymavlink import mavutil
import time
import math
import sys
import RPi.GPIO as GPIO
import time


class Drone:
    def __init__(self, ip, baud, wait_ready):
        self.baglan(ip, baud, wait_ready)

    def baglan(self, ip: str, baud: int, wait_ready: bool):
        try:
            self.vehicle = dronekit.connect(ip=ip, baud=baud, wait_ready=wait_ready)
            print("Bağlantı yapıldı")
        except:
            print("bağlantı yapılamadı")
            sys.exit()

    def mode(self, mode: str):
        self.vehicle.mode = dronekit.VehicleMode(mode)
        while mode != self.vehicle.mode:
            print("{} moduna geçiliyor".format(mode))
            time.sleep(1)
        print("{} moduna geçildi".format(str(self.vehicle.mode)))

    def arm_disarm(self, arm: bool):
        self.vehicle.armed = arm
        if arm == True:
            while not self.vehicle.is_armable:
                print("arm ediliyor")
                time.sleep(1)
            print("arm edildi")
        else:
            while self.vehicle.armed:
                time.sleep(1)
            print("disarm edildi")

    def takeoff(self, alt: int):
        self.vehicle.simple_takeoff(alt=alt)
        while 1:
            if self.vehicle.location.global_relative_frame.alt == alt * 0.90:
                print("Yüksekliğe ulaşıldı")
            else:
                print("Tırmanılıyor. alt=", self.vehicle.location.global_relative_frame.alt)

    def readmission(self, file):
        print("Reading mission from file: %s\n" % file)
        missionlist = []
        # open(file) bunun adını f yaptık
        with open(file) as f:
            # enumerate numaralandırma her satırı index numarasıyla i değişkenine atar
            for i, line in enumerate(f):
                if i == 0:
                    # i 0sa dosya doğrulama sistemi gibi raise da sana konsolda hata almanı sağlıyor
                    if not line.startswith('QGC WPL 110'):
                        raise Exception('File is not supported WP version')
                else:
                    linearray = line.split('\t')
                    ln_index = int(linearray[0])
                    ln_currentwp = int(linearray[1])
                    ln_frame = int(linearray[2])
                    ln_command = int(linearray[3])
                    ln_param1 = float(linearray[4])
                    ln_param2 = float(linearray[5])
                    ln_param3 = float(linearray[6])
                    ln_param4 = float(linearray[7])
                    ln_param5 = float(linearray[8])
                    ln_param6 = float(linearray[9])
                    ln_param7 = float(linearray[10])
                    ln_autocontinue = int(linearray[11].strip())
                    cmd = dronekit.Command(0, 0, 0, ln_frame, ln_command, ln_currentwp, ln_autocontinue, ln_param1,
                                           ln_param2,
                                           ln_param3, ln_param4, ln_param5, ln_param6, ln_param7)
                    missionlist.append(cmd)
        return missionlist

    def upload_mission(self, file):
        missionlist = self.readmission(file)
        cmds = self.vehicle.commands
        cmds.clear()
        for command in missionlist:
            cmds.add(command)
        print(' Upload mission')
        self.vehicle.commands.upload()
        print("görev yüklendi")
        return 0
        # Add new mission to vehicle

    def ortala(self):
        pass


    def sise_birak(self):
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)

        pwm = GPIO.PWM(servoPIN, 50)
        pwm.start(0)

        def aciAyarla(aci):
            x = (1 / 180) * aci + 1
            duty = x * 5
            pwm.ChangeDutyCycle(duty)

        try:
            while True:

                for i in range(0, 181, 45):
                    print("aci = ", i)
                    aciAyarla(i)
                    time.sleep(1)

        except KeyboardInterrupt:
            pwm.stop()
            GPIO.cleanup()

        self.eve_don()
        pass

    def eve_don(self):
        msg = self.vehicle.message_factory.command_long_encode(0, 0, 0,
                                                               mavutil.mavlink.MAV_CMD_CONDITION_CHANGE_ALT,
                                                               0,
                                                               0, 0, 0, 0, 0, 0,
                                                               20)
        self.vehicle.send_mavlink(msg)
        while True:
            if self.vehicle.location.global_relative_frame.alt == 20 * 0.95:
                break

        self.vehicle.simple_goto(self.vehicle.home_location)
        # ev konumuna varma kontrol et.

    def alcal(self):
        yeni_yukseklik = self.vehicle.location.global_relative_frame.alt - 1
        if self.vehicle.location.global_relative_frame.alt != 1:
            msg = self.vehicle.message_factory.command_long_encode(0, 0, 0,
                                                                   mavutil.mavlink.MAV_CMD_CONDITION_CHANGE_ALT,
                                                                   0,
                                                                   0, 0, 0, 0, 0, 0,
                                                                   yeni_yukseklik)
            self.vehicle.send_mavlink(msg)
            while True:
                if self.vehicle.location.global_relative_frame.alt == yeni_yukseklik:
                    break
            self.ortala()
        else:
            self.sise_birak()

    def gorev_kontrol(self):
        tur_sayisi = 0
        while True:
            if tur_sayisi < 5 and self.vehicle.commands.next == 3:
                tur_sayisi += 1
                print("{}. tur başladı".format(tur_sayisi))
                time.sleep(10)
            if tur_sayisi < 5 and self.vehicle.commands.next == 12:
                print("aaaa")
                self.vehicle.commands.next = 2
                time.sleep(2)
            if tur_sayisi == 5 and self.vehicle.commands.next == 12:
                time.sleep(6)
                print("hedefe gidiyorum")
                self.mode("QLOITER")
                time.sleep(1)
                self.mode("GUIDED")
                time.sleep(1)
                print(str(self.vehicle.mode))
                a_location = dronekit.LocationGlobalRelative(self.alan_konum['lat'], self.alan_konum['long'], 20)
                self.vehicle.simple_goto(a_location)
                break


