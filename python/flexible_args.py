def flex_arg(**kwargs):
    for key,value in kwargs.items():
        print(key+';'+value)

flex_arg(name="Kyaw",role="DataEngineer")