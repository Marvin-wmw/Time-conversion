#定义了一个列表，其中有12个元素，它们分别是以英语表示的12个月份
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#定义了一个列表，其中有31个元素，它们分别是1-31的英语序数词的最后两个字符
#该列表的头三个元素分别是st，nd，rd后面紧跟17个th
#接下来又是st，nd和rd，后面7个th最后是st
ending=["st","nd","rd"]+17*["th"]+["st","nd","rd"]+7*["th"]+["st"]
year=input("Enter year:")
month=input("Enter month(1-12):")
day=input("Enther day(1-31)")
m=months[int(month)-1]
d=day+ending[int(day)-1]
y=int(year)
print(m,d,y)