import os
from PIL import Image
from fpdf import FPDF

def convert_images_to_pdf(image_folder, output_pdf_path):
    # Lista tutti i file jpg nella cartella
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.jpg')]
    
    if not image_files:
        print("Nessun file immagine da convertire")
        return
    
    # Crea un oggetto FPDF
    pdf = FPDF()
    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        
        # Ottieni le dimensioni dell'immagine
        width, height = image.size
        
        # Dimensioni della pagina A4 in punti (1 punto = 1/72 pollice)
        a4_width_mm = 210
        a4_height_mm = 297
        
        # Calcola le proporzioni per adattare l'immagine alla pagina A4
        width_mm = width * 0.264583
        height_mm = height * 0.264583
        
        if width_mm > a4_width_mm or height_mm > a4_height_mm:
            if width_mm / a4_width_mm > height_mm / a4_height_mm:
                scale = a4_width_mm / width_mm
            else:
                scale = a4_height_mm / height_mm
            width_mm *= scale
            height_mm *= scale
        
        # Aggiungi una pagina al PDF
        pdf.add_page()
        
        # Aggiungi l'immagine alla pagina centrata
        x = (a4_width_mm - width_mm) / 2
        y = (a4_height_mm - height_mm) / 2
        pdf.image(image_path, x, y, width_mm, height_mm)
    
    # Salva il PDF
    pdf.output(output_pdf_path, "F")
    print(f"Conversione completata! PDF salvato in {output_pdf_path}")

# Percorso della cartella contenente le immagini
image_folder = "images"
# Nome del file PDF di output
output_pdf_path = os.path.join(image_folder, "output.pdf")

# Converti le immagini in PDF
convert_images_to_pdf(image_folder, output_pdf_path)
