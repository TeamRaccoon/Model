# **Sentiment Analysis System Using Movie Review Corpus**

ICLR 2020에서 Google이 학습 효율을 향상시키기 위해 Replaced Token Detection (RTD)이라는 새로운 pre-training 방식을 사용하는 언어 Model인 ELECTRA를 발표하였다. ELECTRA는 기존 BERT를 비롯한 언어 Model과 비교해 동일 조건에서의 성능 및 학습 효율이 높다. 따라서 이를 기반으로 하는 시스템을 제안한다.

국립국어연구원에서 제공하는 ‘모두의 말뭉치’에는 여러 분야의 말뭉치가 존재하지만, 문장에 대한 감성 분석(문장에 대한 의미를 긍정/부정으로 분류)결과를 부착한 말뭉치는 없다. 따라서 평점으로 긍정/부정이 명확하게 표현되는 영화평을 NAVER, DAUM을 통해 수집하여 감성 분석 결과를 부착한 자체 제작 말뭉치를 사용한다.



## **시스템 설명**

본 시스템 ‘Sentiment Analysis System Using Movie Review Corpus(영화평 말뭉치를 사용한 감성 분석 시스템)’은 한국어 문장에 대한 긍정-부정을 판단한다. 

기존 NSMC(Naver Sentiment Movie Corpus)데이터와 자체 제작한 말뭉치 데이터를 전처리 한 뒤, ELECTRA(Efficiently Learning an Encoder that Classifies Token Replacements Accurately) Model와 KNU감성사전 결과의 가중치 합을 수행하여 벡터를 만든다. 이 벡터를 Bi-LSTM과 FNN을 거쳐 학습한다.

본 시스템은 관련 연구가 많이 진행되지 않은 ELECTRA 언어 모델을 사용한다. 또한 각 단어의 긍정-부정을 5가지의 척도(매우 부정/부정/중립/긍정/매우 긍정)로 나타내는 한국어 감성사전을 사용해 한국어 친화적인 모델을 제안한다.

단순 문맥 표현을 사용하는 모델에서 단어의 긍정-부정 스코어를 더해 모델링을 수행함으로 기존 연구보다 감성 분석에 특화적일 것이라고 기대한다.



## **활용 말뭉치**

본 시스템의 정확도를 높이기 위해서는 긍정-부정에 대한 판단이 명확한 한국어 문장이 필요하다고 생각했다. 따라서 평점으로 사용자의 긍정-부정이 명확하게 표현되는 영화평이 적합했고, NAVER와 DAUM 영화를 통해 영화평을 수집하여 평점에 따라 긍정-부정 결과를 부착한 말뭉치를 자체 제작하였다. 

### **1. 모두의 말뭉치**

국립국어연구원에서 제공하는 말뭉치인 ‘모두의 말뭉치’에는 감성 분석이 가능한 신문, 문어, 구어, 웹 등 많은 말뭉치가 존재했다. 하지만 본 시스템에서 학습을 위해 사용하려면 긍정-부정 결과와 같이 사용자의 의도와 생각에 대한 정보가 함께 있어야 했기에 사용이 어려웠다.

감성 분석 연구는 특정 대상에 대한 사용자의 의견을 수집하고 분류하는 과정을 통해 사용자의 긍정-부정, 태도를 분석할 수 있다. 이에 특정 대상에 대한 대책을 수립하는 등 많은 분야에서 쓰일 수 있는 만큼 관련 말뭉치를 제공한다면 큰 도움이 될 것이다. 따라서 기존 말뭉치에 긍정-부정에 대한 결과를 사람들이 직접 부착하여 제공한다면 감성 분석 연구에 큰 도움이 될 것으로 기대된다.

### **2. 자체 구축한 말뭉치**

NAVER 영화평를 통해 기존 구축되어 있던 말뭉치인 NSMC(Naver Sentiment Movie Corpus)의 경우 2016년 이전의 영화평 데이터이다. 2020년을 기준으로 볼 때 새롭게 생긴 신조어, 사회 경향 등의 영향이 있을 것으로 판단하였다. 따라서 NSMC의 기준을 이용해 새로운 말뭉치를 구축하였다. 

기존 NSMC는 100K의 부정 영화평(평점 1-4), 100K의 긍정 영화평(평점 9-10)을 수집하였고, 중립적인 영화평(평점 5-8)은 제외하였다. 하지만 사람마다 평점을 매기는 기준이 달라 평점 5-8이 완전히 중립적인 의견이라고 볼 수 없고, 이런 중립적으로 보이는 데이터에서도 중요한 문맥을 파악할 수 있다고 판단하였다. 

이에 평점 1-4는 부정 영화평, 평점 8-10은 긍정 영화평으로 분류하고, 평점 5-7에 대해서는 직접 긍정-부정에 대한 라벨링을 진행하였다.

*(저작권 상 NAVER 및 DAUM 영화평의 크롤링은 불법이라고 알고 있다. 연구 목적으로 진행하였고, 따로 공개할 수 있지만 상업적인 사용은 불가능할 것이다. 관련 크롤링 코드 또한 Github를 통해 공개한다.)*
