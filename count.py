import sys
def counts(code):
    num_list = []
    num = ""
    number_sum = ""
    sum1 = 0
    sum2 = 0
    code_list = {"0":"48", "1":"49", "2":"50","3":"51","4":"52","5":"53","6":"54","7":"55","8":"56","9":"57","A":"65","B":"66", "C":"67", "D":"68","E":"69","F":"70","G":"71","H":"72","I":"73","J":"74","K":"75","L":"76","M":"77","N":"78","O":"79","P":"80", "Q":"81","R":"82", "S":"83","T":"84","U":"85", "V":"86", "W":"87", "X":"88","Y":"89", "Z":"90", "a":"97", "b":"98", "c":"99","d":"100","e":"101","f":"102", "g":"103", "h":"104", "i":"105","j":"106", "k":"107","l":"108","m":"109", "n":"110", "o":"111","p":"112","q":"113", "r":"114","s":"115","t":"116","u":"117", "v":"118","w":"119","x":"120","y":"121","z":"122"}
    # print(code_list)
    code_split = list(code)
    for x in code_split:
        num += x
    print(num)
    numbers = list(num)
    print(numbers)
    
    for m in numbers:
        number_sum += code_list[m]
    number_list = list(number_sum)

    print(number_sum)    
    for i in number_list[::2]:
        sum1 += int(i)*3
    for n in number_list[1::2]:
        sum2 += int(n)
    
    print(sum1+sum2)

counts("a4rh4FRbdq2")
