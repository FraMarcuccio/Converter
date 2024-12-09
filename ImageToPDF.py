import os
from PIL import Image
from fpdf import FPDF
from PyPDF2 import PdfReader
from docx import Document
import img2pdf

class ImageToPDFConverter:
    @staticmethod
    def convert_images_to_single_pdf(image_folder, output_pdf_path):
        # Lista tutti i file immagine nella cartella
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
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
            # Dimensioni della pagina A4 in millimetri
            a4_width_mm = 210
            a4_height_mm = 297
            # Calcola le proporzioni per adattare l'immagine alla pagina A4
            width_mm = width * 0.264583
            height_mm = height * 0.264583

            if width_mm > a4_width_mm or height_mm > a4_height_mm:
                scale = min(a4_width_mm / width_mm, a4_height_mm / height_mm)
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

    @staticmethod
    def convert_each_image_to_pdf(image_folder, output_folder):
        # Lista tutti i file immagine nella cartella
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if not image_files:
            print("Nessun file immagine da convertire")
            return
        
        # Crea la cartella di output se non esiste
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            output_pdf_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + ".pdf")
            # Apri l'immagine e convertila in PDF usando img2pdf
            with open(output_pdf_path, "wb") as f:
                with Image.open(image_path) as img:
                    # Converte in PDF mantenendo la risoluzione
                    f.write(img2pdf.convert(image_path))
            print(f"Immagine {image_file} convertita in PDF salvato in {output_pdf_path}")

    @staticmethod
    def convert_each_image_to_pdf_sized(image_folder, output_folder):
        # Lista tutti i file immagine nella cartella        
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if not image_files:
            print("Nessun file immagine da convertire")
            return
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            output_pdf_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + ".pdf")
            image = Image.open(image_path)
            # Ottieni le dimensioni dell'immagine
            width_px, height_px = image.size
            # Conversione pixel -> mm (1 px = 0.264583 mm)
            width_mm = width_px * 0.264583
            height_mm = height_px * 0.264583

            # Crea un oggetto PDF con dimensioni personalizzate
            pdf = FPDF(unit="mm", format=(width_mm, height_mm))
            pdf.add_page()
            # Aggiungi l'immagine, occupando l'intera pagina senza margini
            pdf.image(image_path, x=0, y=0, w=width_mm, h=height_mm)
            pdf.output(output_pdf_path, "F")
            print(f"Immagine {image_file} convertita in PDF salvato in {output_pdf_path}")

    """
    def convert_image_to_pdf(self, image_folder, output_folder):
        # Lista tutti i file immagine nella cartella
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if not image_files:
            print("Nessun file immagine da convertire")
            return
        
        # Crea la cartella di output se non esiste
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            output_pdf_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + ".pdf")
            
            pdf = FPDF()
            pdf.add_page()
            image = Image.open(image_path)
            
            # Ottieni le dimensioni dell'immagine
            width, height = image.size
            
            # Dimensioni della pagina A4 in millimetri
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
            
            # Aggiungi l'immagine alla pagina centrata
            x = (a4_width_mm - width_mm) / 2
            y = (a4_height_mm - height_mm) / 2
            pdf.image(image_path, x, y, width_mm, height_mm)
            
            # Salva il PDF
            pdf.output(output_pdf_path, "F")
            print(f"Immagine {image_file} convertita in PDF salvato in {output_pdf_path}")
        """
