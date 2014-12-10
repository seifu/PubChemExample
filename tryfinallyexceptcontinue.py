for i in range(5):
    try:
        i/0
        print ("in try")
    except Exception as et:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(et).__name__, et.args)
        print (message)
        
        continue
    finally:
        print ("in finally")
