import os
from ImageToPDF import ImageToPDFConverter 
from PDFToWord import PDFToWordConverter
from ImageToImage import HEICToJPGConverter

def main():
    input_folderImage = "images_input"
    merged_output_pdf_path = os.path.join(input_folderImage, "merged_output.pdf")
    output_folderPDF = "pdfs_output"
    input_folderPDF = "pdfs_input"
    output_folderWord = "words_output"
    input_folderHEIC = "heic_images_input"  # Cartella con file HEIC
    output_folderJPG = "jpg_images_output"  # Cartella per i file JPG convertiti


    # Converti tutte le immagini in un unico PDF
    ImageToPDFConverter.convert_images_to_single_pdf(input_folderImage, merged_output_pdf_path)

    # Converti ogni immagine in un PDF separato
    ImageToPDFConverter.convert_each_image_to_pdf(input_folderImage, output_folderPDF)

    # Converti ogni immagine in un PDF separato con dimensioni personalizzate
    ImageToPDFConverter.convert_each_image_to_pdf_sized(input_folderImage, output_folderPDF)

    # Converti i PDF in documenti Word
    PDFToWordConverter.convert_pdfs_to_word(input_folderPDF, output_folderWord)

    # Creazione di un'istanza e conversione dei file
    converter = HEICToJPGConverter()
    converter.convert_heic_to_jpg(input_folderHEIC, output_folderJPG)

if __name__ == "__main__":
    main()
