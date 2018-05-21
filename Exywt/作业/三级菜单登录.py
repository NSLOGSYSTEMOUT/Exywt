
menu = {

    "北京":{

        "朝阳":{
            "国贸":{

                "CICC":{},
                "HP":{},
                "银行":{},
                "CCTV":{},
            },

            "望京":{

                "陌陌":{},
                "奔驰":{},
                "360":{},

            },
            "三里屯":{

                "UYK":{},
                "apple":{},

            },
        },

        "昌平":{

            "沙河":{
                "lannanhai":{},
                "baozi":{},
            },
            "天通苑" :{
                "low":{},
                "upp":{},
            },

            "回龙观":{},
        },

        "海淀":{

            "五道口":{

                "谷歌":{},
                "网易":{},
                "搜狐":{},
                "kuaishou":{},
            },

            "中关村":{

                "youku":{},
                "aqiyi":{},
                "qichezhijia":{},
                "xindongfang":{},
                "tengxun":{},

            }
        },

    },

    "上海":{

        "浦东":{

            "陆家嘴":{

                "cicc":{},
                "高盛":{},
                "摩根":{},
            },

            "外滩":{},
        },
        "闵行":{},
        "静安":{},

    },

    "山东":{

        "济南":{

        },

        "青岛":{

        },

        "德州":{

            "乐陵":{

                "丁坞镇":{},
            },

            "平原":{},
        },

    },
}

#可以一层一层进入到 可返回上一层 可任意层退出

back_flag = False
exit_flag = False


while not  back_flag and not exit_flag:

    for key in  menu:
        print(key)

    choice = input(">> : ").strip()
    if choice == "q":
        exit_flag = True

    if choice in menu:

        while not back_flag and not exit_flag: #让程序停留在第二层

             for key2 in menu[choice]:
                print(key2)

             choice2 = input(">>:").strip()
             if choice2 == "b":
                 back_flag = True
             if choice2 == "q":
                 exit_flag = True

             if choice2 in menu[choice]:

                while not  back_flag and not exit_flag:

                    for key3 in menu[choice][choice2]:
                        print(key3)

                    choice3 = input(">>:").strip()
                    if choice3 == "b":
                        back_flag = True
                    if choice3 == "q":
                        exit_flag = True

                    if choice3 in menu[choice][choice2]:

                        while not back_flag and not exit_flag:

                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)

                            choice4 = input(">>:").strip()
                            print("last  level")

                            if choice4 == "b":
                                back_flag = True

                            if choice4 == "q":
                                exit_flag = True


                        else: back_flag = False
                else:
                    back_flag = False
        else:
            back_flag = False
















