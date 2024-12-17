list2=[]
def inputs():
    print("enter 5 values:")
    for i in range(0,5):
        list2.append(int(input("enter value")))

def cal_profit(p_or_l):
    return (p_or_l - (p_or_l + int((0.2 * float(p_or_l)))))

inputs()
year_wise_p_or_l = list(map(cal_profit,list2))

#map(lambda x:)
print(year_wise_p_or_l)