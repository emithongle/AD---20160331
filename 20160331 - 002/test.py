from libs.features import findMaxString, preprocess
from config import *

print(findMaxString("LePhi Thong . (+84) 91 883-0963", skip_chars=skip_punctuation))

print(findMaxString(",435/5 nguyen van cong, p 3, q.go vap", skip_chars=skip_punctuation))
print(findMaxString("+84)154547789", skip_chars=skip_punctuation))
print(findMaxString("dinh thi bich phuong", skip_chars=skip_punctuation))
print(findMaxString("81 duong 16, p. binh tri dong b, q.binh tan", skip_chars=skip_punctuation))
print(findMaxString("0909218877", skip_chars=skip_punctuation))
print(findMaxString("nguyen thi thanh thuy", skip_chars=skip_punctuation))
print(findMaxString("36/6b quang trung, p.10, q. go vap", skip_chars=skip_punctuation))
print(findMaxString("0958064086", skip_chars=skip_punctuation))
print(findMaxString("pham thi phuong", skip_chars=skip_punctuation))
print(findMaxString("d002 lo d chung cu kcn p.tay thanh", skip_chars=skip_punctuation))
print(findMaxString("0903030818", skip_chars=skip_punctuation))
print(findMaxString("huynh kim danh", skip_chars=skip_punctuation))

print(preprocess(" .# ,  LePhi Thong . (+84) 91 883-0963  ,"))