import os
import asyncio
from sys import platform


async def find_all_files(path, f):
    print('Searching, wait please :)')
    find_files = []
    if not path == []:
        for root, dirs, files in os.walk(path):
            find_files += [os.path.join(root, name) for name in files if name.startswith(f) or name.endswith(f)
                           or f == '__main__']
        if not find_files:
            print('Sorry, but you do''not have files with this name. Try to make another request :)')
        else:
            for file in find_files:
                print(file)
        print('Programming magic :3. This is full address of all files with this request :) ')
    return find_files


print('Write your request, I try to find them :) ')
file_search = input()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['{0}:'.format(d) for d in letters if os.path.exists('{0}:'.format(d))]
if platform == "win32":
    for element in drives:
        drives = element+'\\'
elif platform == "darwin":
    for element in drives:
        drives = element+'\\'
else:
    for element in drives:
        drives = element+'/'
if __name__ == '__main__':
    asyncio.run(find_all_files(drives, file_search))
