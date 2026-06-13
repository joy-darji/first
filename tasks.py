techmicra = {
    "aiml":{
        "batch1":[{"name":"Aarav Sharma","age":22,"college":"SU"},
                  {"name":"Aditya Patel","age":23,"college":"GECM"},
                  {"name":"Vivaan Singh","age":21,"college":"GPG"},
                  {"name":"Ananya Gupta","age":24,"college":"PDPU"},
                  {"name":"Diya Reddy","age":22,"college":"SU"}],
        "batch2":[{"name":"Arjun Nair","age":23,"college":"GECM"},
                  {"name":"Ishaan Kumar","age":25,"college":"PDPU"},
                  {"name":"Sanya Malhotra","age":21,"college":"SU"},
                  {"name":"Rohan Desai","age":24,"college":"GPG"},
                  {"name":"Kavya Joshi","age":22,"college":"SU"}]
        },
    "da":{
        "batch1":[{"name":"Advik Kapoor","age":23,"college":"PDPU"},
                  {"name":"Sai Krishna","age":24,"college":"GECM"},
                  {"name":"Myra Verma","age":21,"college":"SU"},
                  {"name":"Dhruv Mehta","age":25,"college":"GPG"},
                  {"name":"Aadhya Iyer","age":22,"college":"PDPU"}],
        "batch2":[{"name":"Kabir Choudhary","age":23,"college":"SU"},
                  {"name":"Anvi Saxena","age":24,"college":"GECM"},
                  {"name":"Vihaan Bhat","age":21,"college":"GPG"},
                  {"name":"Pari Singh","age":25,"college":"PDPU"},
                  {"name":"Ayaan Khan","age":22,"college":"SU"}]
        },
    "django":{
        "batch1":[{"name":"Shaurya Kulkarni","age":23,"college":"GECM"},
                  {"name":"Avni Malhotra","age":24,"college":"PDPU"},
                  {"name":"Krishna Menon","age":21,"college":"SU"},
                  {"name":"Sara Ansari","age":25,"college":"GPG"},
                  {"name":"Reyansh Reddy","age":22,"college":"SU"}],
        "batch2":[{"name":"Prisha Jain","age":23,"college":"PDPU"},
                  {"name":"Aarush Pillai","age":24,"college":"GECM"},
                  {"name":"Anika Sen","age":21,"college":"GPG"},
                  {"name":"Yuvraj Singh","age":25,"college":"SU"},
                  {"name":"Ishita Das","age":22,"college":"PDPU"}]
        },
    "react":{
        "batch1":[{"name":"Samarth Rao","age":22,"college":"SU"},
                  {"name":"Riya Bajaj","age":23,"college":"GECM"},
                  {"name":"Rudra Shetty","age":24,"college":"GPG"},
                  {"name":"Aaradhya Ghosh","age":21,"college":"PDPU"},
                  {"name":"Vedant Thakur","age":25,"college":"SU"}],
        "batch2":[{"name":"Tanvi Agarwal","age":23,"college":"PDPU"},
                  {"name":"Shaan Mathur","age":24,"college":"GECM"},
                  {"name":"Aarohi Mishra","age":21,"college":"SU"},
                  {"name":"Kabir Das","age":25,"college":"GPG"},
                  {"name":"Anushka Paul","age":22,"college":"SU"}],
        "batch3":[{"name":"Ayaan Bose","age":23,"college":"GECM"},
                  {"name":"Trisha Barman","age":24,"college":"PDPU"},
                  {"name":"Shaurya Kaur","age":21,"college":"SU"},
                  {"name":"Sneha Rawat","age":25,"college":"GPG"},
                  {"name":"Ansh Tiwari","age":22,"college":"SU"}],
        "batch4":[{"name":"Kiara Malhotra","age":23,"college":"PDPU"},
                  {"name":"Kiaan Sinha","age":24,"college":"GECM"},
                  {"name":"Aarna Menon","age":21,"college":"GPG"},
                  {"name":"Vivaan Sharma","age":25,"college":"SU"},
                  {"name":"Tara Kapadia","age":22,"college":"PDPU"}],
        "batch5":[{"name":"Reyansh Nair","age":23,"college":"GECM"},
                  {"name":"Sia Pillai","age":24,"college":"PDPU"},
                  {"name":"Dhruv Bhatia","age":21,"college":"SU"},
                  {"name":"Nysa Reddy","age":25,"college":"GPG"},
                  {"name":"Arjun Deshmukh","age":22,"college":"SU"}],
        
        
        }
    
}

names = []

for "batch_1" & "batch_2" in techmicra["aiml"]:
    for student in techmicra["aiml"]["batch_1"]["batch_2"]:
        if student["age"] >= 22:
            names.append(student["name"])

print(names)