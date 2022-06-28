#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#匯入第三方套件
import os
import csv
import sys
import pic
import time
import random
import pandas as pd
import tkinter as tk
from PIL import Image
from tabulate import tabulate
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#定義自訂函數功能checkcheck()
def checkcheck(p):
    try:
        int(p)
        if 0<int(p)<65:
            result=True
        else:
            result=False
    except:
        result=False
    finally:
        return result
#定義自訂函數功能button_event1() - button_event7()
def button_event1():
    global num1
    num1=mybutton1['text']=random.randint(1,2)
def button_event2():
    global num2
    num2=mybutton2['text']=random.randint(1,2)
def button_event3():
    global num3
    num3=mybutton3['text']=random.randint(1,2)
def button_event4():
    global num4
    num4=mybutton4['text']=random.randint(1,2)
def button_event5():
    global num5
    num5=mybutton5['text']=random.randint(1,2)
def button_event6():
    global num6
    num6=mybutton6['text']=random.randint(1,2)
def button_event7():
    global num7
    num7=mybutton7['text']=random.randint(1,6)

#建立主選單，詢問使用者欲使用哪項功能(運用迴圈檢查使用者是否輸入適當的回覆)
manu=''
while manu!=0:
    print('\n\n您好！歡迎來到puipui卜卦列車，這裡是列車大廳，本列車共三種車廂可供您選擇：')
    print('A: 窺探天機列車')
    print('B: 百科全書列車')
    print('C: 知識學堂列車')
    print('0: 按下車鈴')
    car=input('請輸入您想乘坐的車廂：')

    #選擇A即進入第一功能:卜卦，列印情境
    if car=='A':
        print('\n歡迎來到窺探天機列車，此地可讓您進行卜卦，詢問運勢、愛情、考試與求職四大面向問題。\n\n注意事項：\n1. 一事不二問。〔也不可以同一件事用不同問法重覆問，這是褻瀆〕\n2. 誠心冥想你的問題，心唸某某某因何事問卦...。\n3. 卜卦是與自己以及天地的交流對話，不是要讓人迷信、推卸責任。卜問者要有理性及自我負責的心態，不要期待它可以告訴你所有未知之事，卜卦不準是常有的事。\n\n進行方式：\n1. 閱讀完上述注意事項後，請輸入您想詢問的問題面向。\n2. 請將卜卦按鈕視窗依序點擊，直至所有按鈕皆出現阿拉伯數字。\n3. 點擊完畢後，請將按鈕視窗關閉，回到程式進行。\n\n以上，請誠心地開始詢問吧！')
        time.sleep(3)

    #詢問使用者欲查詢面向(運用迴圈檢查使用者是否輸入適當的回覆)
        ask_in=0
        while ask_in==0:
            ask_in=input('\n今天您想窺探天機的內容是什麼呢？\n1.運勢  2.愛情  3.考試  4.求職 5.回到列車大廳 0.按下車鈴\n請輸入對應編號：')
            if ask_in=='1'or ask_in=='2' or ask_in=='3'or ask_in=='4':
                if ask_in=='1':
                    ask='運勢'
                elif ask_in=='2':
                    ask='愛情'
                elif ask_in=='3':
                    ask='考試'
                elif ask_in=='4':
                    ask='求職'

            #設定按鈕buttom以及視窗
                root = tk.Tk()
                root.title('易經卜卦')
                root.geometry('300x200')
                mybutton1 = tk.Button(root, text='第一爻', command=button_event1)
                mybutton2 = tk.Button(root, text='第二爻', command=button_event2)
                mybutton3 = tk.Button(root, text='第三爻', command=button_event3)
                mybutton4 = tk.Button(root, text='第四爻', command=button_event4)
                mybutton5 = tk.Button(root, text='第五爻', command=button_event5)
                mybutton6 = tk.Button(root, text='第六爻', command=button_event6)
                mybutton7 = tk.Button(root, text='關鍵爻', command=button_event7)
                mybutton1.pack()
                mybutton2.pack()
                mybutton3.pack()
                mybutton4.pack()
                mybutton5.pack()
                mybutton6.pack()
                mybutton7.pack()

                #呼叫視窗
                root.mainloop()

                #將產生之數字組合為卜卦結果
                song=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)
                yau=str(num7)+str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)
                print('\n\n\n... 結果輸出中，心誠則靈...')
                time.sleep(3) 

                #開啟卦辭檔案，並根據卜卦結果找尋相對應資料
                with open('data/占卜資料庫(卦辭).csv','r', encoding='UTF-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['辨識碼']==song:
                            #運用tabulate()將卦辭資料以表格呈現
                            table_data=[["您的卦序為",row['卦序']],["卦名為  ",row['卦名']],["組成：",row['組成']],["卦名白話翻譯：",row['卦名白話翻譯']]]
                            table_header=["卍煞氣PUIPUI卍","卜卦結果"]

                            print(tabulate(table_data, headers=table_header, tablefmt='grid'))

                            table_data=[['卦辭：'+row['卦辭']],['卦辭白話解釋：'+row['卦辭白話解釋']],['建議：'+row['建議']],["卦名白話翻譯："+row['卦名白話翻譯']],[ask+'：'+row[ask]]]
                            table_header=['卦名解釋：'+row['卦名解釋']]

                            print(tabulate(table_data, headers=table_header, tablefmt='grid'))

            #開啟爻辭檔案，並根據卜卦結果找尋相對應資料
                with open('data/占卜資料庫(爻辭).csv','r', encoding='UTF-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['辨識碼']==yau:
                            #運用tabulate()將爻辭資料以表格呈現
                            table_data=[['白話解析：'+row['白話解析']]]
                            table_header=['爻辭：'+row['爻辭']]

                            print(tabulate(table_data, headers=table_header, tablefmt='rst'))

            #開啟卦辭檔案，並根據卜卦結果找尋相對卦象(圖片) 
                with open('data/占卜資料庫(卦辭).csv','r', encoding='UTF-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['辨識碼']==song:
                            #呈現卦象圖片
                            img=Image.open('gua_image/'+row['卦序']+'.png')
                            plt.figure("卦序")
                            plt.imshow(img)
                            plt.show()

            #第一功能結束，詢問使用者欲進行之下一步
                print("\n\n\n功能選單:")
                print('0:按下車鈴')
                print('1:回到列車大廳')
                print('2:重新窺探天機')
                re1=''
                while re1!='0':
                    re1=input('請問您接下來有什麼需要：')
                    if re1=='0':
                        print("\n歡迎您下次光臨，下車小心！")
                        sys.exit()
                    elif re1=='1':
                        print('\n'*3)
                        break
                        ask_in=1
                        manu=''
                    elif re1=='2':
                        re1='0'
                        ask_in=0
                    else:
                        print('\n亂輸入小心走路踩到樂高！請重新輸入：')
                        re1=''
            elif ask_in=='5':
                manu=''
            elif ask_in=='0':
                print("\n歡迎您下次光臨，下車小心！")
                sys.exit()
            else:
                print('\n亂輸入小心被雷公打屁屁！請重新輸入：')
                ask_in=0

    #選擇B即進入第二功能:查詢各卦資料，列印圖片     
    elif car=='B':
        item=''
        while item!=0:
            print('\n\n哈囉！歡迎大家來到百科全書列車，對64卦中哪一個卦有興趣呢？這裡的資料開放讓您查詢，應有盡有！64卦列表如下：\n')
            table = PrettyTable(['☯','六十四卦','參考表格','：']) #印出表格讓使用者只用卦序(數字)查詢
            table.add_row([' 1. 乾為天　',' 2. 坤為地　',' 3. 水雷屯　',' 4. 山水蒙　'])
            table.add_row([' 5. 水天需　',' 6. 天水訟　',' 7. 地水師　',' 8. 水地比　'])
            table.add_row([' 9. 風天小畜','10. 天澤履 ','11. 地天泰 ','12. 天地否 '])
            table.add_row(['13. 天火同人','14. 火天大有','15. 地山謙 ','16. 雷地豫 '])
            table.add_row(['17. 澤雷隨 ','18. 山風蠱 ','19. 地澤臨 ','20. 風地觀 '])
            table.add_row(['21. 火雷噬嗑','22. 山火賁 ','23. 山地剝 ','24. 地雷復 '])
            table.add_row(['25. 天雷無妄','26. 山天大畜','27. 山雷頤 ','28. 澤風大過'])
            table.add_row(['29. 坎為水 ','30. 離為火 ','31. 澤山咸 ','32. 雷風恆 '])
            table.add_row(['33. 天山遯 ','34. 雷天大壯','35. 火地晉 ','36. 地火明夷'])
            table.add_row(['37. 風火家人','38. 火澤睽 ','39. 水山蹇 ','40. 雷水解 '])
            table.add_row(['41. 山澤損 ','42. 風雷益 ','43. 澤天夬 ','44. 天風姤 '])
            table.add_row(['45. 澤地萃 ','46. 地風升 ','47. 澤水困 ','48. 水風井 '])
            table.add_row(['49. 澤火革 ','50. 火風鼎 ','51. 震為雷 ','52. 艮為山 '])
            table.add_row(['53. 風山漸 ','54. 雷澤歸妹','55. 雷火豐 ','56. 火山旅 '])
            table.add_row(['57. 巽為風 ','58. 兌為澤 ','59. 風水渙 ','60. 水澤節 '])
            table.add_row(['61. 風澤中孚','62. 雷山小過','63. 水火既濟','64. 火水未濟'])
            print(table)
            print('65：回到列車大廳')
            print('0：按下車鈴')
            print('\n')
            data1 = pd.read_csv('data/占卜資料庫(卦辭)2.csv',encoding='utf-8') #讀取檔案 記得取目標檔案路徑
            data2 = pd.read_csv('data/占卜資料庫(爻辭)2.csv',encoding='utf-8') #讀取檔案 記得取目標檔案路徑

            item=input('請輸入欲查詢的卦序(數字)：') #詢問使用者欲查詢的卦(運用迴圈檢查使用者是否輸入適當的回覆)
            if item=='0':
                print("\n歡迎您下次光臨，下車小心！")
                sys.exit()
            elif item=='65':
                break
            elif not checkcheck(item):
                print('亂輸入小心遇到一群會飛的蟑螂！請重新輸入：')
                continue
            else:
                nitem=int(item)
                table1 = PrettyTable(['第'+str(nitem)+'卦','組成：','白話翻譯：']) #印出表格讓使用者只用卦序(數字)查詢
                table1.add_row([data1.iloc[nitem-1,2]+'卦',data1.iloc[nitem-1,3],data1.iloc[nitem-1,4]])
                print(table1)

                table2 = PrettyTable(['卦名解釋']) #印出卦名解釋
                table2.add_row([data1.iloc[nitem-1,5]])
                print(table2)
                print('\n\n')

                table3a = PrettyTable(['卦辭']) #印出卦辭與白話解析
                table3a.add_row([data1.iloc[nitem-1,6]])
                table3b = PrettyTable(['卦辭白話解釋'])
                table3b.add_row([data1.iloc[nitem-1,7]])
                print(table3a)
                print(table3b)
                print('\n\n')


                for i in range(6*nitem-5,6*nitem+1): 

                    table4a = PrettyTable(['爻辭']) #印出爻辭與白話解析
                    table4a.add_row([data2.iloc[i-1,3]])
                    table4b = PrettyTable(['爻辭白話解析'])
                    table4b.add_row([data2.iloc[i-1,4]])
                    print(table4a)
                    print(table4b)
                    print('\n\n')

                table5 = PrettyTable(['建議']) #印出建議
                table5.add_row([data1.iloc[nitem-1,8]])
                print(table5)
                print('\n\n')

                table6 = PrettyTable(['運勢']) #印出運勢
                table6.add_row([data1.iloc[nitem-1,9]])
                print(table6)

                table7 = PrettyTable(['愛情']) #印出愛情
                table7.add_row([data1.iloc[nitem-1,10]])
                print(table7)

                table8 = PrettyTable(['考試']) #印出考試
                table8.add_row([data1.iloc[nitem-1,11]])
                print(table8)

                table9 = PrettyTable(['求職']) #印出求職
                table9.add_row([data1.iloc[nitem-1,12]])
                print(table9)
                img=Image.open('gua_image/'+str(nitem)+'.png')
                plt.figure("卦序")
                plt.imshow(img)
                plt.show()
                print("\n\n\n功能選單:")  #第二功能結束，詢問使用者欲進行之下一步
                print('0:按下車鈴')
                print('1:回到列車大廳')
                print('2:重新查詢百科全書')
                re2=''
                while re2!=0:
                    re2=input('請問您接下來有什麼需要：') 
                    if re2=='0':
                        print("\n歡迎您下次光臨，下車小心！")
                        sys.exit()
                    elif re2=='1':
                        print('\n'*3)
                        re2=0
                        item=0
                        manu=''
                    elif re2=='2':
                        re2=0
                        item='' 
                    else:
                        print('\n亂輸入小心被蚊子叮到全身都是！請重新輸入：')



        #選擇C即進入第三功能:卜卦小學堂
    elif car=='C':
        #卜卦小學堂-介紹#
        print("\n\n歡迎各位來到知識學堂列車")
        print("在這裡，各位可以透過主題選擇了解各式各樣的卜卦小知識")
        print("希望在經過我們的介紹之後，大家都能對卜卦及易經有所認識")
        print("甚至參加我們所舉辦的小測驗，成為本屆天竺鼠車車盃的卜卦知識王！")
        print("那接著就讓我們開始進行今天的課程吧！")
        print("Let's GO!\n")
        print("今天的介紹將分為以下7大主題：")
        i1=1
        i2=1
        i3=1
        i4=1
        i5=1
        i6=1
        i7=1
        num=1
        while num>0:
            print("\n1. 易經的歷史發展與組成")
            print("2. 周易陰陽概念的形成")
            print("3. 八卦")
            print("4. 六十四卦")
            print("5. 卦辭與爻辭")
            print("6. 卦的組成規則與意義")
            print("7. 卜卦方式")
            print("8. 參加天竺鼠車車盃知識大考驗！")
            print("9. 回到列車大廳")
            print("0. 按下車鈴\n")
            func1=input("請輸入想了解的主題：")  #詢問使用者欲了解的主題(運用條件判斷檢查使用者是否輸入適當的回覆)
            if func1=='0':
                print("歡迎您下次光臨，下車小心！")
                sys.exit()

            #選擇1即印出易經的歷史發展與組成內容   
            elif func1=='1':
                print("\n\n\n《易經》的核心結構，就是64個卦符，64個卦辭，和64組爻辭。")
                print("這是起初的《易經》，它是商、周之際（西元前11世紀左右）")
                print("在漫長的時間裡，在一次次占卜實作中")
                print("經過前前後後許多卜者的共同參與，所逐漸完成的")
                print("為了明確區隔，有人把這部份稱作「周易古經」。")
                print("歷史上，第一波對周易古經的正式解釋，出現在戰國時期（西元前5～3世紀）")
                print("距離卦爻辭產生的時代至少七、八百年")
                print("它有七種，共十篇，稱作《十翼》（十篇輔助材料，英譯叫Ten Wings），又稱《易傳》")
                print("周易古經加上它們，才是今天所謂《易經》的全部。")
                i1-=1
                if i1==0:
                    num+=1
                    print("\n您目前已經完成",num-1,"個課程\n")
                else:
                    num=num


            #選擇2即印出周易陰陽概念的形成內容
            elif func1=='2':
                print("\n\n\n後代易學裡非常根本非常重要的「陰」、「陽」的概念，其實不是一開始就出現的。")
                print("《周易古經》的形成所根據的，可能只是兩個非常素樸的、簡單的概念。")
                print("其中一個約略是「男性」、「太陽」")
                print("以及「開闊完整的天空，太陽高居其中，推動、宰制著整個世界」的概念")
                print("（後來逐漸演變、提升、凝聚為「陽」的概念）")
                print("另一個大致是「女性」、「月亮」")
                print("以及「具體實在的大地，蘊涵豐富資源，內容複雜多樣」的概念")
                print("（後來逐漸演變、提升、凝聚為「陰」的概念）")
                print("上面這兩個素樸的概念，可以用簡化的圖案、符號來表示。")
                print("簡化到了二維的話可以是「○」與「⊕」，或更加簡化的「○」與「Θ」。")
                print("然後再進一步簡化為一維，就可以是「─」和「- -」了。")
                i2-=1
                if i2==0:
                    num+=1
                    print("\n您目前已經完成",num-1,"個課程\n")
                else:
                    num=num
            #選擇3即印出八卦內容        
            elif func1=='3':
                print("\n\n\n將陰和陽兩個符號任意重疊為三層（稱作三個「爻」），可以得到八個不同的符號。")
                print("用類似造字六書中「會意」的方法來解讀這三個爻，賦予特殊意義")
                print("這就產生了《易經》的八個基本卦，也就是所謂的「八卦」。\n")
                print("天（乾）：天加上天，三重的天還是天")
                print("地（坤）：地加上地，三重的地還是地")
                print("火（離）：可以想像成一個火把，中間陰爻是木頭，上下兩個陽爻是火焰")
                print("水（坎）：這是河流。中間陽爻是流水，上下兩個陰爻是兩岸")
                print("澤（兌）：這是沼澤，最上面是澤岸，兩個陽爻是澤面，而下方的澤岸省略")
                print("風（巽）：這本來是平原。不過平原上的風最是順暢，所以用平原來表示風")
                print("山（艮）：上面三分之一是天空，底下三分之二是土地，這是山")
                print("雷（震）：地底下有個陽爻，這是雷（錢穆說，古人以為雷從地底下打出來）")
                pic.eig('八卦')
                i3-=1
                if i3==0:
                    num+=1
                    print("\n您目前已經完成",num-1,"個課程\n")
                else:
                    num=num

            #選擇4即印出六十四卦內容
            elif func1=='4':
                print("\n\n\n將八個基本卦兩兩相重，就變成64個六爻的卦")
                print("（因此各卦的上三爻、下三爻又稱作上卦、下卦）")
                print("64卦中各卦的主題，通常是上下卦卦象會意的結果。")
                print("（天、地、雷……等基本象徵，或它們的引申，如「水」引申為「雲」、「泉」等）")
                print("例如「山／水（山腳的水流比較混濁，或山下有水則草木繁茂而有所遮蔽）」表示「蒙昧」（蒙卦）")
                print("「水／地（地面上的水）」表示「貼附、親附」（比卦）")
                print("「天／火（夜空下有火光）」表示「集結人群」（同人卦）")
                print("「地／火（光明被地面遮蔽）」表示「光明受到損傷」（明夷卦）等等")
                print("這都是先民根據人生經驗想像、構作出來的。")
                print("只不過，有些卦到底根據什麼線索會意出來，今天已經不容易確知了")
                i4-=1
                if i4==0:
                    num+=1
                    print("\n您目前已經完成",num-1,"個課程\n")
                else:
                    num=num

            #選擇5即印出卦辭和爻辭內容
            elif func1=='5':
                print("\n\n\n初期的卜卦可能只是卜出某一個卦而已。")
                print("卜者在每次占卜時，根據人生經驗來解釋所卜出的卦，記下來就是卦辭了。")
                print("有時候，也會把占卜時跟所提問題相關的人、事、物一起記下來，讓它們都成為卦辭的一部份。")
                print("64卦總共64組訊息，每次卜得其中之一，這裡頭可以選擇的訊息太少了。")
                print("於是卜卦進一步發展，就是將每個卦再展開為六個可能的情境，逐一加上爻辭。")
                print("（六倍的訊息量大致適合，又剛好跟六個爻畫相呼應）")
                print("到這個時候，周易古經就算完成了。")
                print("於是訊息量增加到386個")
                print("（每卦6個爻辭，總共384個爻辭，再加上乾卦的「用九」和坤卦的卦的「用六」）")
                print("每次卜卦可以卜出「某一個卦的某一個爻」，卜卦就變得更豐富也更細密了。")
                print("到這個時候，原有的卦辭不再是解讀、思考的焦點")
                print("但它仍然是所卜得的答案（某個爻）的背景，仍然具有參考的意義。")
                i5-=1
                if i5==0:
                    num+=1
                    print("\n您目前已經完成",num-1,"個課程\n")
                else:
                    num=num

            #選擇6即印出卦的組成規則與意義內容
            elif func1=='6':
                print("\n\n\n一、每卦六個爻，下三爻是下卦，上三爻是上卦。")
                print("    上、下卦卦象的功能，主要是藉由會意來產出該卦主題。")
                print("二、每卦六個爻，從下往上算（這點務必要注意要記得），分別稱作初、二、三、四、五、上。")
                print("    而陽爻用「九」表示，陰爻用「六」表示。")
                print("    要指稱、標示一個爻，必須同時包括爻位和陰陽兩方面。")
                print("    第一、六爻稱「初＊」、「上＊」（＊表示九或六，下同）")
                print("    第二到五爻則稱「＊二」、「＊三」……等")
                print("    舉例來說，「初九」表示第一爻和陽爻，「六二」表示第二爻和陰爻，而「九五」就表示第五爻和陽爻。")
                print("三、從第一到第六爻，常常意味著年齡、地位、事件、情勢等的逐步發展。")
                print("    就人來說，則其中第二爻常常意味著基層中稍具份量的人")
                print("    第五爻常常意味著主導的、最高的地位（所謂「九五之尊」）")
                print("    而第六爻常常意味著末尾的失誤與轉折、變化。")
                i6-=1
                if i6==0:
                    num+=1
                    print("\n您目前已經完成",num-1,"個課程\n")
                else:
                    num=num

            #選擇7即印出卜卦方式內容
            elif func1=='7':
                print("\n\n\n可利用擲骰子六次（奇數是陽，偶數是陰），搭配第七次擲出第幾爻。")
                print("也可以手握六個硬幣（其中一個做上記號），以適當力道將它們拋落地面")
                print("先根據硬幣的正反面（正面是陽，反面是陰）和位置（最近的是第一爻，最遠的是第六爻）")
                print("確定所得到的某一個卦的六個爻，再根據有記號的銅板的位置確定所得的是第幾爻。")
                print("卜問前先靜思，然後在心中默念或開口說出你的問題。")
                print("稱呼天為「老天爺」、「親愛的老天爺」、「上天」、「公正的上天」都可以。")
                print("使用日常的措詞、話語來訴說就行（就像請教智者、賢人那樣）。")
                print("所提的問題要單純清晰（可別像在問一個申論題那樣，這樣子老天很難回答你）")
                print("說完以後，就開始進行卜問。")
                print("根據你卜得的結果，將六個爻和關鍵爻（或者說焦點爻、答案爻）畫出來")
                print("從上下卦的會意來辨識它是什麼卦，或利用上下卦交叉檢索表找出卦名和序號。")
                print("然後根據序號在《易經》書中查到這個卦的卦爻辭。")
                print("只要找到關鍵爻的爻辭，從爻辭的的言說或譬喻來體會天意即可。")
                i7-=1
                if i7==0:
                    num+=1
                    print("\n您目前已經完成",num-1,"個課程\n")
                else:
                    num=num

            #選擇8即印出天竺鼠車車盃知識大考驗內容
            elif func1=='8':
                #卜卦小學堂-天竺鼠車車盃知識大考驗#
                print("\n\n\n歡迎來到一年好幾度，想什麼時候參加就什麼時候參加的天竺鼠車車盃-卜卦知識大考驗(？")
                print("在看完以上馬鈴薯為各位精(上)心(網)準(估)備(狗)的小知識後")
                print("相信各位對於中國卜卦都有一定程度的了解")
                print("於是接下來阿比將為各位準備一連串豐富又有趣的題目")
                print("考驗你是否具備足夠的資格成為卜卦大神\n")
                #請使用者輸入欲進行的動作，並用選擇結構檢查
                ready=1
                while not ready==0:
                    ready=input("\n你準備好了嗎？\n是（輸入1）\n再...再「在」等我一下...（輸入2）\n我...我下次再挑戰好了...（輸入3）\n：")
                    if ready=="1":
                        ans=0
                        qus=0
                        q1=1
                        while q1>0: #請使用者輸入選項內容，並用迴圈結構檢查（以下各題皆如此）
                            q1=input("\nQ1.請問《易經》最早的起源可以回溯到？\nA)車車鑽木取火的時候\nB)商、周時期\nC)唐宋文學盛世\nD)好啦，其實是我寫的啦哈哈，現代！\n你的回答是：")
                            if q1=="A":
                                print("答錯了，再想一下...\n")
                                q1=0
                                qus+=1
                                ans=ans
                            elif q1=="B":
                                print("恭喜答對！\n")
                                q1=0
                                qus+=1
                                ans+=1
                            elif q1=="C":
                                print("不對喔！下次再看仔細一點\n")
                                q1=0
                                qus+=1
                                ans=ans
                            elif q1=="D":
                                print("...\n")
                                q1=0
                                qus+=1
                                ans=ans
                            else:
                                print("輸入錯誤！請重新輸入答案！\n")
                                q1=1
                                qus=qus
                                ans=ans
                            print("您已完成",qus,"題，還剩下",7-qus,"題")  #計算並印出完成幾題（以下各題皆如此）

                        q2=1
                        while q2>0:
                            q2=input("Q2.《易經》「陰」、「陽」的概念最初是什麼以型態呈現？\nA)「男性」、「女性」\nB)「藍色」、「粉紅色」\nC)「年」、「月」\nD)「西羅摩」、「巧克力」\n你的回答是：")
                            if q2=="A":
                                print("恭喜答對！\n")
                                q2=0
                                qus+=1
                                ans+=1
                            elif q2=="B":
                                print("答錯了，再想一下...\n")
                                q2=0
                                qus+=1
                                ans=ans
                            elif q2=="C":
                                print("不對喔！下次再看仔細一點\n")
                                q2=0
                                qus+=1
                                ans=ans
                            elif q2=="D":
                                print("...\n")
                                q2=0
                                qus+=1
                                ans=ans
                            else:
                                print("輸入錯誤！請重新輸入答案！\n")
                                q2=1
                                qus=qus
                                ans=ans
                            print("您已完成",qus,"題，還剩下",7-qus,"題")

                        q3=1
                        while q3>0:
                            q3=input("Q3.請問八卦共有幾個基本卦呢？\nA)64\nB)2\nC)4\nD)8\n你的回答是：")
                            if q3=="A":
                                print("不對喔！等等可以再回去複習一下~\n")
                                q3=0
                                qus+=1
                                ans=ans
                            elif q3=="B":
                                print("答錯了，再接再勵\n")
                                q3=0
                                qus+=1
                                ans=ans
                            elif q3=="C":
                                print("不對喔！下次再看仔細一點\n")
                                q3=0
                                qus+=1
                                ans=ans
                            elif q3=="D":
                                print("恭喜答對！\n")
                                q3=0
                                qus+=1
                                ans+=1
                            else:
                                print("輸入錯誤！請重新輸入答案！\n")
                                q3=1
                                qus=qus
                                ans=ans
                            print("您已完成",qus,"題，還剩下",7-qus,"題")

                        q4=1
                        while q4>0:
                            q4=input("Q4.64卦是如何組成的呢？\nA)32X2\nB)16X4\nC)8X8\nD)日向寧次發明出來的\n你的回答是：")
                            if q4=="A":
                                print("不對喔！等等可以再回去複習一下~\n")
                                q4=0
                                qus+=1
                                ans=ans
                            elif q4=="B":
                                print("答錯了，再接再勵\n")
                                q4=0
                                qus+=1
                                ans=ans
                            elif q4=="C":
                                print("恭喜答對！\n")
                                q4=0
                                qus+=1
                                ans+=1
                            elif q4=="D":
                                print("是在哈囉？？？？\n")
                                q4=0
                                qus+=1
                                ans=ans
                            else:
                                print("輸入錯誤！請重新輸入答案！\n")
                                q4=1
                                qus=qus
                                ans=ans
                            print("您已完成",qus,"題，還剩下",7-qus,"題")

                        q5=1
                        while q5>0:
                            q5=input("Q5.64卦共可得64種訊息，但數量太少，於是後來擴增至多少種訊息？\nA)386\nB)1001\nC)沒有上限\nD)跟學妹沒有回你的訊息一樣多\n你的回答是：")
                            if q5=="A":
                                print("恭喜答對！\n")
                                q5=0
                                qus+=1
                                ans+=1
                            elif q5=="B":
                                print("答錯了，再接再勵\n")
                                q5=0
                                qus+=1
                                ans=ans
                            elif q5=="C":
                                print("不對喔！再複習一下~\n")
                                q5=0
                                qus+=1
                                ans=ans
                            elif q5=="D":
                                print("是在哈囉？？？？\n")
                                q5=0
                                qus+=1
                                ans=ans
                            else:
                                print("輸入錯誤！請重新輸入答案！\n")
                                q5=1
                                qus=qus
                                ans=ans
                            print("您已完成",qus,"題，還剩下",7-qus,"題")

                        q6=1
                        while q6>0:
                            q6=input("Q6.下列關於卜卦的敘述，何者正確？\nA)每卦六個爻，從下往上算\nB)每卦六個爻，上三爻是下卦，下三爻是上卦\nC)研究顯示，會卜卦者脫單機率較高\nD)我其實快要想不出有什麼選項了...\n你的回答是：")
                            if q6=="A":
                                print("恭喜答對！\n")
                                q6=0
                                qus+=1
                                ans+=1
                            elif q6=="B":
                                print("答錯了，再接再勵\n")
                                q6=0
                                qus+=1
                                ans=ans
                            elif q6=="C":
                                print("那你要不要去學一下：)\n")
                                q6=0
                                qus+=1
                                ans=ans
                            elif q6=="D":
                                print("對不起啦QQ\n")
                                q6=0
                                qus+=1
                                ans=ans
                            else:
                                print("輸入錯誤！請重新輸入答案！\n")
                                q6=1
                                qus=qus
                                ans=ans
                            print("您已完成",qus,"題，還剩下",7-qus,"題")

                        q7=1
                        while q7>0:
                            q7=input("Q7.卜問時注意事項何者錯誤？\nA)使用日常的措詞、話語來訴說就行\nB)所提的問題要單純清晰\nC)卜問前先靜思，然後在心中默念或開口說出你的問題\nD)向各方神明同時進行卜問效果較佳\n你的回答是：")
                            if q7=="A":
                                print("答錯！逋逋\n")
                                q7=0
                                qus+=1
                                ans=ans
                            elif q7=="B":
                                print("答錯！逋逋\n")
                                q7=0
                                qus+=1
                                ans=ans
                            elif q7=="C":
                                print("答錯！逋逋\n")
                                q7=0
                                qus+=1
                                ans=ans
                            elif q7=="D":
                                print("恭喜答對！\n")
                                q7=0
                                qus+=1
                                ans+=1
                            else:
                                print("輸入錯誤！請重新輸入答案！\n")
                                q7=1
                                qus=qus
                                ans=ans
                            print("您已完成",qus,"題，還剩下",7-qus,"題") #答題結果呈現 計算分數 印出相對印分數的圖
                        print("恭喜你完成所有測驗題")
                        print("在這次測驗的7個題目中，你總共答對",ans,"題")
                        if ans==0:
                            print("不行了皮諾可，這個直接電死")
                            pic.eig('皮諾可')
                        elif 1<=ans<=3:
                            print("表現不如預期，下去領紅蘿蔔吧")
                            pic.eig('紅蘿蔔')
                        elif 4<=ans<=6:
                            print("表現不錯，恭喜獲得主辦方所提供的金蘿蔔(非物理")
                            pic.eig('金蘿蔔')
                        elif ans==7:
                            print("你就是卜算界的宋仲基\n易經學裡的周子瑜\n恭喜獲得本次天竺鼠車車盃的卜算知識王\n快去跟親朋好友分享這份喜悅(這樣我們才不用找How哥業配")
                            pic.eig('冠軍')
                        print("\n將你送回剛剛的地方囉") 
                        break   #回到知識學堂列車的選單

                    elif ready=="2":
                        print("我不管，不開始我就咬你(by 泰迪\n我再問一次喔")
                        ready=1
                    elif ready=="3":
                        print("好吧...看來我們的緣分就到這了...")
                        print("\n將你送回剛剛的地方囉QQ") 
                        num=1
                        break
                    else:
                        print("\n亂輸入小心下一次上廁所沒有衛生紙！請重新輸入：")



            elif func1=='9':
                break
            else:
                print("\n亂輸入小心被做成中部粽！請重新輸入：")
                num=1



    #選擇0則結束程式   
    elif car=='0':
        print("\n\n歡迎您下次光臨，下車小心！")
        manu=0
    #條件判斷使用者是否輸入正確的內容
    else:
        print("\n亂輸入小心期末考被當光光！請重新輸入：\n")
        manu=''
