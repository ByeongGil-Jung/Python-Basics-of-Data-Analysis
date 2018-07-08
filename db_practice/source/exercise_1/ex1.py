import Dao as d

"""
 Created by IntelliJ IDEA.
 Project: source
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-08
 Time: 오후 6:20
"""


def ex1():
    # Singleton instance
    dao = d.Dao()

    print("\n( Basic data )\n")
    pcs = dao.pc_list()
    for pc in pcs:
        print("Model : {}, Speed : {}, Ram : {}, HD : {}, CD : {}, Price : {}"
              .format(pc.model, pc.speed, pc.ram, pc.hd, pc.cd, pc.price))

    print("\n - Insert a data\n")
    dao.pc_insert(9999, 999, 99, 9.9, "9x", 9999)

    print("\n( After inserting data )\n")
    pcs = dao.pc_list()
    for pc in pcs:
        print("Model : {}, Speed : {}, Ram : {}, HD : {}, CD : {}, Price : {}"
              .format(pc.model, pc.speed, pc.ram, pc.hd, pc.cd, pc.price))

    print("\n - Delete the data\n")
    dao.pc_delete("9999")

    print("\n( After deleting data )\n")
    pcs = dao.pc_list()
    for pc in pcs:
        print("Model : {}, Speed : {}, Ram : {}, HD : {}, CD : {}, Price : {}"
              .format(pc.model, pc.speed, pc.ram, pc.hd, pc.cd, pc.price))
