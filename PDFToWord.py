import os
from PIL import Image
from fpdf import FPDF
from PyPDF2 import PdfReader
from docx import Document
import re
import img2pdf

class PDFToWordConverter:
    @staticmethod
    def convert_pdfs_to_word(pdf_folder, output_folder):
        if not os.path.exists(pdf_folder):
            print("Cartella PDF non trovata.")
            return
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]
        if not pdf_files:
            print("Nessun file PDF da convertire")
            return
        
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            output_word_path = os.path.join(output_folder, os.path.splitext(pdf_file)[0] + ".docx")
            try:
                # Leggi il PDF
                pdf_reader = PdfReader(pdf_path)
                document = Document()
                # Estrai testo da ogni pagina e aggiungilo al documento Word
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text: # Controlla che ci sia del testo estratto
                        clean_text = PDFToWordConverter.clean_text(text)
                        document.add_paragraph(clean_text)
                document.save(output_word_path)
                print(f"Conversione del PDF {pdf_file} completata! Documento Word salvato in {output_word_path}")
            except Exception as e:
                print(f"Errore durante la conversione del PDF {pdf_file}: {e}")

    @staticmethod
    def clean_text(text):
        # Rimuove caratteri non validi per XML
        return re.sub(r'[^\x09\x0A\x0D\x20-\x7E\xA0-\xFF]', '', text)
