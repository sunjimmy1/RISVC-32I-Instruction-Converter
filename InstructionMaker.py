import clipboard
print("Instructions should be entered in a human readable format\nRegister addresses should be prefaced with an \"x\"")

inp = str(input("Enter an instruction: "))
while(inp != ""):
    instrFields = inp.split()
    issue = False
    DtB = lambda x,y : ''.join(reversed( [str((x >> i) & 1) for i in range(y)]))
    rtype = lambda funct7, funct3 : funct7 + "_" + DtB(int(instrFields[3][1:]),5) + "_" + DtB(int(instrFields[2][1:]),5)+ "_" + funct3 + "_" + DtB(int(instrFields[1][1:]),5) + "_0110011"
    itype = lambda funct3 : DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_" + funct3 + "_" + DtB(int(instrFields[1][1:]), 5) + "_0010011"
    loadInstr = lambda funct3 : DtB(int(instrFields[3]), 12) + "_" + DtB(int(instrFields[2][1:]), 5) + "_" + funct3 + "_" + DtB(int(instrFields[1][1:]), 5) + "_0000011"
    def btype(funct3):
        imm = DtB(int(instrFields[3]), 12)
        return imm[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_" + funct3 + "_" + imm[7:] + "_1100011"
    def stype(funct3):
        imm = DtB(int(instrFields[3]), 12)
        return imm[0:7] + "_" + DtB(int(instrFields[2][1:]),5) + "_" + DtB(int(instrFields[1][1:]),5) + "_" + funct3 + "_" + imm[7:] + "_0100011"
    try:
        instrName = instrFields[0].casefold()
        if(instrName == "add"):
            IWord = rtype("0000000","000")
        elif(instrName == "sub"):
            IWord = IWord = rtype("0100000","000")
        elif(instrName == "sll"):
            IWord = rtype("0000000","001")
        elif(instrName == "slt"):
            IWord = rtype("0000000","010")
        elif(instrName == "sltu"):
            IWord = rtype("0000000","011")
        elif(instrName == "xor"):
            IWord = rtype("0000000","100")
        elif(instrName == "srl"):
            IWord = rtype("0000000","101")
        elif(instrName == "sra"):
            IWord = rtype("0100000","101")
        elif(instrName == "or"):
            IWord = rtype("0000000","110")
        elif(instrName == "and"):
            IWord = rtype("0000000","111")
        elif(instrName == "beq"):
            IWord = btype("000")
        elif(instrName == "bne"):
            IWord = btype("001")
        elif(instrName == "blt"):
            IWord = btype("100")
        elif(instrName == "bge"):
            IWord = btype("101")
        elif(instrName == "bltu"):
            IWord = btype("110")
        elif(instrName == "bgeu"):
            IWord = btype("111")
        elif(instrName == "lb"):
            IWord = loadInstr("000")
        elif(instrName == "lh"):
            IWord = loadInstr("001")
        elif(instrName == "lw"):
            IWord = loadInstr("010")
        elif(instrName == "lbu"):
            IWord = loadInstr("100")
        elif(instrName == "lhu"):
            IWord = loadInstr("101")
        elif(instrName == "sb"):
            IWord = stype("000")
        elif(instrName == "sh"):
            IWord = stype("001")
        elif(instrName == "sw"):
            IWord = stype("010")
        elif(instrName == "addi"):
            IWord = itype("000")
        elif(instrName == "slti"):
            IWord = itype("010")
        elif(instrName == "sltiu"):
            IWord = itype("011")
        elif(instrName == "xori"):
            IWord = itype("100")
        elif(instrName == "ori"):
            IWord = itype("110")
        elif(instrName == "andi"):
            IWord = itype("111")
        else:
            issue = True
            print("The instruction you entered is invalid or not supported.")
        if(not issue):
            outStr = "32'b" + IWord + "; //" + inp
            print("\n" + outStr + "\n")
            clipboard.copy(outStr)
    except:
        print("There was a problem with your input. Make sure it's formatted correctly")
    inp = str(input("Enter an instruction: "))
