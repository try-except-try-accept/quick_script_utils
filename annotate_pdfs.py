from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from os import listdir, path, mkdir, getcwd

header = io.BytesIO()

# create a new PDF with Reportlab
can = canvas.Canvas(header, pagesize=letter)
can.setFillColorRGB(1, 0, 0)
can.drawString(80, 1140, "Instructions: check the grades on this document against your original data and sign end at the end to confirm they are correct.")
can.save()

#move to the beginning of the StringIO buffer
header.seek(0)
new_header_pdf = PdfFileReader(header)


tail = io.BytesIO()

can2 = canvas.Canvas(tail, pagesize=letter)
can2.setFillColorRGB(1, 0, 0)
can2.drawString(50, 700, "I confirm that all grades have been reviewed and quality checked to ensure their accuracy.")
can2.drawString(50, 660, "SIGNED: ")
can2.drawString(50, 640, "DATE: ")
can2.drawString(50, 620, "POSITION: ")
can2.save()

#move to the beginning of the StringIO buffer
tail.seek(0)
new_footer_pdf = PdfFileReader(tail)


for folder in listdir():
     if not path.isdir(getcwd()+"/"+folder) or folder=="final":
          continue

     if not path.isdir(getcwd()+"/"+"final/"+ folder):
          mkdir("final/"+folder)

     for fn in listdir(folder):

          new_fn = fn.replace("AQA Centre Services", "Final Sign-Off").replace("Cambridge Assessment International Education _ Grade Submission System", "Final Sign-Off").replace("TAG Portal - Learner Grades", "Final Sign-Off")
          if path.exists(getcwd()+"/"+"final/"+folder+"/"+new_fn):
               continue
          
          existing_pdf = PdfFileReader(open(getcwd()+"/"+folder+"/"+fn, "rb"))
          output = PdfFileWriter()
          page = existing_pdf.getPage(0)
          page.mergePage(new_header_pdf.getPage(0))
          
          pages = existing_pdf.getNumPages()

          output.addPage(page)

          for i in range(1, pages):
               output.addPage(existing_pdf.getPage(i))

          
          page = new_footer_pdf.getPage(0)
          output.addPage(page)
         
          outputStream = open(getcwd()+"/"+"final/"+folder+"/"+new_fn, "wb")
          print("Annotated", new_fn)
          output.write(outputStream)
          outputStream.close()

