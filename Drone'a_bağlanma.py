import tellopy
import time

def connect_to_tello():
    # Tello cihazına bağlan
    drone = tellopy.Tello()
    try:
        print("Bağlantı kuruluyor...")
        drone.connect()
        print("Bağlantı başarılı!")
        
        # Drone'u başlat
        drone.takeoff()
        time.sleep(5)  # 5 saniye havada bekleyin
        
        # Drone'u sağa hareket ettir
        print("Sağa hareket ediyor...")
        drone.go_right(30)  # 30 cm sağa hareket
        time.sleep(2)
        
        # Drone'u sola hareket ettir
        print("Sola hareket ediyor...")
        drone.go_left(30)  # 30 cm sola hareket
        time.sleep(2)
        
        # Drone'u ileri hareket ettir
        print("İleri hareket ediyor...")
        drone.go_forward(30)  # 30 cm ileri hareket
        time.sleep(2)
        
        # Drone'u geri hareket ettir
        print("Geri hareket ediyor...")
        drone.go_back(30)  # 30 cm geri hareket
        time.sleep(2)
        
        # Drone'u indirin
        print("İniş yapılıyor...")
        drone.land()
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        # Drone bağlantısını sonlandır
        drone.quit()

if __name__ == "__main__":
    connect_to_tello()
