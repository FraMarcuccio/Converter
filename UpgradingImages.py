import os
from PIL import Image
from realesrgan import RealESRGAN

def upscale_image_with_realesrgan(image_folder, output_folder):
    """
    Usa il modello Real-ESRGAN per migliorare la risoluzione di tutte le immagini in una cartella.

    :param image_folder: Path della cartella contenente le immagini di input
    :param output_folder: Path della cartella di output dove salvare le immagini migliorate
    """

    # Crea la cartella di output se non esiste
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista tutti i file immagine nella cartella
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print("Nessun file immagine da migliorare.")
        return

    # Inizializza il modello Real-ESRGAN
    model = RealESRGAN.from_pretrained('RealESRGAN_x4plus')  # Usa il modello pre-addestrato x4

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        output_image_path = os.path.join(output_folder, f"upscaled_{image_file}")

        try:
            # Apri l'immagine
            image = Image.open(image_path).convert('RGB')  # Converte in RGB se l'immagine non lo è
        except FileNotFoundError:
            print(f"L'immagine {image_file} non è stata trovata.")
            continue

        print(f"Miglioramento della qualità per: {image_file}")

        # Applica il modello di super-risoluzione
        sr_image = model.predict(image)
        
        # Salva l'immagine migliorata
        sr_image.save(output_image_path)
        print(f"Immagine migliorata salvata come: {output_image_path}")

    print("Processo completato per tutte le immagini.")

# Esempio di utilizzo
image_folder = "images"  # Cartella delle immagini di input
output_folder = "output_images"  # Cartella per le immagini migliorate
upscale_image_with_realesrgan(image_folder, output_folder)
