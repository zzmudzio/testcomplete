# Skrypt do przenoszenia na kosz logow z aplikacji TestComplete
# do wyboru opcja przeniesienia wszystkich logow lub wskazania aplikacji, z ktorej chcemy przeniesc logi 
# Mateusz Zmuda, 2022 


import os 
import send2trash


def draw_menu():
    os.system("cls")
    print("MENU: ")
    print(f'Wybierz opcje 1 lub 2(wybranie innej spowoduje odswiezenie menu)')
    print('\033[92m 1. Przeniesienie do kosza logow testcomplete ze wszystkich aplikacji \n 2. Przeniesienie do kosza logow testcomplete ze wskazanej aplikacji \033[0m \n Wybor: ', end="")


def get_menu_decision():
    try:
        choice = int(input())
        return choice 
    except ValueError: # w razie gdyby ktos wpisal cos innego niz cyfry 
        return 0


def remove_logs(path_dict, all=False, indicated_apps=None):
    if all:
        for app, path in path_dict.items():
            for root, directories, files in os.walk(path):
                for directory in directories: 
                    print(f'Przenosze do kosza nastepujace katalogi z aplikacji {app}: {os.path.join(root, directory)}')
                    send2trash.send2trash(os.path.join(root, directory))
    else:
        for app_name in indicated_apps:
            for root, directories, files in os.walk(path_dict[app_name]):
                for directory in directories: 
                    print(f'Przenosze do kosza nastepujace katalogi z aplikacji {app_name}: {os.path.join(root, directory)}')
                    send2trash.send2trash(os.path.join(root, directory))
    return "success"


def get_app_names(path_dict):
    os.system("cls")
    print('Z ktorej/ktorych aplikacji chcesz usunac logi? jezeli wiecej niz jedna, wpisz po przecinku.')
    print('Dostepne aplikacje:')
    for app in path_dict.keys():
        print(f'=>>>> \033[96m {app} \033[0m <<<<=')
    apps = input('Wybor: ')
    separated_list_of_apps = [app.strip().replace(' ', '') for app in apps.split(',')]
    apps_to_remove = remove_absent_apps(path_dict, separated_list_of_apps)
    return apps_to_remove
    

def remove_absent_apps(path_dict, separated_list_of_apps):
    apps_list = list(path_dict.keys())
    indexes_to_remove = []
    for index, separated_app in enumerate(separated_list_of_apps):
        if separated_app not in apps_list:
            indexes_to_remove.append(index)
    final_list_of_apps = [y for x, y in enumerate(separated_list_of_apps) if x not in indexes_to_remove]
    return final_list_of_apps


if __name__ == "__main__":
    log_paths = {'wgos1':'C:\\Users\\m.zmuda-trzebia\\Desktop\\Testowy katalog\\test1_Log',
                'wgos2':'C:\\Users\\m.zmuda-trzebia\\Desktop\\Testowy katalog\\test2_Log'}
    choice = 0 
    while choice not in (1, 2):
        draw_menu()
        choice = get_menu_decision()
    if choice == 1: 
        remove_logs(log_paths, all=True)
    elif choice == 2:
        remove_logs(log_paths, all=False, indicated_apps=get_app_names(log_paths))
