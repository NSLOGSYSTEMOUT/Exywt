

# s = [1,"a", "b"]
# s1 =[1,"a", "b"]
# s1[0] = 2
# print(s)
# print(s1)


# s1 = [1, "a", "b"]
# s2 = s1.copy()
# print(s2)                  # [1, 'a', 'b']
# s2[0] = 2                 #不会对1产生影响
# print(s1)                   #[1, 'a', 'b']
# print(s2)                   #[2, 'a', 'b']

#浅拷贝    只拷贝第一层
# s = [[1,2], "a", "b"]
# s3 = s.copy()
# print(s3)                   #[[1, 2], 'a', 'b']
# s3[1]="change a"
# print(s3)                   #[[1, 2], 'change a', 'b']
# s3[0][1]=3                  #改变s3列表元素对s中的列表元素产生影响
# print(s3)                   #[[1, 3], 'change a', 'b']
# print(s)                    #[[1, 3], 'a', 'b']
# s[0]= 'd'
# print(s)                    #['d', 'a', 'b']
# print(s3)                   #[[1, 3], 'change a', 'b']

#深拷贝    克隆一份
import  copy
husband = ["man", 123, [10000,5000]]

wife = husband.copy()
wife[0] = "woman"
wife[1] = 124

husband[2][1] -= 1000
print(wife)

three = copy.deepcopy(husband)
# three = husband.copy()
three[0]= "twoman"
three[1]= 125
three[2][1] -= 1000

print(wife)             #['woman', 124, [10000, 4000]]
print(three)            #['twoman', 125, [10000, 3000]]
