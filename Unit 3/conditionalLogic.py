def doorEntranceCode(userPin):
    pinCode = "get_this_money"
    if userPin == pinCode: 
        print("access granted. Door is unlocked")
    else:
        print("access denied. Door will remain locked")

doorEntranceCode("get_this_money")