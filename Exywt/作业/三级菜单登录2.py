

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


current_layer = menu
# parent_layer = menu   #只可以保存一次
parent_list = []

while True:

    for key in  current_layer:
        print(key)

    choice = input(">>:").strip()

    if len(choice) == 0 : continue

    if choice in current_layer:

        # parent_layer = current_layer;           #改之前相当于父层
        parent_list.append(current_layer)
        current_layer = current_layer[choice]   #改为子层


    elif choice == "b":

        # current_layer = parent_layer            #把子层改为父层

        if parent_list:
            current_layer = parent_list.pop()


    else:
        print("无此项...")

