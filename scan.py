import os

def scan_directory(directory):
    virus_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Bu joyda siz o'zingizning virus identifikatsiya tizimini qo'llashingiz kerak
            # Bu namuna orqali emulyatsiya qilinmoqda
            is_infected = check_for_virus(file_path)

            if is_infected:
                print(f"Virus topildi: {file_path}")
                virus_count += 1

    return virus_count