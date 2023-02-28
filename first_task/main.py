import re
import os

from resolution import get_resolution



# TODO 2: Написать изначальную директорию где лежит Стимовская папка
BASE_DIR = r'N:\\'
video_settings_path = BASE_DIR + r'Steam\steamapps\common\Underlords\game\dac\cfg\video.txt'
run_game_path = BASE_DIR + r'Steam\steamapps\common\Underlords\game\bin\win64\underlords.exe'

try:
    # TODO 3: Получить данные с текстового файла и записать их в списке
    with open(video_settings_path, 'r') as video_settings_file:
        video_settings_data = video_settings_file.readlines()
    our_resolution_data = get_resolution()
    for index_line in range(len(video_settings_data)):
        # TODO 4: Пройтись по списку и найти с помощью regex линии где находятся ширина и высота
        if re.search('(defaultres")[ \t]+(.)[0-9]*(.)', video_settings_data[index_line]):
            video_settings_data[index_line] = f'\t"setting.defaultres"\t\t"' \
                                              f'{str(our_resolution_data[0])}"\n'

        if re.search('(defaultresheight")[ \t]+(.)[0-9]*(.)', video_settings_data[index_line]):
            video_settings_data[index_line] = f'\t"setting.defaultresheight"\t\t"' \
                                              f'{str(our_resolution_data[1])}"\n'

    # TODO 5: Записать в файле изменения
    with open(video_settings_path, 'w') as video_settings_file:
        video_settings_file.writelines(video_settings_data)

    # TODO 6: Запустить игру
    os.system(run_game_path)
except IOError:
    print('Нельзя найти файл. Пожалуйста введите соответствующий путь!')
finally:
    print("Программа завершена")

