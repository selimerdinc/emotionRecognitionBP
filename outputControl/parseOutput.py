def returnResult(output):
    my_file = open(output, "r",encoding="utf-8")
    outputs=my_file.read().lower()
    outputs=outputs.replace("\n",",")
    outputs=outputs.split(",")

    happyCount=outputs.count("happy")
    sadCount=outputs.count("sad")
    angryCount=outputs.count("angry")
    fearCount=outputs.count("fear")
    disgustCount=outputs.count("disgust")
    neutralCount=outputs.count("neutral")
    surpriseCount=outputs.count("surprise")

    toplam=happyCount+sadCount+angryCount+fearCount+disgustCount+neutralCount+surpriseCount
    ortHappy=float((happyCount/toplam)*100).__round__(2)
    ortSad=float((sadCount/toplam)*100).__round__(2)
    ortAngry=float((angryCount/toplam)*100).__round__(2)
    ortFear=float((fearCount/toplam)*100).__round__(2)
    ortDisgust=float((disgustCount/toplam)*100).__round__(2)
    ortNeutral=float((neutralCount/toplam)*100).__round__(2)
    ortSurprise=float((surpriseCount/toplam)*100).__round__(2)

    list=["Happy","Sad","Angry","Fear","Disgust","Neutral","Surprise"]
    dataList=[happyCount,sadCount,angryCount,fearCount,disgustCount,neutralCount,surpriseCount]
    ortList = [ortHappy,ortSad,ortAngry,ortFear,ortDisgust,ortNeutral,ortSurprise]

    for i in range(0,7) :
        print(list[i]," = ",dataList[i],"// Oran : %",ortList[i])




