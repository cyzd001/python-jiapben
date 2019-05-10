import threading
from time import ctime,sleep
from selenium import webdriver

# driver=webdriver.Chrome()

def music(func):
    driver = webdriver.Chrome()
    print("I was at the %s! %s" % (func, ctime()))
    driver.get("http://game.huihuang200.com/")
def move(func):
    driver = webdriver.Chrome()
    print("I was at the %s! %s" % (func, ctime()))
    driver.get("http://game.huihuang200.com/")
def move1(func):
    driver = webdriver.Chrome()
    print("I was at the %s! %s" % (func, ctime()))
    driver.get("http://game.huihuang200.com/")
def move2(func):
    driver = webdriver.Chrome()
    print("I was at the %s! %s" % (func, ctime()))
    driver.get("http://game.huihuang200.com/")



threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)
t3 = threading.Thread(target=move1,args=(u'阿凡达',))
threads.append(t3)
t4 = threading.Thread(target=move2,args=(u'阿凡达',))
threads.append(t4)



if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print("all over %s" %ctime())