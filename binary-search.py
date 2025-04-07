
def binary_search(a_list,item):
    #a_list is a sorted array/list
    #item number that is supposed to be searched

    first = 0
    last = len(a_list) - 1 
    while first<=last:
        mid = int((first+last)/2)
        if a_list[mid] == item:
            print(f"The {item} is found at {mid}")
            break
        elif a_list[mid]>item:
            last = mid -1 
        elif a_list[mid]<item:
            first = mid + 1
    else :
        print(f"The {item} is not found")



if __name__ == "__main__":
    binary_search([2,3,7,9,50,57,79,550],4)