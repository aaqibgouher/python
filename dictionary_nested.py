#nested dictionay
family = {
    "Danish" : {
        "full_name" : "Gouher Danish",
        "occupation" : "job",
        "mobile_no" : 7004247708,
        "sex" : "M"
    },

    "Nazish" : {
        "full_name" : "Nazish Fraz",
        "occupation" : "job",
        "mobile_no" : 7004247710,
        "sex" : "M"       
    },

    "Imrana" : {
        "full_name" : "Imrana Falaq",
        "occupation" : "house wife",
        "mobile_no" : 9123456788,
        "sex" : "F"          
    }
}

print(family)
print(family["Nazish"])
print(family["Imrana"]["occupation"])