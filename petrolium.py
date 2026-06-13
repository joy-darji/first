petrolium = {
    "fueltype":["petrolium","diesel","cng","lpg"],

    "employee": {
        "details":[
                {"name": "rahul","age":25,"salary":20000  }, 
                 {"name": "krish","age":22,"salary":22000 },
                   {"name": "jay","age":23,"salary":21000 }
        ]
}
}
print(petrolium["employee"]["details"][-3]["salary"])