#################Wrapper
#Carl,bonferroni adjustments,stdres

#I wrote these two wrappers for inspecting the residuals with bonferroni adjustments:

chisq.apr <- function(x,alpha) { # chi-squared adjusted pearson residuals N(0,1)
  print(chisq.test(x))
  adjustedresiduals <- chisq.test(x)$stdres
  print(signif(adjustedresiduals),4)
  #        return(chisq.test(x)$y)
  dim <- nrow(x)*ncol(x)
  p <- (alpha/dim) # bonferroni correction
  print(paste0("dimensions ","(",nrow(x),"x",ncol(x),"): ",dim))
  print(paste0("Bonferroni adjustment to alpha: ",p))    
  print(paste0("two-tailed critical value: ",qnorm(p/2,lower.tail=FALSE))
  )
}

chisq.apr.pvalue <- function(rows,cols,alpha,r) {
  dim <- rows*cols
  p <- (alpha/dim)
  pv <- (1-pnorm(abs(r)))*2
  if(p<pv){
    cat(paste0("actual \033[0;41m",pv,">",p,"(bonf alpha) \033[0m \n"))
  }else{
    cat(paste0("actual \033[0;42m",pv,"<=",p,"(bonf alpha) \033[0m \n"))
  }
  # print(pv)
  # print(p)
}

################# End of Wrapper


####Wrpper ordinal regression

polr.apr <- function(x) { 
  
  # summary(with(D,lm(MotionEnergy~CollabLevelMedian)))
  # testdata<- read.csv("/Users/zohrehkhosrobeigi/Documents/MyPAPER/Papers/Paper3_Multimedia Computing/Carl_Motion_Gest_Each_Player/Data_Motion_Gesture/Book1.csv",header=TRUE,stringsAsFactors=TRUE)
  # head(testdata)
  # summary( polr(apply ~ pared , data = testdata, Hess=TRUE))
  # 
  # #Regression section
  # summary(polr(CollabLevelMedian~MotionEnergy,data=D, Hess=TRUE))
  # model_fit<-polr(Dominance~MotionEnergy,data=D, Hess=TRUE)
  # summary(model_fit)
  # summary_table <- coef(summary(model_fit))
  # pval <- pnorm(abs(summary_table[, "t value"]),lower.tail = FALSE)* 2
  # summary_table <- cbind(summary_table, "p value" = round(pval,3))
  # summary_table
  
  
  
  #Regression section
  #model_fit<-with(D,polr(Dominance~MotionEnergy, Hess=TRUE))
  model_fit<-polr(x, Hess=TRUE)
  print("Summary")
  print(summary(model_fit))
  summary_table <- coef(summary(model_fit))
  
  pval <- pnorm(abs(summary_table[, "t value"]),lower.tail = FALSE)* 2
  summary_table <- cbind(summary_table, "p value" = round(pval,3))
  print("converted Summary table")
  print(summary_table)
  
}
#### end of wrapper
D <- read.csv("Input/Output_Join_Motion_Collab_Dom_Trait_Per_Session_WithinSession.csv",header=TRUE,stringsAsFactors=TRUE)

signif(with(D,tapply(MotionEnergy,list(Gesture),mean)),3)
signif(with(D,tapply(MotionEnergy,list(Gesture),sd)),3)

with(D,kruskal.test(MotionEnergy~Gesture))

with(D,pairwise.wilcox.test(MotionEnergy,Gesture,p.adj = "bonf"))


D$MEQc <- cut(D$MotionEnergy,with(D,c(summary(MotionEnergy)[2:3],summary(MotionEnergy)[5:6])),include.lowest=TRUE,ordered_result=TRUE)#0,0.0001 //  0.0001,0.0111   //    0.0111,1
#add Dominance column based on median, Maria has used.

D$Dominance <- factor(with(D,ifelse(Session=="S02","Right_Is_Dominant",ifelse(Session=="S03","Right_Is_Dominant",ifelse(Session=="S04","Left_Is_Dominant",ifelse(Session=="S05","Left_Is_Dominant",ifelse(Session=="S07","Left_Is_Dominant",
  ifelse(Session=="S08","Right_Is_Dominant",ifelse(Session=="S09","DomBalance",
                                                   ifelse(Session=="S10","Left_Is_Dominant",ifelse(Session=="S11","Left_Is_Dominant",
                                                                                                   ifelse(Session=="S13","Left_Is_Dominant",ifelse(Session=="S14","Right_Is_Dominant",
                                                                                                                                                   ifelse(Session=="S17","DomBalance",ifelse(Session=="S18","Left_Is_Dominant",
                                                                                                                                                                                             ifelse(Session=="S19","Right_Is_Dominant",ifelse(Session=="S20","DomBalance",
                                                                                                                                                                                                                                              ifelse(Session=="S21","Right_Is_Dominant",ifelse(Session=="S22","Right_Is_Dominant",
                                                                                                                                                                                                                                                                                               ifelse(Session=="S23","Left_Is_Dominant","CheckMe"))))))))))))))))))))
#consider the interaction of categories:
chisq.apr(with(D,xtabs(~Gesture+MEQc)),0.05)


with(D,cor.test(MotionEnergy,MedianDom,method="spearman"))
with(D[D$Gesture!="Agestural"&D$Gesture!="NonApplicable",],cor.test(MotionEnergy,MedianDom,method="spearman"))
with(D[D$Gesture=="Agestural"|D$Gesture=="NonApplicable",],cor.test(MotionEnergy,MedianDom,method="spearman"))


with(D,tapply(MedianDom,list(MEQc),mean))

with(D,tapply(MedianDom,list(MEQc),sd))

with(D,kruskal.test(MedianDom~MEQc))

with(D,pairwise.wilcox.test(MedianDom,MEQc,p.adjust.method = "BH"))

chisq.apr(with(D,xtabs(~MedianDom+MEQc)),0.05)
	
signif(with(D,tapply(MotionEnergy,list(Dominance),mean)),3)
signif(with(D,tapply(MotionEnergy,list(Dominance),sd)),3)	
	

with(D,kruskal.test(MotionEnergy~Dominance))
with(D,pairwise.wilcox.test(MotionEnergy,Dominance,p.adjust.method = "BH"))
chisq.apr(with(D,xtabs(~Dominance+MEQc)),0.05)
with(D,tapply(CollabMedian,list(MEQc),mean))
with(D,tapply(CollabMedian,list(MEQc),sd))
with(D,kruskal.test(CollabMedian~MEQc))
with(D,pairwise.wilcox.test(CollabMedian,MEQc,p.adjust.method = "BH"))
chisq.apr(with(D,xtabs(~CollabMedian+MEQc)),0.05)
signif(with(D,tapply(EXTRO_raw_score,list(MEQc),mean)),3)

with(D,cor.test(MotionEnergy,EXTRO_raw_score,method="spearman"))
with(D[D$Gesture=="Agestural"|D$Gesture=="NonApplicable",],cor.test(MotionEnergy,EXTRO_raw_score,method="spearman"))
with(D[D$Gesture!="Agestural"&D$Gesture!="NonApplicable",],cor.test(MotionEnergy,EXTRO_raw_score,method="spearman"))
with(D,kruskal.test(EXTRO_raw_score~MEQc))
with(D,pairwise.wilcox.test(EXTRO_raw_score,MEQc,p.adjust.method = "BH"))
with(D,cor.test(MotionEnergy,AGREE_raw_score,method="spearman"))
with(D[D$Gesture!="Agestural"&D$Gesture!="NonApplicable",],cor.test(MotionEnergy,AGREE_raw_score,method="spearman"))
with(D[D$Gesture=="Agestural"|D$Gesture=="NonApplicable",],cor.test(MotionEnergy,AGREE_raw_score,method="spearman"))

with(D,cor.test(MotionEnergy,CONSCIENTIOUS_raw_score,method="spearman"))
with(D[D$Gesture!="Agestural"&D$Gesture!="NonApplicable",],cor.test(MotionEnergy,CONSCIENTIOUS_raw_score,method="spearman"))
with(D[D$Gesture=="Agestural"|D$Gesture=="NonApplicable",],cor.test(MotionEnergy,CONSCIENTIOUS_raw_score,method="spearman"))

with(D,cor.test(MotionEnergy,OPEN_raw_score,method="spearman"))
with(D[D$Gesture!="Agestural"&D$Gesture!="NonApplicable",],cor.test(MotionEnergy,OPEN_raw_score,method="spearman"))
with(D[D$Gesture=="Agestural"|D$Gesture=="NonApplicable",],cor.test(MotionEnergy,OPEN_raw_score,method="spearman"))

with(D,cor.test(MotionEnergy,NEURO_raw_score,method="spearman"))
with(D[D$Gesture!="Agestural"&D$Gesture!="NonApplicable",],cor.test(MotionEnergy,NEURO_raw_score,method="spearman"))
with(D[D$Gesture=="Agestural"|D$Gesture=="NonApplicable",],cor.test(MotionEnergy,NEURO_raw_score,method="spearman"))
chisq.apr(with(D,xtabs(~EXRTc+MEQc)),0.05)

