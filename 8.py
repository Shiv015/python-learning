print 'Enter today\'s date in the formate dd/mm/yyyy: '
date = raw_input()
dd,mm,yyyy = date.split('/')
mm1 = ['01','03','05','07','08','10','12']
mm2 = ['04','06','09','11']
mm3 = ['02']
if (yyyy%400==0 and mm in mm1 and dd <=30):
    dd=int(dd)+1
    print int(dd) + int(mm) + int(yyyy)
else:
    print 'hi'
