techmicra = {
    "aiml":{
        "batch_1":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},   
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}],

        "batch_2":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}]

    },
    "django":{"batch_1":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}],

        "batch_2":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}]
    },

    "react":{"batch_1":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}],

        "batch_2":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}]
    },

    "data_analystics":{"batch_1":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}],

        "batch_2":[{"name":"jay","age":20,"college":"su"},
                  {"name":"raj","age":20,"college":"su"},
                  {"name":"ayush","age":20,"college":"su"},
                  {"name":"nik","age":20,"college":"su"},
                  {"name":"ronny","age":20,"college":"su"}],

        "batch_3":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"}],

        "batch_4":[{"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"jay","age":20,"college":"su"},
                  {"name":"raj","age":21,"college":"ku"},
                  {"name":"jay","age":20,"college":"su"}]
    },              
    }


for student in techmicra["data_analystics"]["batch_2"]:
    print(student["name"])