import fitz  # PyMuPDF library


if __name__ == "__main__":
    # Create a new PDF document
    pdf_document = fitz.open()

    # Add a new page to the document
    page = pdf_document.new_page()

    # Set the page text to "Hello, World!"
    page.insert_text((100, 100), "Hello, World!")

    # Save the document to the specified output filename
    output_filename = "hello_world.pdf"
    pdf_document.save(output_filename)

    # Close the document
    pdf_document.close()
