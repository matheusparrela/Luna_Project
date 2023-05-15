from reportlab.pdfgen import canvas

class GerarPDF:

    def __init__(self, a):
        self.a = a

    def file_pdf(self):
        c = canvas.Canvas("report.pdf")
        c.drawString(100, 750, "Hello World!")
        c.save()
