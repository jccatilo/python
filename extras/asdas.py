import os



path, dirs, files = next(os.walk(r"C:\Users\User\Desktop\python\organize files\folders"))
file_count = len(dirs)
#print(file_count)
semi_ext_array = []
for i in range (file_count):
    l = os.listdir(r"C:\Users\User\Desktop\python\organize files\folders")
    for e in l:
        #print(f"File name is {e} and the extenson is {os.path.splitext(e)[0]}")
        data = str(e)
        semi_ext_array.append(data)

ext_array = list(dict.fromkeys(semi_ext_array))
print(ext_array)

