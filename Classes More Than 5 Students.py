import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # dict ={}
    # for i in range(len(courses)):
    #     cor = courses['class'][i]
    #     if cor not in dict:
    #         dict[cor] = 1
    #     dict[cor] = dict[cor] + 1

    # result = []
    # for key,value in dict.items():
    #     if value >= 5:
    #         result.append(key)

    # return pd.DataFrame(result,columns=['class']) 
    #sol2       
    # df = courses.groupby(['class']).size().reset_index(name = 'count')
    # df = df[df['count']>=5]
    # print(df)

    # return df[['class']]

    #sol3
    df = courses.groupby(['class']).count().reset_index()
    print(df)
    df = df[df['student']>=5]
    print(df)

    return df[['class']]


 

    