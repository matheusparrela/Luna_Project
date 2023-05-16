from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, Image
from reportlab.lib import colors
import datetime
import CurvaEmpuxo as ce

class GerarPDF:
    def __init__(self, a, grafico, empuxo_table):

        self.empuxo_table = empuxo_table
        self.doc = SimpleDocTemplate("documento.pdf", pagesize=A4)
        self.styles = getSampleStyleSheet()
        self.conteudo = []
        self.cidade = 'Senador Carneiro'
        self.estado = 'KT'
        self.nome = "BT-8"
        self.img_grafico = "grafico.png"
        self.obs = "Nada a Declarar"
        self.centralizado = ParagraphStyle("estilo_centralizado",
                                            parent=self.styles["Normal"],
                                            alignment=1)  # 0=esquerda, 1=centralizado, 2=direita
        self.esquerda = ParagraphStyle("estilo_esquerda",
                                           parent=self.styles["Normal"],
                                           alignment=0)  # 0=esquerda, 1=centralizado, 2=direita
        self.negrito = ParagraphStyle("estilo_negrito",
                                      parent=self.styles["Normal"],
                                      fontName="Helvetica-Bold", alignment=0)  # Estilo de parágrafo em negrito

    def cabecalho(self):

        top = Paragraph("RELATÓRIO DE TESTE ESTÁTICO DE MOTOR DE MINIFOGUETE", self.centralizado)
        top1 = Paragraph(f"<b>NOME DO MOTOR:</b> {self.nome}", self.negrito)
        self.conteudo.append(top)
        self.conteudo.append(Spacer(1, 30))
        self.conteudo.append(top1)

        linha_horizontal = HRFlowable(width="100%", thickness=1, lineCap='round', spaceAfter=10)
        self.conteudo.append(linha_horizontal)

        data_atual = datetime.date.today()
        data_formatada = data_atual.strftime("%d/%m/%Y")
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

        # Parágrafo com linha na frente
        linha_vertical = f"LOCAL:   {self.cidade} - {self.estado}   " \
                         f"DATA:    {data_formatada}    " \
                         f"HORA:    {hora_atual}    "

        paragrafo_com_linha = Paragraph(linha_vertical, self.centralizado)
        self.conteudo.append(paragrafo_com_linha)

        self.conteudo.append(Spacer(1, 50))
        self.table()
        self.conteudo.append(Spacer(1, 50))

        self.grafico()
        self.conteudo.append(Spacer(1, 50))

        observacoes = Paragraph(f"OBSERVAÇÔES: {self.obs}", self.esquerda)
        self.conteudo.append(observacoes)

        # Construir o documento PDF
        self.doc.build(self.conteudo)

    def grafico(self):

        # Adicionar a imagem ao conteúdo do documento
        imagem = Image(self.img_grafico, width=350, height=300)
        self.conteudo.append(imagem)

    def table(self):

        # Dados da tabela
        dados = [["PROPRIEDADE", "VALOR", "UNIDADE"]]
        dados.extend(self.empuxo_table)

        '''
        Colocar os valores que foram encontrados em CurvaEmpuxo 
        '''
        # Define o estilo da tabela
        estilo_tabela = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),  # Cor de fundo da primeira linha
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Cor do texto da primeira linha
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do texto da primeira linha
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # Tamanho da fonte da primeira linha
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaçamento inferior da primeira linha
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Cor de fundo das demais linhas
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borda da tabela
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinhamento do texto
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Fonte do texto das demais linhas
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # Tamanho da fonte das demais linhas
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),  # Espaçamento inferior das demais linhas
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Cor de fundo do cabeçalho
        ])

        # Cria a tabela
        tabela = Table(dados)
        # Aplica o estilo à tabela
        tabela.setStyle(estilo_tabela)
        # Adiciona a tabela ao conteúdo do documento
        self.conteudo.append(tabela)
