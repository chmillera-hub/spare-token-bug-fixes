# Shows how Python's compiler handles the value being matched (run on Python 3.13 or 3.14)
import dis, sys
print("Python", sys.version.split()[0])
src = '''
def f(x):
    match x:
        case 1 | 0:
            return "hit"
    return "miss"
'''
ns = {}; exec(src, ns)
for ins in dis.get_instructions(ns["f"]):
    if ins.opname in ("COPY", "LOAD_CONST", "LOAD_SMALL_INT", "COMPARE_OP", "POP_JUMP_IF_FALSE", "POP_TOP", "LOAD_FAST", "TO_BOOL"):
        print(f"{ins.offset:4} {ins.opname:20} {ins.argrepr:12} stack change {dis.stack_effect(ins.opcode, ins.arg if ins.opcode >= dis.HAVE_ARGUMENT else None):+d}")
call = [i for i in dis.get_instructions(compile("Logic(1)", "<s>", "eval")) if i.opname == "CALL"][0]
print("CALL with 1 argument: stack change", dis.stack_effect(call.opcode, call.arg), "(removes the function slot and the extra slot and 1 argument and leaves 1 result)")
