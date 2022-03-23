# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from celery_app import task1, task2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("wtf it works! hhhhh")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("main lanuched")
    ans = task1.add.delay(2, 4)
    print("result for add is {}".format(ans))
    # ans2 = task2.multiply.delay(2,4)
    # print("result for multy is {}".format(ans2))
    print_hi('PyCharm')

