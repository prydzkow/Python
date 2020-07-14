

persona_list = [{"name":"Peter",
                "chars":
                    ["male", 
                    "noosom"
                    ]
                },
                {"name":"Hannah",
                "chars":
                    ["female",
                    "osom"
                    ]
                }]
#print(persona_list)
name = input("Provide a name: ")
l = lambda t: t["name"]==name

result = filter(l, persona_list)
print(list(result)[0]["chars"][1])

