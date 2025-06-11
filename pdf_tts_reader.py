# pdf_tts_reader.py
try:
    import pyttsx3
    from PyPDF2 import PdfReader
    from tkinter.filedialog import askopenfilename
    import tkinter as tk

    # Hide main tkinter window
    tk.Tk().withdraw()

    # Open file browser to select a PDF
    book = askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])

    if not book:
        raise FileNotFoundError("No file was selected.")

    # Read PDF
    pdf_reader = PdfReader(book)

    if pdf_reader.is_encrypted:
        raise ValueError("PDF is encrypted and cannot be read.")

    pages = len(pdf_reader.pages)

    # Initialize TTS engine
    player = pyttsx3.init()

    # Read and speak each page
    for num in range(pages):
        page = pdf_reader.pages[num]
        text = page.extract_text()
        if text:
            player.say(text)
            player.runAndWait()
        else:
            print(f"Page {num + 1} has no readable text.")

    # Stop the engine
    player.stop()

except Exception as e:
    print(f"Error: {e}\nPDF file not selected properly or it's encrypted.")
else:
    print("Program run successfully.")
