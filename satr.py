
import fitz 
from docx import Document
def hisoblash(word_fayli):
    qator_soni = 0

    # Word fayl
    doc = Document(word_fayli)

    #  qatorlarni hisoblaymiz
    for paragraf in doc.paragraphs:
        qator_soni += len(paragraf.text.split('\n'))

    return qator_soni

#  manzilni kiriting
word_fayli = 'sarvar.docx'

#  hisoblash
natija = hisoblash(word_fayli)

print(f"{word_fayli} faylida {natija} ta qator bor.")
