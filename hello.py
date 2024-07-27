import os
import shutil
import fitz

source_folder = "/home/dungne/Downloads"
file_extensions = {
    "pdf": "PDF_Files",
    "txt": "Text_Files",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "doc": "Documents",
    "docx": "Documents",
    
    "odt": "Documents",
    "xls": "Spreadsheets",
    "xlsx": "Spreadsheets",
    "csv": "Spreadsheets",
    "ppt": "Presentations",
    "pptx": "Presentations",
    "html": "Web_Files",
    "css": "Web_Files",
    "js": "Web_Files",
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "mp4": "Videos",
    "avi": "Videos",
    "mov": "Videos",
    "mkv": "Videos",
    "mp3": "Audio",
    "wav": "Audio",
    "ogg": "Audio",
    "flac": "Audio",
    "xml": "XML_Files",
    "drawio": "Diagrams",
    "pem": "Certificates",
    "rst": "Documentation",
    "vtt": "Subtitles",
    "pt": "Models",
    # Thêm các định dạng file khác tại đây
}


def is_pdf(file_path):  # kiemtrapdf
    try:
        doc = fitz.open(file_path)
        doc.close()
        return True
    except:
        return False


def organize_files_by_extension(src_folder, ext_dict):
    for item in os.listdir(src_folder):
        item_path = os.path.join(src_folder, item)

        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()[1:]
            if not ext:

                if is_pdf(item_path):
                    ext = "pdf"

            if ext in ext_dict:
                target_folder = os.path.join(src_folder, ext_dict[ext])
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(item_path, os.path.join(target_folder, item))
            else:
                print(f"Không có thư mục định dạng cho {item}")


if __name__ == "__main__":
    organize_files_by_extension(source_folder, file_extensions)
