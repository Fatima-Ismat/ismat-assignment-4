import os
path=input("Enter the path:")     #C:\Users\user\Desktop\images1\
path=path.replace('\\','/')      #\
print(path)
#rename(old_name, new_name)
print(os.listdir(path))   #[]

def main():
     i=0
     for filename in os.listdir(path):
          new_name=path+"car"+str(i)+'.jpg'
          old_name=path+filename
          os.rename(old_name,new_name)
          i+=1

main()


