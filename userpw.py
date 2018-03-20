#!/usr/bin/env python
# encoding: utf-8

db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken,try another:'
            continue
        else:
            break
    pwd = raw_input('passwd:')

    db[name] = pwd

def olduser():
    name = raw_input('login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else:
        print 'login incorrect'

def org_menu():
    input_ok = True
    while input_ok:
        org_item = raw_input("您要进行的操作，删除用户请输入delete，显示所有存在用户请速all，退出请选择q")
        if org_item == 'q':
            input_ok = False
        if org_item == 'all':
            print db.items()
        if org_item == 'delete':
            which_count = raw_input("您要删除哪个账户")
            del db[which_count]
            print db

def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
(M)enu
Enter choice:"""

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s' % choice
            if choice not in 'neqm':
                print 'try aiain'
            else:
                chosen = True



        if choice == 'q':done =True
        if choice == 'n':newuser()
        if choice == 'e':olduser()
        if choice == 'm':org_menu()


if __name__ =='__main__':
    showmenu()

