#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication,QWidget,
    QHBoxLayout,QVBoxLayout,
    QGroupBox,QButtonGroup,QRadioButton,
    QPushButton, QLabel)
from random import shuffle, randint

class Question():
    '''содержит вопрос, правиьный ответ и три неправельных'''
    def __init__(self, question, right_answer,worg1, worg2, worg3):
        self.question = question
        self.right_answer = right_answer
        self.worg1 = worg1
        self.worg2 = worg2
        self.worg3 = worg3

question_list = []
question_list.append(Question('Овециальный правая рука Спецназовского', 'Rober Bob', 'Taffe', 'Timi', 'Olle'))
question_list.append(Question('Новое спецподразделение в мире', 'Spec Blak Ops', 'Альфа', 'Sas', 'Морские котики'))
question_list.append(Question('Солдат США из спецназовского показал себя в спецоперации в Британии', 'Olle', 'Rober Bob', 'солдаты Jons', 'Taffe'))
question_list.append(Question('Лучший отряд  спецопераций Японии под командованием', 'Капитан шрамовый глаз', 'Майор Синуч', 'Капитана Васкиса', 'Лейтинат Майкл'))
question_list.append(Question('Главный генерал_маршал спецназовского', 'Lev', 'Michael', 'Artem', 'Sasha'))
question_list.append(Question('Название спецоперация в Авганестане', 'Sunny day Olle', 'Глаз прицела', 'Авганестан', 'Spec Blak Ops'))
app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbth_1 = QRadioButton('Вариант 1')
rbth_2 = QRadioButton('вариант 2')
rbth_3 = QRadioButton('вариант 3')
rbth_4 = QRadioButton('вариант 4')

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbth_1)
RadioGroup.addButton(rbth_2)
RadioGroup.addButton(rbth_3)
RadioGroup.addButton(rbth_4)

layot_ans1 = QHBoxLayout()
layot_ans2 = QVBoxLayout()
layot_ans3 = QVBoxLayout()
layot_ans2.addWidget(rbth_1)
layot_ans2.addWidget(rbth_2)
layot_ans3.addWidget(rbth_3)
layot_ans3.addWidget(rbth_4)

layot_ans1.addLayout(layot_ans2)
layot_ans1.addLayout(layot_ans3)

RadioGroupBox.setLayout(layot_ans1)

AnsGroupBox= QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

layot_res = QVBoxLayout()
layot_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layot_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layot_res)

layot_line1 = QHBoxLayout()
layot_line2 = QHBoxLayout()
layot_line3 = QHBoxLayout()

layot_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layot_line2.addWidget(RadioGroupBox)
layot_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layot_line3.addStretch(1)
layot_line3.addWidget(btn_OK, stretch=2)
layot_line3.addStretch(1)

layot_card = QVBoxLayout()

layot_card.addLayout(layot_line1, stretch=2)
layot_card.addLayout(layot_line2, stretch=8)
layot_card.addStretch(1)
layot_card.addLayout(layot_line3, stretch=1)
layot_card.addSpacing(5)
def show_resunt():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbth_1.setChecked(False)
    rbth_2.setChecked(False)
    rbth_3.setChecked(False)
    rbth_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbth_1, rbth_2, rbth_3, rbth_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.worg1)
    answer[2].setText(q.worg2)
    answer[3].setText(q.worg3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_corect(res):
    lb_Result.setText(res)
    show_resunt()

def check_answer():
    if answer[0].isChecked():
        show_corect('Правельно!')
        window.score += 1
        print('Статистика')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_corect('Неверно!')
            print('no')

def next_question():
    window.total += 1
    print('Статистика')
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layot_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.resize(400,300)
window.show()
app.exec()
