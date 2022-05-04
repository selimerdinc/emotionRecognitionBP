my_file = open("output.txt", "r",encoding="utf-8")
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
ortHappy=(happyCount/toplam)*100
ortSad=(sadCount/toplam)*100
ortAngry=(angryCount/toplam)*100
ortFear=(fearCount/toplam)*100
ortDisgust=(disgustCount/toplam)*100
ortNeutral=(neutralCount/toplam)*100
ortSurprise=(surpriseCount/toplam)*100

list=["Happy","Sad","Angry","Fear","Disgust","Neutral","Surprise"]
dataList=[happyCount,sadCount,angryCount,fearCount,disgustCount,neutralCount,surpriseCount]
ortList = [ortHappy,ortSad,ortAngry,ortFear,ortDisgust,ortNeutral,ortSurprise]

for i in range(0,7) :
    print(list[i]," = ",dataList[i],"// Oran : %",ortList[i])





