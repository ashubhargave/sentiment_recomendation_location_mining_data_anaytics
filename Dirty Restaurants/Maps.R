library(ggplot2)
library(ggmap)
table = read.table("C:/Users/AshutoshBhargave/Desktop/Courses/BigData/Project/Phoenix City.txt",header=TRUE,sep="\t")
lat = table$latitude
long = table$longitude

#,maptype ="hybrid"
map <- get_map(location ="Phoenix", zoom=12)
p <-ggmap(map)
p <- p + geom_point(data=table,aes(x=long,y=lat),,colour="red",size=2.5)
p <- p + geom_text(data=table, aes(x=long, y=lat,label=table$bad_reviews_size), size=2, hjust=-0.1)+xlab('Longitude')+ ylab('Latitude')+ggtitle("Dirty Restaurants in Phoenix")
#Plot the graph
print(p)


#Open The Las Vegas file
vegas = read.table("C:/Users/AshutoshBhargave/Desktop/Courses/BigData/Project/Las Vegas City.txt",header=TRUE,sep="\t")
vegas_lat = vegas$latitude
vegas_long = vegas$longitude

#,maptype ="hybrid"
map <- get_map(location ="Las Vegas", zoom=12)
p <-ggmap(map)
p <- p + geom_point(data=vegas,aes(x=vegas_long,y=vegas_lat),,colour="red",size=2.5)
p <- p + geom_text(data=vegas, aes(x=vegas_long, y=vegas_lat,label=vegas$bad_reviews_size), size=2, hjust=-0.1)+xlab('Longitude')+ ylab('Latitude')+ggtitle("Dirty Restaurants in Las Vegas")
#Plot the graph
print(p)
size_review = c(2472,1383,520,338,290)
place = c("Las Vegas","Phoenix","Pittsburgh","madison","Chandler")
datam = data.frame(x= place,y=size_review)
ggplot(data= datam,aes(x=place, y=size_review)) + geom_bar(colour="black", fill="#DD8888", width=.8, stat="identity") + guides(fill=FALSE) +xlab("Location") + ylab("Number of dirty restaurants") +ggtitle("Top 5 cities with dirty restaurant")
          