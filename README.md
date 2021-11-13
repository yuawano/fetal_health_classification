# How can we end preventable fetal death and maternal death?
![image](images/pic1.jpg)

## Background 
Did you know that having a healthy child is rather a miracle than 'normal'? 
Did you know that many pregnancy comes with risk of death?
Many of us who lives in a developed world may have a beautiful picture of having a child but in the developing world there are many challenges lie in pregnancy and giving birth. Over 90% of fetal death and maternal death are happening in the developing world.

Based on the report from UNICEF open data source, it is estimated that **5.1 million** infant passed away before their fifth birthday. Out of the 5.1 million, **approx. 50% of death is happening within 4 weeks after birth (neonatal)**. And in addition, there are estimats of **2 million still birth (born dead)** where every third case is preventable.

The world made remarkable progress in child survival in the past three decades. Since 2015, there is a new targets set out in the Sustainable Development Goals (SDGs) of ending preventable death of newborns and children under 5 years old.
Therefore it is **essential to have a closer look into how to end preventable stillbirth and neonatal**.

In addition to fetal death, in 2015, in anticipation of the launch of the SDGs, the World Health Organization (WHO) and partners released a consensus statement and full strategy paper on **ending preventable maternal mortality**. As of 2019 report from UNICEF open data source, there are 30 thousand maternal death worldwide and most are preventable.

## Project target and data source
### Target
By using Cardiotocography (CTG) data of fetal heart and uterine contractions,
detect fetal health by **creating classification model** and by **data visualization techniques**.

Ultimately apply these results and techniques in the developing world with high stillbirth and neonatal death to help medical practitioners to take immediate actions to prevent fetal death and maternal death and acheive the target of SDGs by 2030.


### Data source
- Data set:  [Cardiotocography (CTG) data](https://www.kaggle.com/andrewmvd/fetal-health-classification) of fetal heart and uterine contractions from Kaggle
- Data set size: 2126 rows x 22 features
- Target variable: Fetal health status (Normal, Suspect, Pathological)
- Example of features: Baseline value (beats per minute), Uterine contractions per seconds, Severe decelerations, Histogram widths, max, min, mean 

## Solution and results

### modeling
Imbalanced data was found in the target variable, therefore upsampling and SMOTE metrix was used to fix imbalance.
In this studies three different model was tested: **Logistic regression, KNN Classifier** and **Random Forest**.

Results:

| Models              |        |          | upsample       | smote          |
|---------------------|--------|----------|----------------|----------------|
| Logistic regression |        |          | 0.7            | 0.72           |
| KNN Classifier      | recall | A/ B/ C  | 0.78/0.90/0.95 | 0.84/0.89/0.93 |
|                     | F1     | A/ B/ C  | 0.83/0.88/0.93 | 0.87/0.86/0.94 |
| Random forest       |        |          | **0.94**       | **0.92**       |

Based on the results above, upsampling metrix with random forest performed best in this particular case.

### Findings from data visualization 

**TO BE UPDATED!!!**

## Libraries
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/stable/contents.html)
- [Seaborn](https://seaborn.pydata.org/)
- [Sklearn](https://scikit-learn.org/stable/)




### Other resource:
- [WHO maternal death report](https://www.who.int/news/item/05-10-2021-new-global-targets-to-prevent-maternal-deaths)
- [WHO Neonatal and perinatal mortality](http://apps.who.int/iris/bitstream/handle/10665/43444/9241563206_eng.pdf;jsessionid=F36359625C33C27CABCEBD4D451A7C46?sequence=1)
