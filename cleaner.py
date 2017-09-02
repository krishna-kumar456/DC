import os

downloads_folder = '/Users/redfruit/Downloads'
folders = ['Documents', 'Images', 'Media', 'Packages', 'Others']
doc_file_types = ['.doc', '.docx']
image_file_types = ['.jpg', '.png']
media_file_types = ['.mp3', '.mp4', '.mkv']
package_file_types = ['.zip', '.rar']


if __name__ == '__main__':

    for folder in folders:
        new_folder = downloads_folder + '/' + folder
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

    onlyfiles = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]

    for files in onlyfiles:
        print(files)
        ext = os.path.splitext(files)[-1].lower()
        print(ext)

        if ext in doc_file_types:
            os.rename(downloads_folder + '/' + files, downloads_folder + '/Documents' + '/' + files )

        elif ext in image_file_types:
            os.rename(downloads_folder + '/' + files, downloads_folder + '/Images' + '/' + files)

        elif ext in media_file_types:
            os.rename(downloads_folder + '/' + files, downloads_folder + '/Media' + '/' + files)

        elif ext in package_file_types:
            os.rename(downloads_folder + '/' + files , downloads_folder + '/Packages' + '/' + files)

        else:
            os.rename(downloads_folder + '/' + files, downloads_folder + '/Others' + '/' + files)
    print('Cleanup complete!')
