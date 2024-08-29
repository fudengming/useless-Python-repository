def wife():
    while True:
        try:
            your_wife_age_input=input("你老婆的年纪:")
            your_wife_age=float(your_wife_age_input)
        except:
            print("你确定你输的是年纪？")
            print("回去重输！")
        else:
            print(your_wife_age_input+"岁...？你老婆命真长..." if your_wife_age>=100 else "行吧，没啥问题..." if your_wife_age>=18.0 else "变态！坐牢去吧！" if your_wife_age>0 else "你老婆还没出生？")
            break
def man():
    print("我靠哥们，你男同啊？")
    print("咳咳，不过测试还得继续...")
    wife_or_husband=str(input("敢问你对象是老公还是老婆？(怎么怪怪的...):"))
    wife_husband_test(wife_or_husband)
def wife_husband_test(wife_or_husband):
    wife() if wife_or_husband=="老婆" else husband() if wife_or_husband=="老公" else wife_husband_err()
def wife_husband_err():
    print("你输了个什么玩意？看不懂诶...")
    print("给我滚回去重输！")
    wife_or_husband=str(input("你对象是老公还是老婆？:"))
    wife_husband_test(wife_or_husband)
def woman():
    print("我靠，你女同啊？")
    print("咳咳，不过测试还得继续...")
    wife_or_husband=str(input("敢问你对象是老公还是老婆？(怎么怪怪的...):"))
    wife_husband_test(wife_or_husband)
def husband():
    while True:
        try:
            your_husband_age_input=input("你老公的年纪:")
            your_husband_age=float(your_husband_age_input)
        except:
            print("你确定你输的是年纪？")
            print("回去重输！")
        else:
            print(your_husband_age_input+"岁...？你老公命真长..." if your_husband_age>=100 else "行吧，没啥问题..." if your_husband_age>=18.0 else "我靠？还没成年呢就结婚？" if your_husband_age>0 else "你老公还没出生？")
            break
def get_your_gender():
    your_gender=str(input("你的性别是:"))
    get_your_lover_gender("男") if your_gender=="男" else get_your_lover_gender("女") if your_gender=="女" else get_your_gender_err()
def get_your_gender_err():
    print("你输了个什么...")
    print("算了，看不懂，回去重输！")
    print("输入\"男\"或\"女\"才可以哦...")
    get_your_gender()
def get_your_lover_gender(gender):
    your_lover_gender=str(input("你恋人的性别是:"))
    gay(gender) if gender==your_lover_gender else wife() if your_lover_gender=="女" else husband() if your_lover_gender=="男" else get_your_lover_gender_err(gender)
def get_your_lover_gender_err(gender):
    print("你输了个什么...")
    print("算了，看不懂，回去重输！")
    print("输入\"男\"或\"女\"才可以哦...")
    get_your_lover_gender(gender)
def gay(gender):
    man() if gender=="男" else woman()
get_your_gender()