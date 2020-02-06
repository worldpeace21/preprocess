#-*- coding:utf-8 -*-
from konlpy.tag import Twitter
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def count_noun_frequency(text_dir, result_dir):
"""
목적: 명사 빈도수를 카운팅합니다.
Args: 
    - .text 파일 주소
    - 결과를 저장할 파일 주소

"""
    
    # 파일 열기
    with open(text_dir, 'r', encoding='utf-8') as text_file:
        lines = text_file.read()  

    # 명사 추출
    nlpy = Twitter()
    nouns = nlpy.nouns(lines)
    
    # 명사 빈도수 카운팅
    count = Counter(nouns)
 
    # 딕셔너리에 저장   
    dic = {}
    for noun, count in count.items():
            dic[noun]=count
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True) # 빈도수 내림차순 정렬
    total = len(dic) # 명사 총 개수

    
    # 파일에 빈도수 작성
    with open(result_dir, 'w', encoding='utf-8') as result_file:
        for noun, count in dic:
            result_file.write("{}:{}\n".format(noun, count))
        result_file.write("---------------------------------\n")    
        result_file.write("명사 총 {}개\n".format(total))
        result_file.write("---------------------------------\n")    
        
#     # 콘솔에 결과 출력
#     for noun, count in dic:
#             print("{}:{}\n".format(noun, count))
#     print("---------------------------------\n") 
#     print("명사 총 {}개\n".format(total))
#     print("---------------------------------\n") 

#     # 상위 30개 추출
#     up_to = 30
#     top_list = dic[:up_to]
#     x = [element[0] for element in top_list]
#     y = [element[1] for element in top_list]
        
#     # 막대 그래프로 빈도수 시각화
#     plt.bar(x, y)
#     plt.title('단어 빈도수')
#     plt.xlabel('단어')
#     plt.ylabel('빈도수')
#     plt.show()
    