from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import pagesizes
from io import BytesIO


def generate_pdf(user_data, bmi, calories, plan_text):
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=pagesizes.A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=20
    )

    title_style = ParagraphStyle(
        name="Title",
        fontSize=18,
        leading=22,
        spaceAfter=20,
        alignment=TA_CENTER,
        bold=True
    )

    header_style = ParagraphStyle(
        name="Header",
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=6,
        bold=True
    )

    normal_style = ParagraphStyle(
        name="Normal",
        fontSize=11,
        leading=16
    )

    elements = []

    elements.append(Paragraph("<b>Personalized Workout & Diet Plan</b>", title_style))

    user_table_data = [
        ["Age", user_data["age"]],
        ["Gender", user_data["gender"]],
        ["Height (cm)", user_data["height"]],
        ["Weight (kg)", user_data["weight"]],
        ["Goal", user_data["goal"]],
        ["BMI", bmi],
        ["Estimated Calories", f"{calories} kcal/day"],
    ]

    table = Table(user_table_data, colWidths=[150, 300])
    elements.append(table)
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("<b>AI Generated Plan</b>", header_style))

    for line in plan_text.split("\n"):
        if line.strip():
            elements.append(Paragraph(line, normal_style))

    doc.build(elements)

    buffer.seek(0)

    return buffer
