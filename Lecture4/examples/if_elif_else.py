


# Learning points
## Usage of boolean expressions
## Indentation

gems_of_iitb = ["Ajay","Akash","New Name", "Aryan","Ayan","Bharani","Chidhambaram","Gaurav","Sridhar","Karan","Karthikeya","Krishna","Madhav","Prithviraj","Shrey","Vanshil","Vinayak"]
while True:
    name = str(input())
    if name in ["Varun", "Harsh"]:
        print("Welcome home, "+name)
    elif name in gems_of_iitb:
        print("Hello {}!".format(name))
    else:
        print("Access denied!")