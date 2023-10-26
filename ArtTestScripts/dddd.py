from utilites.utils import utills
import string
import random

file = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"
rows = utills.getRowCount(file, "Sheet1")
coloumns = utills.getColumnCount(file, "Sheet1")

def random_invoceGenerator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def random_BillGenerator(size=6, chars=string.ascii_uppercase + string.digits + ','):
    return ''.join(random.choice(chars) for x in range(size))


def random_BilloGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    # Generate a random index to insert commas
    comma_indices = random.sample(range(size), random.randint(0, size))
    # Initialize the generated string with no commas
    result = ''.join(random.choice(chars) for _ in range(size))
    # Insert commas at random positions
    for index in comma_indices:
        result = result[:index] + ',' + result[index:]
    return result

#Read data from excel
for r in range(9, 12):
    i = 0
    i = i - 1
    billCounts = utills.readData(file, "Sheet1", r, 2)
    lineitmscount = utills.readData(file, "Sheet1", r, 3)

    trnpmode = utills.readData(file, "Sheet1", r, 9)
    scacData = utills.readData(file, "Sheet1", r, 11).split(",")

    entfilltype = utills.readData(file, "Sheet1", r, 7)
    scacData2 = "MFUS"
    scacData3 = "tk"
    billofladdingNo2 = random_BillGenerator()
    uomData2 = "PKG"
    qtyyData2 = "50"

    #print(trnpmode)

    if trnpmode == 40:# or "11"
        print(scacData3)
    else:
        print(scacData2)

    # Bill Of lading
    # try:
    #     print(billCounts)
    #     billCounts = billCounts - 1
    #     for i in range(billCounts):
    #         print(billCounts)
    #     for val_SCAC, val_UOM, val_BL_QTY in zip(scacData, uomData, qtyyData):  # button #val_BL  billofladdingNo
    #         print(val_SCAC, val_UOM, val_BL_QTY, billofladdingNo)#, billofladdingNo
    #
    # except Exception as e:
    #     print(e)

