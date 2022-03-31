"""
this script file starts an notepad app, then looks for a word (i.e. old_word) in given text file (FILE_NAME) and 
if it exists, it's replaced by a new_word
after replacing the contents of file with replaced word/s is compared with a template file 
if they are the same, script succeeds, otherwise fails, which is logged by Log.Message methods
"""


#mateusz zmuda

FILE_NAME = 'test'
old_word = 'topowym'
new_word = 'testowym'

def start_restore_app():
  #start if it's not already started
  if Sys.WaitProcess("notepad", 500).Exists:
    Log.Message('There was an instance of notepad, new process will not be launched')
    handler = Sys.Process("notepad")
    return handler
  else:
    Log.Message('there was no instance of notepad, starting a new one')
    handler = TestedApps.notepad.Run()
    return handler
    
def open_file():
    app = start_restore_app()
    window_handler = app.Form("Bez tytułu — Notatnik")
    window_handler.MenuBar("Aplikacja").MenuItem("Plik").Click()
    app.Popup("Plik").MenuItem("Otwórz...\tCtrl+O").Click()
    app.Dialog("Otwieranie").Window("DUIViewWndClassName", "", 1)\
    .UIAObject("Okienko_Eksploratora").Window("CtrlNotifySink", "", 3).Panel("Widok folderu powłoki")\
    .UIAObject("Widok_elementów").UIAObject("test").dblClick()
    find_and_replace_text(window_handler, app)
    
def find_and_replace_text(wh, app_):
    wh.MenuBar("Aplikacja").MenuItem("Edycja").Click()
    app_.Popup("Edycja").MenuItem("Zamień...\tCtrl+H").Click()
    app_.Dialog("Zamienianie").Edit("Znajdź:").SetText(old_word)
    app_.Dialog("Zamienianie").Edit("Zamień na:").SetText(new_word)
    app_.Dialog("Zamienianie").Button("Zamień wszystko").Click()
    app_.Dialog("Zamienianie").Close()
    save_file()

def save_file():
    start_restore_app().Form('*'+FILE_NAME + ' — Notatnik').MenuBar("Aplikacja").MenuItem("Plik").Click()
    start_restore_app().Popup("Plik").MenuItem("Zapisz\tCtrl+S").Click()
    start_restore_app().Close()
    check_files()
    
def check_files():
    ori_file_location = 'C:\\Users\\m.zmuda-trzebia\\Desktop\\rezultat.txt'
    test_file_location = 'C:\\Users\\m.zmuda-trzebia\\Desktop\\test.txt'
    with open(ori_file_location, 'r') as file:
      original_file_contents = file.read()
    with open(test_file_location, 'r') as file: 
      test_file_contents = file.read()
    if original_file_contents == test_file_contents:
      Log.Message('they are the same!, correct')
    else:
      Log.Message('thery vary')

def main():
    open_file()

    
