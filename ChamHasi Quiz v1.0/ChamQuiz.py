from tkinter import *
from tkinter import messagebox as msg
import json
from datetime import datetime

with open('Questions.json') as Questions_file:
  data = json.load(Questions_file)

acronym_ques = (data['Acronym_questions'])
acronym_ans = (data['Acronym_answer'])
acronym_opt = (data['Acronym_option'])

animation_ques = (data['Animation_questions'])
animation_ans = (data['Animation_answer'])
animation_opt = (data['Animation_option'])

computer_ques = (data['Computer_questions'])
computer_ans = (data['Computer_answer'])
computer_opt = (data['Computer_option'])

program_ques = (data['Programming_questions'])
program_ans = (data['Programming_answer'])
program_opt = (data['Programming_option'])

it_ques = (data['It_questions'])
it_ans = (data['It_answer'])
it_opt = (data['It_option'])

reli_ques = (data['Religion_questions'])
reli_ans = (data['Religion_answer'])
reli_opt = (data['Religion_option'])

class MainApp:
  def __init__(self, game):
    self.game = game
    self.game.title('CHAM Quiz')
    self.game.geometry('1500x800+90+90')
    self.game.iconbitmap('Cham.ico')
    self.game.config(background='#313440')
    self.game.resizable(width=False, height=False)

    self.register_list = []

  # The frames
    self.begin_frame = Frame(self.game, bg='#313440')
    self.begin_frame.pack(expand=YES)
    self.register_frame = Frame(self.game, bg='#313440', bd=1, highlightthickness=5, highlightbackground="#3399ff", highlightcolor="#3399ff")
    self.start_frame = Frame(self.game, bg='#313440')

    self.acronym_question_frame = Frame(self.game, bg='#313440')
    self.animation_question_frame = Frame(self.game, bg='#313440')
    self.computer_question_frame = Frame(self.game, bg='#313440')
    self.company_question_frame = Frame(self.game, bg='#313440')
    self.it_question_frame = Frame(self.game, bg='#313440')
    self.religion_question_frame = Frame(self.game, bg='#313440')

    self.up_frame = Frame(self.game,bg="#3399ff")

    self.dwon_frame = Frame(self.game,bg='#313440')
    self.dwon_frame.pack(side=BOTTOM)

    label1 = Label(self.begin_frame, text='WELCOME TO CHAM QUIZ GAME', font=('Helvetica', 55, 'bold','underline'), fg='white', bg='#313440')
    label2 = Label(self.begin_frame, text='Before starting, you have to know that this game is completely free and OPEN-SOURCE.\nTherefore, selling it or using it to earn money is not allowed, so be aware.\nFor more information or free games you can visit us on our website :\nwww.chamsoudine.com OR chamsoudine50@gmail.com\n\n\nThank you for visiting us in advance !', font=('Helvetica', 26, 'bold'), fg='white', bg='#313440')
    label1.grid(pady=80)
    label2.grid(pady=25)

    start_button = Button(self.begin_frame, text='Start The Game', width=70, height=2, font=('Helvetica', 25, 'bold'), activebackground='white', activeforeground='#3399ff', fg='white', bg='#3399ff', highlightthickness=0, command=self.register)
    start_button.grid()

  def register(self):
    self.begin_frame.pack_forget()
    self.register_frame.place(x=450, y=250)

    start_label = Label(self.register_frame, text='    Registration    ', font=('Helvetica', 50, 'bold'), fg='white', bg='#313440')
    start_label.grid(row=0, columnspan=2, pady=20)
    name_label = Label(self.register_frame, text='F.Name:', font=('Helvetica', 20, 'bold'), fg='white', bg='#313440')
    name_label.grid(row=1, column=0, sticky=W)
    last_label = Label(self.register_frame, text='L.Name:', font=('Helvetica', 20, 'bold'), fg='white', bg='#313440')
    last_label.grid(row=2, column=0, sticky=W)
    self.name_entry = Entry(self.register_frame, width=25, font=('Helvetica', 20, 'bold'), fg='white', bg='#313440', highlightthickness=0)
    self.name_entry.grid(row=1, column=1, pady=5)
    self.last_entry = Entry(self.register_frame, width=25, font=('Helvetica', 20, 'bold'), fg='white', bg='#313440', highlightthickness=0)
    self.last_entry.grid(row=2, column=1, pady=10)
    register_button = Button(self.register_frame, text='Register', width=30, height=1, font=('Helvetica', 20, 'bold'), activebackground='white', activeforeground="#3399ff", fg='white', bg='#3399ff', highlightthickness=0, command=self.start_window)
    register_button.grid(row=3, columnspan=2, pady=15)

  def about(self):
    msg.showinfo("About","CHAM QUIZ is an OPEN-SOURCE Game developed by Chamsoudine Boubacar known as Cham50. The version of this application is v1.0, and it was released to the public on monday 2021/09/06.\n\nFor more information please consider visiting our website www.chamsoudine.com. Thanks!")

  def start_window(self):
    self.begin_frame.pack_forget()
    self.register_frame.pack_forget()
    self.start_frame.pack(expand=YES)

    self.first_name = self.name_entry.get()
    self.last_name = self.last_entry.get()

    if self.first_name == '' and self.last_name == '':
      msg.showerror('Sorry', 'Please enter your name and last name before starting the game !')
      self.start_frame.pack(expand=YES)
    else:
      self.register_list.append(self.first_name)
      self.register_list.append(self.last_name)

      msg.showinfo('Successful', f'{self.first_name} {self.last_name} is successfully registed. Thanks!')
      self.name_entry.delete(0, END)
      self.last_entry.delete(0, END)

      start_label = Label(self.start_frame, text=(f'Welcome Mr/Ms {self.first_name} to CHAM Quiz. \nMake your choice to start the game.'), font=('Helvetica', 45, 'bold'), fg='white', bg='#313440')
      start_label.grid(row=0, columnspan=3, pady=30)

      acronym_button = Button(self.start_frame, text='Acronym', width=23, height=2, font=('Helvetica', 25, 'bold'), fg='white', bg='#3399ff', activeforeground="#3399ff", highlightthickness=0, command=self.acronymstart)
      animation_button = Button(self.start_frame, text='Animation', width=23, height=2, font=('Helvetica', 25, 'bold'), fg='white', bg='#3399ff', activeforeground="#3399ff", highlightthickness=0, command=self.animestart)
      program_button = Button(self.start_frame, text='Programming', width=23, height=2, font=('Helvetica', 25, 'bold'), fg='white', bg='#3399ff', activeforeground="#3399ff", highlightthickness=0, command=self.programstart)
      computerScience_button = Button(self.start_frame, text='Computer Science', width=23, height=2, font=('Helvetica', 25, 'bold'), fg='white', bg='#3399ff', activeforeground="#3399ff", highlightthickness=0, command=self.computerstart)
      it_button = Button(self.start_frame, text='I.T', width=23, height=2, font=('Helvetica', 25, 'bold'), fg='white', bg='#3399ff', activeforeground="#3399ff", highlightthickness=0, command=self.itstart)
      religion_button = Button(self.start_frame, text='Religion', width=23, height=2, font=('Helvetica', 25, 'bold'), fg='white', bg='#3399ff', activeforeground="#3399ff", highlightthickness=0, command=self.religionstart)
      exit_button = Button(self.start_frame, text='Exit Game', width=23, height=2, font=('Helvetica', 25, 'bold'), fg='white', bg='#ff3333', activeforeground="#ff3333", highlightthickness=0, command=self.game.destroy)
      about_button = Button(self.start_frame, text="About", width=23, height=2, bg="#ff3333", fg="white", font=("Helvetica",25,"bold"), activeforeground="#ff3333",highlightthickness=0, command=self.about)

      acronym_button.grid(row=1, column=0, padx=5, pady=15)
      animation_button.grid(row=1, column=1, pady=15)
      computerScience_button.grid(row=1, column=2, padx=5, pady=15)
      program_button.grid(row=2, column=0, padx=5, pady=15)
      it_button.grid(row=2, column=1, padx=5, pady=15)
      religion_button.grid(row=2, column=2, padx=5, pady=15)
      exit_button.grid(row=3, column=1, padx=5, pady=15)
      about_button.grid(row=3, column=2, padx=5, pady=15)

  def window(self):
    self.win = Toplevel()
    self.win.iconbitmap('Cham.ico')
    self.win.geometry('1500x800+90+90')
    self.win.config(background="#313440")
    self.win.resizable(width=False, height=False)

# ============================================ Acronym Window ============================================
  def acronymstart(self):
    self.window()
    self.win.title('Acronym')

    self.acro_ques_no = 0
    self.acro_display_question()
    self.opt_selected = IntVar()
    self.opts = self.acro_radio_buttons()
    self.acro_display_options()
    self.data_size = len(acronym_ques)
    self.correct = 0

    self.next_button = Button(self.win, text="Next Question", width=20, bg="#3399ff", fg="white", font=("Helvetica",20,"bold"), activeforeground="#3399ff", command=self.acro_next_btn)
    self.next_button.place(x=1135, y=730)
    self.quit_button = Button(self.win, text="Quit the game", width=20, bg="#ff3333", fg="white", font=("Helvetica",20,"bold"), activeforeground="#ff3333", command=self.win.destroy)
    self.quit_button.place(x=750, y=730)

    self.up_frame = Frame(self.win, bg="#3399ff")
    self.up_frame.pack(side=TOP, fill=X)

    time = datetime.now()
    now = time.date()
    player = Label(self.up_frame, text=f"Player: {self.first_name} {self.last_name}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    
    player_section = Label(self.up_frame, text="Section: Acronym", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    
    player_level = Label(self.up_frame, text="Questions N°: 15", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    
    current_time = Label(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")    
    
    player.grid(row=0, column=0, padx=5)
    player_section.grid(row=0, column=1, padx=25)
    player_level.grid(row=0, column=2, padx=25)
    current_time.grid(row=0, column=3, padx=25)

  def acro_display_result(self):
    wrong_count = self.data_size - self.correct
    correct = f"Correct Answers: {self.correct}"
    wrong = f"Wrong Answers: {wrong_count}"

    score = int(self.correct / self.data_size * 100)
    result = f"Total Score: {score}%"

    msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")

  def acro_check_ans(self, acro_ques_no):
    if self.opt_selected.get() == acronym_ans[acro_ques_no]:
      return True

  def acro_next_btn(self):
    if self.acro_check_ans(self.acro_ques_no):
      self.correct += 1

    self.acro_ques_no += 1
    if self.acro_ques_no == self.data_size:
      self.acro_display_result()
      self.win.destroy()
    else:
      self.acro_display_question()
      self.acro_display_options()

  def acro_display_options(self):
    self.val = 0
    self.opt_selected.set(0)
    for option in acronym_opt[self.acro_ques_no]:
      self.opts[self.val]['text'] = option
      self.val += 1

  def acro_display_question(self):
    self.qu_no = Label(self.win, text = acronym_ques[self.acro_ques_no], width=45, font=( 'Helvetica' ,40, 'bold' ), bg="#313440", fg="white")
    self.qu_no.place(x=25, y=100)

  def acro_radio_buttons(self):
    self.acro_ques_list = []
    y_pos = 270
    while len(self.acro_ques_list) < 4:
      self.radio_btn = Radiobutton(self.win, text=" ", variable=self.opt_selected, value = len(self.acro_ques_list)+1, font=("Helvetica",25, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440")
      self.acro_ques_list.append(self.radio_btn)
      self.radio_btn.place(x=110, y=y_pos)
      y_pos += 80
    return self.acro_ques_list

# ============================================ Animation Window ============================================
  def animestart(self):
    self.window()
    self.win.title('Animation')

    self.anime_ques_no = 0
    self.anime_display_question()
    self.opt_selected = IntVar()
    self.opts = self.anime_radio_buttons()
    self.anime_display_options()
    self.data_size = len(animation_ques)
    self.correct = 0

    self.next_button = Button(self.win, text="Next Question", width=20, bg="#3399ff", fg="white", font=("Helvetica",20,"bold"), command=self.anime_next_btn)
    self.next_button.place(x=1135, y=730)
    self.quit_button = Button(self.win, text="Quit the game", width=20, bg="#ff3333", fg="white", font=("Helvetica",20,"bold"), activeforeground="#ff3333", command=self.win.destroy)
    self.quit_button.place(x=750, y=730)

    self.up_frame = Frame(self.win, bg="#3399ff")
    self.up_frame.pack(side=TOP, fill=X)

    time = datetime.now()
    now = time.date()
    player = Label(self.up_frame, text=f"Player: {self.first_name} {self.last_name}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_section = Label(self.up_frame, text="Section: Anime", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_level = Label(self.up_frame, text="Questions N°: 15", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    current_time = Label(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player.grid(row=0, column=0, padx=5)
    player_section.grid(row=0, column=1, padx=25)
    player_level.grid(row=0, column=2, padx=25)
    current_time.grid(row=0, column=3, padx=25)

  def anime_display_result(self):
    wrong_count = self.data_size - self.correct
    correct = f"Correct Answers: {self.correct}"
    wrong = f"Wrong Answers: {wrong_count}"

    score = int(self.correct / self.data_size * 100)
    result = f"Total Score: {score}%"

    msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")

  def anime_check_ans(self, anime_ques_no):
    if self.opt_selected.get() == animation_ans[anime_ques_no]:
      return True

  def anime_next_btn(self):
    if self.anime_check_ans(self.anime_ques_no):
      self.correct += 1

    self.anime_ques_no += 1
    if self.anime_ques_no == self.data_size:
      self.anime_display_result()
      self.win.destroy()
    else:
      self.anime_display_question()
      self.anime_display_options()

  def anime_display_options(self):
    self.val = 0
    self.opt_selected.set(0)
    for option in animation_opt[self.anime_ques_no]:
      self.opts[self.val]['text'] = option
      self.val += 1

  def anime_display_question(self):
    self.qu_no = Label(self.win, text = animation_ques[self.anime_ques_no], width=45, height=3, font=( 'Helvetica' ,40, 'bold' ), bg="#313440", fg="white" )
    self.qu_no.place(x=25, y=80)

  def anime_radio_buttons(self):
    self.anime_ques_list = []
    y_pos = 300
    while len(self.anime_ques_list) < 4:
      self.radio_btn = Radiobutton(self.win, text=" ", variable=self.opt_selected, value = len(self.anime_ques_list)+1, font=("Helvetica",25, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440")
      self.anime_ques_list.append(self.radio_btn)
      self.radio_btn.place(x=110, y=y_pos)
      y_pos += 80
    return self.anime_ques_list

# ============================================ Computer Science Window ============================================
  def computerstart(self):
    self.window()
    self.win.title('Computer Science')

    self.computer_ques_no = 0
    self.comp_display_question()
    self.opt_selected = IntVar()
    self.opts = self.comp_radio_buttons()
    self.comp_display_options()
    self.data_size = len(computer_ques)
    self.correct = 0

    self.next_button = Button(self.win, text="Next Question", width=20, bg="#3399ff", fg="white", font=("Helvetica",20,"bold"), command=self.comp_next_btn)
    self.next_button.place(x=1135, y=730)
    self.quit_button = Button(self.win, text="Quit the game", width=20, bg="#ff3333", fg="white", font=("Helvetica",20,"bold"), activeforeground="#ff3333", command=self.win.destroy)
    self.quit_button.place(x=750, y=730)

    self.up_frame = Frame(self.win, bg="#3399ff")
    self.up_frame.pack(side=TOP, fill=X)

    time = datetime.now()
    now = time.date()
    player = Label(self.up_frame, text=f"Player: {self.first_name} {self.last_name}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_section = Label(self.up_frame, text="Section: Computer Science", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_level = Label(self.up_frame, text="Questions N°: 15", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    current_time = Label(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player.grid(row=0, column=0, padx=5)
    player_section.grid(row=0, column=1, padx=25)
    player_level.grid(row=0, column=2, padx=25)
    current_time.grid(row=0, column=3, padx=25)

  def comp_display_result(self):
    wrong_count = self.data_size - self.correct
    correct = f"Correct Answers: {self.correct}"
    wrong = f"Wrong Answers: {wrong_count}"

    score = int(self.correct / self.data_size * 100)
    result = f"Total Score: {score}%"

    msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")

  def comp_check_ans(self, computer_ques_no):
    if self.opt_selected.get() == computer_ans[computer_ques_no]:
      return True

  def comp_next_btn(self):
    if self.comp_check_ans(self.computer_ques_no):
      self.correct += 1

    self.computer_ques_no += 1
    if self.computer_ques_no == self.data_size:
      self.comp_display_result()
      self.win.destroy()
    else:
      self.comp_display_question()
      self.comp_display_options()

  def comp_display_options(self):
    self.val = 0
    self.opt_selected.set(0)
    for option in computer_opt[self.computer_ques_no]:
      self.opts[self.val]['text'] = option
      self.val += 1

  def comp_display_question(self):
    self.qu_no = Label(self.win, text = computer_ques[self.computer_ques_no], width=45, height=3, font=( 'Helvetica' ,40, 'bold' ), justify='center', bg="#313440", fg="white")
    self.qu_no.place(x=25, y=80)

  def comp_radio_buttons(self):
    self.computer_ques_list = []
    y_pos = 330
    while len(self.computer_ques_list) < 4:
      self.radio_btn = Radiobutton(self.win, text=" ", variable=self.opt_selected, value = len(self.computer_ques_list)+1, font=("Helvetica",25, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440")
      self.computer_ques_list.append(self.radio_btn)
      self.radio_btn.place(x=110, y=y_pos)
      y_pos += 80
    return self.computer_ques_list

# ============================================ Programming Window ============================================
  def programstart(self):
    self.window()
    self.win.title('Programming')

    self.pro_ques_no = 0
    self.pro_display_question()
    self.opt_selected = IntVar()
    self.opts = self.pro_radio_buttons()
    self.pro_display_options()
    self.data_size = len(program_ques)
    self.correct = 0

    self.next_button = Button(self.win, text="Next Question", width=20, bg="#3399ff", fg="white", font=("Helvetica",20,"bold"), command=self.pro_next_btn)
    self.next_button.place(x=1135, y=730)
    self.quit_button = Button(self.win, text="Quit the game", width=20, bg="#ff3333", fg="white", font=("Helvetica",20,"bold"), activeforeground="#ff3333", command=self.win.destroy)
    self.quit_button.place(x=750, y=730)

    self.up_frame = Frame(self.win, bg="#3399ff")
    self.up_frame.pack(side=TOP, fill=X)

    time = datetime.now()
    now = time.date()
    player = Label(self.up_frame, text=f"Player: {self.first_name} {self.last_name}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_section = Label(self.up_frame, text="Section: Programming", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_level = Label(self.up_frame, text="Questions N°: 15", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    current_time = Label(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player.grid(row=0, column=0, padx=5)
    player_section.grid(row=0, column=1, padx=25)
    player_level.grid(row=0, column=2, padx=25)
    current_time.grid(row=0, column=3, padx=25)

  def pro_display_result(self):
    wrong_count = self.data_size - self.correct
    correct = f"Correct Answers: {self.correct}"
    wrong = f"Wrong Answers: {wrong_count}"

    score = int(self.correct / self.data_size * 100)
    result = f"Total Score: {score}%"

    msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")

  def pro_check_ans(self, pro_ques_no):
    if self.opt_selected.get() == program_ans[pro_ques_no]:
      return True

  def pro_next_btn(self):
    if self.pro_check_ans(self.pro_ques_no):
      self.correct += 1

    self.pro_ques_no += 1
    if self.pro_ques_no == self.data_size:
      self.pro_display_result()
      self.win.destroy()
    else:
      self.pro_display_question()
      self.pro_display_options()

  def pro_display_options(self):
    self.val = 0
    self.opt_selected.set(0)
    for option in program_opt[self.pro_ques_no]:
      self.opts[self.val]['text'] = option
      self.val += 1

  def pro_display_question(self):
    self.qu_no = Label(self.win, text = program_ques[self.pro_ques_no], width=45, height=4, font=( 'Helvetica' ,40, 'bold' ), bg="#313440", fg="white")
    self.qu_no.place(x=25, y=80)

  def pro_radio_buttons(self):
    self.pro_ques_list = []
    y_pos = 330
    while len(self.pro_ques_list) < 4:
      self.radio_btn = Radiobutton(self.win, text=" ", variable=self.opt_selected, value = len(self.pro_ques_list)+1, font=("Helvetica",25, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440")
      self.pro_ques_list.append(self.radio_btn)
      self.radio_btn.place(x=110, y=y_pos)
      y_pos += 80
    return self.pro_ques_list

# ============================================ IT Window ============================================
  def itstart(self):
    self.window()
    self.win.title('IT')

    self.it_ques_no = 0
    self.it_display_question()
    self.opt_selected = IntVar()
    self.opts = self.it_radio_buttons()
    self.it_display_options()
    self.data_size = len(it_ques)
    self.correct = 0

    self.next_button = Button(self.win, text="Next Question", width=20, bg="#3399ff", fg="white", font=("Helvetica",20,"bold"), command=self.it_next_btn)
    self.next_button.place(x=1135, y=730)
    self.quit_button = Button(self.win, text="Quit the game", width=20, bg="#ff3333", fg="white", font=("Helvetica",20,"bold"), activeforeground="#ff3333", command=self.win.destroy)
    self.quit_button.place(x=750, y=730)

    self.up_frame = Frame(self.win, bg="#3399ff")
    self.up_frame.pack(side=TOP, fill=X)

    time = datetime.now()
    now = time.date()
    player = Label(self.up_frame, text=f"Player: {self.first_name} {self.last_name}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_section = Label(self.up_frame, text="Section: IT", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_level = Label(self.up_frame, text="Questions N°: 15", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    current_time = Label(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player.grid(row=0, column=0, padx=5)
    player_section.grid(row=0, column=1, padx=25)
    player_level.grid(row=0, column=2, padx=25)
    current_time.grid(row=0, column=3, padx=25)

  def it_display_result(self):
    wrong_count = self.data_size - self.correct
    correct = f"Correct Answers: {self.correct}"
    wrong = f"Wrong Answers: {wrong_count}"

    score = int(self.correct / self.data_size * 100)
    result = f"Total Score: {score}%"

    msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")

  def it_check_ans(self, it_ques_no):
    if self.opt_selected.get() == it_ans[it_ques_no]:
      return True

  def it_next_btn(self):
    if self.it_check_ans(self.it_ques_no):
      self.correct += 1

    self.it_ques_no += 1
    if self.it_ques_no == self.data_size:
      self.it_display_result()
      self.win.destroy()
    else:
      self.it_display_question()
      self.it_display_options()

  def it_display_options(self):
    self.val = 0
    self.opt_selected.set(0)
    for option in it_opt[self.it_ques_no]:
      self.opts[self.val]['text'] = option
      self.val += 1

  def it_display_question(self):
    self.qu_no = Label(self.win, text = it_ques[self.it_ques_no], width=45, height=3, font=( 'Helvetica' ,40, 'bold' ), bg="#313440", fg="white")
    self.qu_no.place(x=25, y=80)

  def it_radio_buttons(self):
    self.it_ques_list = []
    y_pos = 300
    while len(self.it_ques_list) < 4:
      self.radio_btn = Radiobutton(self.win, text=" ", variable=self.opt_selected, value = len(self.it_ques_list)+1, font=("Helvetica",25, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440")
      self.it_ques_list.append(self.radio_btn)
      self.radio_btn.place(x=110, y=y_pos)
      y_pos += 80
    return self.it_ques_list

# ============================================ Religion Window ============================================
  def religionstart(self):
    self.window()
    self.win.title('Religion')

    self.reli_ques_no = 0
    self.reli_display_question()
    self.opt_selected = IntVar()
    self.opts = self.reli_radio_buttons()
    self.reli_display_options()
    self.data_size = len(reli_ques)
    self.correct = 0

    self.next_button = Button(self.win, text="Next Question", width=20, bg="#3399ff", fg="white", font=("Helvetica",20,"bold"), command=self.reli_next_btn)
    self.next_button.place(x=1135, y=730)
    self.quit_button = Button(self.win, text="Quit the game", width=20, bg="#ff3333", fg="white", font=("Helvetica",20,"bold"), activeforeground="#ff3333", command=self.win.destroy)
    self.quit_button.place(x=750, y=730)

    self.up_frame = Frame(self.win, bg="#3399ff")
    self.up_frame.pack(side=TOP, fill=X)

    time = datetime.now()
    now = time.date()
    player = Label(self.up_frame, text=f"Player: {self.first_name} {self.last_name}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_section = Label(self.up_frame, text="Section: Religion", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player_level = Label(self.up_frame, text="Questions N°: 15", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    current_time = Label(self.up_frame, text=f"Date: {now}", font=("Helvetica",15,"bold"), bg="#3399ff", fg="white")
    player.grid(row=0, column=0, padx=5)
    player_section.grid(row=0, column=1, padx=25)
    player_level.grid(row=0, column=2, padx=25)
    current_time.grid(row=0, column=3, padx=25)

  def reli_display_result(self):
    wrong_count = self.data_size - self.correct
    correct = f"Correct Answers: {self.correct}"
    wrong = f"Wrong Answers: {wrong_count}"

    score = int(self.correct / self.data_size * 100)
    result = f"Total Score: {score}%"

    msg.showinfo("Result", f"{result}\n{correct}\n{wrong}")

  def reli_check_ans(self, reli_ques_no):
    if self.opt_selected.get() == reli_ans[reli_ques_no]:
      return True

  def reli_next_btn(self):
    if self.reli_check_ans(self.reli_ques_no):
      self.correct += 1

    self.reli_ques_no += 1
    if self.reli_ques_no == self.data_size:
      self.reli_display_result()
      self.win.destroy()
    else:
      self.reli_display_question()
      self.reli_display_options()

  def reli_display_options(self):
    self.val = 0
    self.opt_selected.set(0)
    for option in reli_opt[self.reli_ques_no]:
      self.opts[self.val]['text'] = option
      self.val += 1

  def reli_display_question(self):
    self.qu_no = Label(self.win, text = reli_ques[self.reli_ques_no], width=45, height=3, font=( 'Helvetica' ,40, 'bold' ), bg="#313440", fg="white")
    self.qu_no.place(x=25, y=80)

  def reli_radio_buttons(self):
    self.reli_ques_list = []
    y_pos = 270
    while len(self.reli_ques_list) < 4:
      self.radio_btn = Radiobutton(self.win, text=" ", variable=self.opt_selected, value = len(self.reli_ques_list)+1, font=("Helvetica",25, 'bold'), bg="#313440", fg="white", activebackground="#3399ff", activeforeground="white", selectcolor="#313440")
      self.reli_ques_list.append(self.radio_btn)
      self.radio_btn.place(x=110, y=y_pos)
      y_pos += 80
    return self.reli_ques_list


game = Tk()
ob_game = MainApp(game)
game.mainloop()
