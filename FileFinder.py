import os
def find_files(drives, f):
    print ('Searching, wait please :)')
    find_files = []
    for i in drives:
      for root, dirs, files in os.walk(drives):
          find_files += [os.path.join(root, name) for name in files if name.startswith(f) or name.endswith(f)]
      if not find_files:
          print ('Sorry, but you do not have files with this name. Try to make another request :) ')
      else:
        for element in find_files:
          print(element)
        print ('Programming magic :3. This is full address of all files with this request :) ')
      return find_files
print('Write your request, I try to find them :) ')
file_search=input()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['{0}:'.format(d) for d in letters if os.path.exists('{0}:'.format(d))]
for element in drives:
    drives=element+'\\'
find_files(drives,file_search)










