from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from app.models.analysis import Analysis


class ReportService:
    def build_pdf(self, analysis: Analysis) -> bytes:
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        y = height - 50

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(50, y, "DevFlow AI - Relatório de Análise")
        y -= 40

        pdf.setFont("Helvetica", 11)
        pdf.drawString(50, y, f"Projeto: {analysis.project_name}")
        y -= 20
        pdf.drawString(50, y, f"Score: {analysis.score}/100")
        y -= 30

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Resumo")
        y -= 20
        pdf.setFont("Helvetica", 10)
        for line in self._wrap(analysis.summary, 95):
            pdf.drawString(50, y, line)
            y -= 14

        y -= 18
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Principais achados")
        y -= 20
        pdf.setFont("Helvetica", 9)

        for finding in analysis.findings[:25]:
            if y < 70:
                pdf.showPage()
                y = height - 50
                pdf.setFont("Helvetica", 9)
            text = f"[{finding['severity'].upper()}] {finding['category']} - {finding.get('file') or 'Projeto'}: {finding['message']}"
            for line in self._wrap(text, 105):
                pdf.drawString(50, y, line)
                y -= 13
            y -= 5

        pdf.save()
        buffer.seek(0)
        return buffer.read()

    def _wrap(self, text: str, width: int) -> list[str]:
        words = text.split()
        lines = []
        current = ""
        for word in words:
            if len(current) + len(word) + 1 > width:
                lines.append(current)
                current = word
            else:
                current = f"{current} {word}".strip()
        if current:
            lines.append(current)
        return lines
