from pypdf import PdfReader

def extractpdf(pdf_doc):
    pdf = PdfReader(pdf_doc) # index, page details
    
    raw_text = ''
    for index, page in enumerate(pdf.pages):
        raw_text +=page.extract_text()
        
    return raw_text