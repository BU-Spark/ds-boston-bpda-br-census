# coding:utf-8

import os,re
def Generate_menu(dir):
    out_file = "index.html"
    title = "index"
    head_text1 = "<HTML><HEAD><TITLE>%s</TITLE>"
    head_text2 = '''
<META http-equiv=Content-Type content="text/html; charset=gb2312">
</HEAD>
<body>
<DIV align=center><FONT size=3>
    '''
    head_text3 = '<B>%s</B>'
    head_text4 = '''
<BR><BR></FONT></DIV>
<DIV align=center><TABLE width="30%"><TR><TD><h4>
    '''
    tail_text = '''
</h4></TD></TR></TABLE></DIV></body>
    '''
    list = os.listdir(dir)
    list.sort(key=sort_key)
    #print(list)
    with open(out_file,'w') as f:
        f.write(head_text1  % (title))
        f.write(head_text2)
        f.write(head_text3 % (title))
        f.write(head_text4)
        for i in list:
            f.write("<a href='%s/%s'>%s</br>" % (dir,i,i))
        f.write(tail_text)

def sort_key(s):
    #sort_strings_with_embedded_numbers
    re_digits = re.compile(r'(\d+)')
    pieces = re_digits.split(s)  # 切成数字与非数字
    pieces[1::2] = map(int, pieces[1::2])  # 将数字部分转成整数
    return pieces

def main():
    os.chdir("./")
    dir = "./" #相对路径
    Generate_menu(dir)

if __name__ == '__main__':
    main()