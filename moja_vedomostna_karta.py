from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle


class Question:
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(Question('The state language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
question_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
question_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))


app = QApplication([])




window = QWidget()
window.setWindowTitle('Vedomostna karta')
window.move(100, 100) # meni kde sa okno nachadza na obrazovke
window.resize(400, 200) # meni rozmery okna
#------------------------------------


# Text otazky
otazka = QLabel('Ktora z narodnosti neexistuje?')
# Tlacidlo "vyhodnotit"
button = QPushButton("Vyhodnotit")


#---------------------------------------
# Okno s odpovedami
RadioGroupBox = QGroupBox('Odpovede')
btn_answer1 = QRadioButton('Slovenska')
btn_answer2 = QRadioButton('Ceskoslovenska')
btn_answer3 = QRadioButton('Ceska')
btn_answer4 = QRadioButton('Madarska')


btn_group = QButtonGroup()
btn_group.addButton(btn_answer1)
btn_group.addButton(btn_answer2)
btn_group.addButton(btn_answer3)
btn_group.addButton(btn_answer4)


layout_answers = QHBoxLayout() # vytvori riadok
layout_answersV1 = QVBoxLayout() # stlpec 1
layout_answersV2 = QVBoxLayout() # stlpec 2


layout_answersV1.addWidget(btn_answer1)
layout_answersV1.addWidget(btn_answer2)


layout_answersV2.addWidget(btn_answer3)
layout_answersV2.addWidget(btn_answer4)


layout_answers.addLayout(layout_answersV1)
layout_answers.addLayout(layout_answersV2)


RadioGroupBox.setLayout(layout_answers)
# -----------------------------------------------
# Okno s vysledkami
AnswerGroupBox = QGroupBox('Vysledky')
vysledok = QLabel('Spravne/Nespravne')
spravna_odpoved = QLabel('Spravna odpoved')


layout_vysledok = QVBoxLayout()


layout_vysledok.addWidget(vysledok, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_vysledok.addWidget(spravna_odpoved, alignment=Qt.AlignHCenter, stretch=2)


AnswerGroupBox.setLayout(layout_vysledok)
# ----------------------------------------------
# Okno so skore
ScoreGroupBox = QGroupBox('Skore')
body = QLabel('Celkovo mas 0 bodov.')
percenta = QLabel('Celkovo mas 0%.')


layout_score = QVBoxLayout()
layout_score.addWidget(body, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_score.addWidget(percenta, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))


ScoreGroupBox.setLayout(layout_score)
#----------------------------------------------


layout_line1 = QHBoxLayout() # Otazka
layout_line2 = QHBoxLayout() # Okienko s odpovedami
layout_line3 = QHBoxLayout() # Tlacitko vyhodnotit


layout_line1.addWidget(otazka, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))


layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnswerGroupBox)
layout_line2.addWidget(ScoreGroupBox) # TOTO
AnswerGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch = 2) # the button should be large
layout_line3.addStretch(1)


layout_main = QVBoxLayout()


layout_main.addLayout(layout_line1, stretch = 2)
layout_main.addLayout(layout_line2, stretch = 8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch = 1)
layout_main.addStretch(1)
layout_main.setSpacing(5) # prida medzery medzi layouty


def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button.setText("Dalsia otazka")


def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    button.setText("Vyhodnotit")


    btn_group.setExclusive(False)#prikaz, vdaka ktoremu vieme resetovat radio buttons
    btn_answer1.setChecked(False) #nastavuje, ci je button zaskrnuty
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    btn_group.setExclusive(True)#vdaka tomuto, vieme znovu zaznacit iba jeden radiobutton




answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]


def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    otazka.setText(q.question)
    spravna_odpoved.setText(q.right_ans)
    show_question()


def show_correct(res):
    vysledok.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct("Spravne!")
        window.score += 1
        print("Prave mas: ", window.score, " bodov.")
        print('Percenta:', (window.score/window.total*100), "%")
    else:
        show_correct("Nespravne!")
        body.setText("Body:" + str(window.score))
        percenta.setText("Percenta:" + str(window.score/window.total*10) + "%")


def next_question():
    window.total +=1
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
        #exit()
    q = question_list[window.cur_question]
    ask(q)


window.cur_question = -1
window.score = 0
window.total = 1


def click_ok():
    if button.text() == 'Vyhodnotit':
        check_answer()
    else:
        next_question()


q = Question("Co je moje najoblubenejsie zviera?", "Macka", "Pes", "Kon", "Panda")


ask(q)


button.clicked.connect(click_ok)


window.setLayout(layout_main)
window.show()
app.exec()
