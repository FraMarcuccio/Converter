import os
from PIL import Image
import pillow_heif  # Libreria per leggere file HEIC

class HEICToJPGConverter:
    def __init__(self):
        pillow_heif.register_heif_opener()

    @staticmethod
    def convert_heic_to_jpg(input_folder, output_folder):
        """
        Converte tutti i file HEIC in una cartella in formato JPG.

        Args:
            input_folder (str): Percorso della cartella con file HEIC.
            output_folder (str): Percorso della cartella dove salvare i file JPG.
        """
        # Controlla se la cartella di output esiste; altrimenti, creala
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Lista tutti i file HEIC nella cartella di input
        heic_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.heic')]

        if not heic_files:
            print("Nessun file HEIC trovato per la conversione.")
            return


        for heic_file in heic_files:
            input_path = os.path.join(input_folder, heic_file)
            output_path = os.path.join(output_folder, os.path.splitext(heic_file)[0] + ".jpg")

            try:
                # Apri il file HEIC e convertilo in JPG
                with Image.open(input_path) as img:
                    rgb_image = img.convert("RGB")  # Converti l'immagine in RGB
                    rgb_image.save(output_path, "JPEG", quality=95)  # Salva come JPG con alta qualità
                print(f"Convertito {heic_file} in {output_path}")
            except Exception as e:
                print(f"Errore durante la conversione di {heic_file}: {e}")
