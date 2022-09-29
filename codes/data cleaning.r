library(tidyverse)
df<-read.csv("C:/Users/USER-PC/Desktop/america.csv")

#see whether there is some missing values 
print(sum(is.na(df)))

#change the column named "Cliton" to "Clinton"
names(df)[names(df)=="Cliton"]<-"Clinton"
#fill the missing values in the column "Trump" with the value of "1-Clinton"
df$Trump[is.na(df$Trump)]<-1-df$Clinton[is.na(df$Trump)]

#fill the missing values in the column "Clinton" with the value of "1-Trump"
df$Clinton[is.na(df$Clinton)]<-1-df$Trump[is.na(df$Clinton)]


#add a new column to the data frame named "Trump_win_ornot" to indicate whether Trump won the state or not
df$Trump_win_ornot<-ifelse(df$Trump>df$Clinton,1,0)

print(df)

#save the data frame as a new csv file
write.csv(df,"C:/Users/USER-PC/Desktop/america_cleaned.csv")