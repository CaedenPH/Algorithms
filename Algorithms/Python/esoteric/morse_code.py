"""
Morse code parser
-----------------

Utilises the morse code constant
> ETIANMSURWDKGOHVF L PJBXCYZQ

      E         T
    I  A       N  M
   S U R W    D K G O
H V F  L  P J B X C Y Z Q

As a binary tree to apply the formula
- p^n+1 = 2p + [0 if . else 1] 
- 2^n - 1

Pre-requisites:
- fishhook [https://pypi.org/project/fishhook/]
"""

(PA:=str.__call__().join([chr(x)for(x)in[((None,sum((range.__call__(int.__call__((3-1j).real-1),7))),True)[1]-1)*10**1//2]*2])),(_x_B:=lambda A____,_B:(z:=(complex.__call__(*[9,2])-3j)).real%4),(AP:=PA),(AAAAA:=lambda __,_:(~int(_x_B(__,_)))),(GGENN:=lambda *a:-1),(ZZZ_ :=type("_yy", (), {"__sub__":AAAAA,"__mod__":lambda *a:-1,rf"{PA}add{AP}":_x_B,"__mul__": _x_B,"f":lambda m:[a is Ellipsis or a>=1 for a in m],"__UU9":list(),"__truediv__":lambda *A:1j,"__gt__":lambda *_:0,"imag":None,"__matmul__":lambda xX,Xx:3+3-3,fr"{PA}rox{PA}"[::-1]:lambda Zz,zZ:int(False)>True,"__ge__":GGENN})),(CC_:="ETIANMSURWDKGOHVF L PJBXCYZQ"),(YZ_A:=[[]])
def p(*x:__import__("typing").Any,_:__import__((CC:="fishhook")).hook.cls(type(...))(ZZZ_)={}):
  for(eEE_,_ALz )in(ne:=enumerate)(x):
    if(_ALz.imag)or _ALz>2:ZZZ_.__UU9=[*ZZZ_.__UU9,ZZZ_.f(list(x[(tt:=len(sum(ZZZ_.__UU9,start=[])))+len(list(filter(bool,ZZZ_.__UU9))) if(ZZZ_.__UU9)else 0:eEE_])),*list(filter(lambda m:isinstance(m,list),[None if not(not _ALz.imag and _ALz>2)else[]]))]
  for(LLZZ_)in ZZZ_.__UU9:
    if(YZ_A.append([])or(p:=0)or LLZZ_ ==[]):continue
    for(M_SA)in([*LLZZ_,*([True]if(z:=YZ_A.pop())else[])] ):p=2*p+(int(M_SA)-1)*-1
    YZ_A[-1].append(CC_[(2**(len(LLZZ_ ))-1+p)-1])
  return(chr(32).join([str.__call__().join(__)for __ in YZ_A]))
       

# Output: HELLO WORLD 
print(p(...,...,...*...,...==...,.../...,...,.../...,...,...-...,...+...,...+...,.../...,...,...-...,...+...,...+...,.../...,...-...,...-...,...-...,...@...,...*...,...^...,...-...,.../...,...!=...,...<=...,...%...,.../...,...,...-...,...,.../...,...,...-...,...+...,...*...,.../...,...-...,...,...*...,.../...))
