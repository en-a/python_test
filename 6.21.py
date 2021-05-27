#トランプ強弱勝負

import random
import datetime

#開始時刻
dt_start = datetime.datetime.now()

mlist=["♥","♦","♠","♣"]

klist=[[1,2,3],[4,5,6],
       [7,8,9],[10,11,12],
       [13,"Joker" ,"白紙"]]   #多元化リスト使用

m=0 #自分の初期ポイント
c=0 #相手の初期ポイント

print("　♥♦♠♣ カードゲームをはじめましょう ♥♦♠♣")

while c<10 and m<10:    

    ans=input("---カードをひきますか?(y/n)---")

    if ans=="n":
        print("\n"+"---ゲームが中断されたよ---")
        break
    
    ans=="y"
        
#自分の手を表示
    mi=random.randint(0,4)
    mj=random.randint(0,2)
    mmark=random.choice(mlist)

    if klist[mi][mj]=="白紙":
        print("あなたのカードは",klist[mi][mj])
    elif klist[mi][mj]=="Joker":
        print("あなたのカードは",klist[mi][mj])
    else:
        print("あなたのカードは",mmark,klist[mi][mj])
        
#相手の手を表示
    ci=random.randint(0,4)
    cj=random.randint(0,2)
    cmark=random.choice(mlist)

    if klist[ci][cj]=="白紙":
        print("相手のカードは",klist[ci][cj])
    elif klist[ci][cj]=="Joker":
        print("相手のカードは",klist[ci][cj])
    else:
        print("相手のカードは",cmark,klist[ci][cj])

#ポイントシステム
    if klist[mi][mj]=="白紙" or klist[ci][cj]=="白紙" :
        print("ドロー")
        print("あなたのポイントは",m, "相手のポイントは",c)  
    elif klist[mi][mj]==klist[ci][cj]:
        print("ドロー")
        print("あなたのポイントは",m, "相手のポイントは",c)  
    elif klist[mi][mj]=="Joker":
            m=m+c                 #数値計算
            c=0                       
            print("Jokerがでたよ！相手のポイントを奪おう！")
            print("あなたのポイントは",m, "相手のポイントは",c) 
    elif klist[ci][cj]=="Joker":
        c=c+m
        m=0
        print("Jokerがでたよ！相手のポイントを奪おう！")
        print("あなたのポイントは",m, "相手のポイントは",c)      
    elif cmark=="♠" and klist[ci][cj]==1:
        c=c+3
        print("☆★スペードのエースが出たよ！プラス3点★☆")
        print("あなたのポイントは",m, "相手のポイントは",c) 
    elif mmark=="♠" and klist[mi][mj]==1:
        m=m+3
        print("☆★スペードのエースが出たよ！プラス3点★☆")
        print("あなたのポイントは",m, "相手のポイントは",c)   
    elif klist[mi][mj]>klist[ci][cj]: 
        m=m+1
        print("あなたの勝ち！")
        print("あなたのポイントは",m, "相手のポイントは",c)  
    elif klist[ci][cj]>klist[mi][mj]: 
        c=c+1
        print("相手の勝ち！")
        print("あなたのポイントは",m, "相手のポイントは",c) 
 
else:
    print("finish")
    
#終了時刻
dt_end = datetime.datetime.now()

time=dt_end-dt_start        #数値計算

#ファイル出力
x=str(time)
y=str(dt_start)
z=str(dt_end)

f=open("time.txt","a")
f.write("ゲーム開始時刻　"+y+"\n"+"ゲーム終了時刻　"+z+"\n"+"～プレイ時間は "+x+"です～"+"\n"+"\n")
f.close()

#ゲーム終了時
if m>=10:
    print("---終了---")
    print("10ポイントに到達！あなたの勝利です！")  
    print("\n"+"--------------------------------------")
    print("→　→　ファイル　time.txt　にプレイ時間が記録されているよ")    
if c>=10 :
    print("---終了---")
    print("相手が合計10ポイントに到達！相手の勝利です")
    print("\n"+"--------------------------------------")
    print("→　→　ファイル　time.txt　でプレイ時間が記録されているよ→→")  
