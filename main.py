import os
import time
import multiprocessing

path="D:\\coding"
processes=[]

def delete_folder(path):
    print("Removing node_modules folder "+path)
    os.system('rmdir /S /Q "{}"'.format(path))

def scan_dir(path):
    for item in os.listdir(path):
        item_path=os.path.join(path,item)
        if item=="node_modules":
            p=multiprocessing.Process(target=delete_folder,args=(item_path,))
            processes.append(p)
            p.start()
            continue
        if os.path.isdir(item_path):
            scan_dir(item_path)
        else:
            print(item_path)


if __name__ == '__main__':
    start=time.time()
    scan_dir(path)
    for p in processes:
        p.join()
    print(time.time()-start)
