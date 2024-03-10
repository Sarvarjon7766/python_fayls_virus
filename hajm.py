import os
def scan_directory(directory):
    virus_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            
            is_infected = check_for_virus(file_path)

            if is_infected:
                print(f"Virus topildi: {file_path}")
                virus_count += 1

    return virus_count

def word_file_size(file_path):
    try:
       
        size_in_bytes=os.path.getsize(file_path)

        
        size_in_mb=size_in_bytes/(1024)
        
        return size_in_mb
    except FileNotFoundError:
        return "Fayl topilmadi"
    except Exception as e:
        return f"Xatolik yuz berdi:{e}"

file_path="sarvar.docx" 
result=word_file_size(file_path)
print(f"Fayl hajmi:r{result}KB")   

def check_for_virus(file_path):
   
    if "virus" in file_path.lower():
        return True

    return False