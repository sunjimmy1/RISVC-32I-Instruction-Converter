
print("Instructions should be entered in a human readable format\nRegister addresses should be prefaced with an \"x\"")

inp = str(input("Enter an instruction: "))
while(inp != ""):
    instrFields = inp.split()
    
    DtB = lambda x,y : ''.join(reversed( [str((x >> i) & 1) for i in range(y)]))
    
    instrName = instrFields[0].casefold()

    if(instrName == "add"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_000_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "sub"):
        IWord = "0100000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_000_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "sll"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_001_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "slt"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_010_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "sltu"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_011_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "xor"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_100_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "srl"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_101_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "sra"):
        IWord = "0100000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_101_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "sra"):
        IWord = "0100000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_101_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "or"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_110_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "and"):
        IWord = "0000000_" + DtB(int(instrFields[3][1:]),5) + "_"+ DtB(int(instrFields[2][1:]),5) + "_111_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    elif(instrName == "beq"):
        branch = DtB(int(instrFields[3]), 12)
        IWord = branch[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_000_" + branch[7:] + "_" + "1100011"
    elif(instrName == "bne"):
        branch = DtB(int(instrFields[3]), 12)
        IWord = branch[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_001_" + branch[7:] + "_" + "1100011"
    elif(instrName == "blt"):
        branch = DtB(int(instrFields[3]), 12)
        IWord = branch[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_100_" + branch[7:] + "_" + "1100011"
    elif(instrName == "bge"):
        branch = DtB(int(instrFields[3]), 12)
        IWord = branch[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_101_" + branch[7:] + "_" + "1100011"
    elif(instrName == "bltu"):
        branch = DtB(int(instrFields[3]), 12)
        IWord = branch[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_110_" + branch[7:] + "_" + "1100011"
    elif(instrName == "bgeu"):
        branch = DtB(int(instrFields[3]), 12)
        IWord = branch[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_111_" + branch[7:] + "_" + "1100011"
    elif(instrName == "lb"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_000_" + DtB(int(instrFields[1][1:]), 5) + "_0000011"
    elif(instrName == "lh"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_001_" + DtB(int(instrFields[1][1:]), 5) + "_0000011"
    elif(instrName == "lw"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_010_" + DtB(int(instrFields[1][1:]), 5) + "_0000011"
    elif(instrName == "lbu"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_100_" + DtB(int(instrFields[1][1:]), 5) + "_0000011"
    elif(instrName == "lhu"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_101_" + DtB(int(instrFields[1][1:]), 5) + "_0000011"
    elif(instrName == "sb"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_000_" + DtB(int(instrFields[1][1:]), 5) + "_0100011"
    elif(instrName == "sh"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_001_" + DtB(int(instrFields[1][1:]), 5) + "_0100011"
    elif(instrName == "sw"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_010_" + DtB(int(instrFields[1][1:]), 5) + "_0100011"
    elif(instrName == "addi"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_000_" + DtB(int(instrFields[1][1:]), 5) + "_0010011"
    elif(instrName == "slti"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_010_" + DtB(int(instrFields[1][1:]), 5) + "_0010011"
    elif(instrName == "sltiu"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_011_" + DtB(int(instrFields[1][1:]), 5) + "_0010011"
    elif(instrName == "xori"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_100_" + DtB(int(instrFields[1][1:]), 5) + "_0010011"
    elif(instrName == "ori"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_110_" + DtB(int(instrFields[1][1:]), 5) + "_0010011"
    elif(instrName == "andi"):
        IWord = DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_111_" + DtB(int(instrFields[1][1:]), 5) + "_0010011"
    print(IWord + "; //" + inp)
    inp = str(input("Enter an instruction: "))
