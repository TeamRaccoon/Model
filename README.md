# **Sentiment Analysis System Using Movie Review Corpus**

ICLR 2020 에서 Google 이 학습 효율을 향상시키기 위해 Replaced Token Detection (RTD)이라는 새로운 pre-training 방식을 사용하는 언어 Model 인 ELECTRA 를 발표하였다. ELECTRA 는 기존 BERT 를 비롯한 언어 Model과 비교해 동일 조건에서의 성능 및 학습 효율이 높다. 따라서 이를 기반으로 하는 시스템을 제안한다.

국립국어연구원에서 제공하는 ‘모두의 말뭉치’에는 여러 분야의 말뭉치가 존재하지만, 문장에 대한 감성 분석(문장에 대한 의미를 긍정/부정으로 분류)결과를 부착한 말뭉치는 존재하지 않는다. 따라서 평점으로 긍정/부정이 명확하게 표현되는 영화평을 NAVER, DAUM 을 통해 수집하여 감성 분석 결과를 부착한 자체 제작 말뭉치를 사용한다.



## **시스템 설명**

본 시스템 ‘Sentiment Analysis System Using Movie Review Corpus(영화평 말뭉치를 사용한 감성 분석 시스템)’은 한국어 문장에 대한 긍정-부정을 판단한다.

기존 NSMC(Naver Sentiment Movie Corpus)데이터와 자체 제작한 말뭉치 데이터를 전처리 한 뒤, ELECTRA(Efficiently Learning an Encoder that Classifies Token Replacements Accurately) Model 와 KNU 감성사전 결과의 가중치 합을 수행하여 벡터를 만든다. 이 벡터를 Bi-LSTM 과 RNN 을 거쳐 학습한다.

본 시스템은 관련 연구가 많이 진행되지 않은 ELECTRA 언어 모델을 사용한다. 또한 각 단어의 긍정-부정을 5 가지의 척도(매우 부정/부정/중립/긍정 /매우 긍정)로 나타내는 한국어 감성사전을 사용해 한국어 친화적인 모델을 제안한다.

단순 문맥 표현을 사용하는 모델에서 단어의 긍정-부정 스코어를 더해 모델링을 수행함으로 기존 연구보다 감성 분석에 특화된 시스템일 것이라 기대한다.



## **활용 말뭉치**

본 시스템의 정확도를 높이기 위해서는 긍정-부정에 대한 판단이 명확한 한국어 문장이 필요하다. 평점을 통해 사용자의 긍정-부정을 명확하게 판단할 수 있는 영화평이 적합했고, NAVER 와 DAUM 영화를 통해 영화평을 수집하여 평점에 따라 긍정-부정 결과를 부착한 말뭉치를 자체 제작하였다.

### **1. 모두의 말뭉치**

국립국어연구원에서 제공하는 말뭉치인 ‘모두의 말뭉치’에는 감성 분석이 가능한 신문, 문어, 구어, 웹 등 많은 말뭉치가 존재한다. 하지만 본 시스템에서 학습을 위해 사용하려면 긍정-부정 결과와 같이 사용자의 의도와 생각에 대한 정보가 함께 있어야 했기에 사용이 어려웠다.

감성 분석 연구는 대상에 대한 사용자의 의견을 수집하고 긍정-부정에 따라 분류하여 사용자의 태도를 분석한다. 특정 대상에 대한 대중의 반응을 확인하는 등 많은 분야에서 쓰일 수 있는 만큼 관련 말뭉치를 제공한다면 큰 도움이 될 것이다. 따라서 기존 말뭉치에 긍정-부정에 대한 결과를 함께 제공한다면 감성 분석 연구에 큰 도움이 될 것으로 기대한다.

### **2. 자체 구축한 말뭉치**

NAVER 영화평를 통해 기존 구축되어 있던 말뭉치인 NSMC(Naver Sentiment Movie Corpus)의 경우 2016 년 이전의 영화평을 기반으로 수집한 데이터이다. 2020 년을 기준으로 볼 때 새롭게 생긴 신조어, 사회 경향 등의 영향이 있을 것으로 판단하였다. 따라서 NSMC 의 기준을 이용해 새로운 말뭉치를 구축하였다.

기존 NSMC 는 100K 의 부정 영화평(평점 1-4), 100K 의 긍정 영화평(평점 9-10)을 수집하였고, 중립적인 영화평(평점 5-8)은 제외하였다. 하지만 사람마다 평점을 매기는 기준이 달라 평점 5-8 이 완전히 중립적인 의견이라고 볼 수 없고, 이런 중립적으로 보이는 데이터에서도 중요한 문맥을 파악할 수 있다고 판단하였다.

이에 평점 1-4는 부정 영화평, 평점 8-10은 긍정 영화평으로 분류하고, 평점 5-7에 대해서는 직접 긍정-부정에 대한 라벨링을 진행하였다.

*(저작권 상 NAVER 및 DAUM 영화평의 크롤링은 불법이라고 알고 있다. 연구 목적으로 진행하였고, 따로 공개할 수 있지만 상업적인 사용은 불가능할 것이다. 관련 크롤링 코드 또한 Github를 통해 공개한다.)*



### 시스템 성능

본 시스템에서는 영화평 감성 분석의 실험 데이터로 자체 구축한 영화평 말뭉치를 이용하였고, 학습 15 만개(NSMC)/150 만개(자체구축)와 평가 5 만개(NSMC + 자체구축 중 무작위 선별)의 데이터로 구성된다.

실험을 수행한 환경은 Google Colaboratory 이다. 데이터 셋의 문장 최대 길이는 140, 배치 크기는 128 으로 설정하였다.



표 1 은 NSMC 영화평 데이터 셋, 표 2 는 자체 구축한 데이터 셋에 대해 본 시스템에서 제안한 모델의 시스템 성능을 보인다.
 (앞서 본 시스템에서 KNU 감성사전을 제안하였으나 ELECTRA 와 KNU 감성사전의 Token 이 다르게 형성되고, 벡터의 크기를 맞춰 둘의 가중치 합을 더해 Model 에 돌렸을 때의 정확도가 떨어졌다. 따라서 해당 문서에는 KNU 감성사전을 제외한 Model 의 비교값만을 나타낸다. 또한, KNU 감성사전을 효과적으로 넣는 방법에 대한 논의가 진행 중이다.)

| Model(NSMC)            | Acc       | 차이      |
| ---------------------- | --------- | --------- |
| ELECTRA                | 85.87     | -         |
| **ELECTRA + BiLSTM**   | **88.26** | **+2.39** |
| ELECTRA + BiLSTM + RNN | 88.25     | +2.38     |

[Table 1] NSMC학습 모델 영화평 감성 분석 비교



| Model(자체 구축 데이터 셋) | Acc       | 차이(자체/NSMC)   |
| -------------------------- | --------- | ----------------- |
| ELECTRA                    | 93.5      | - / +7.63         |
| **ELECTRA + BiLSTM**       | **93.87** | **+0.37 / +8.00** |
| ELECTRA + BiLSTM + RNN     | 93.76     | +0.26 / +7.89     |

[Table 2] 자체 구축 데이터 셋 학습 모델 영화평 감성 분석 비교

비교 결과, NSMC 로 학습시킨 모델은 정확도 85.87%를 보였다. ELECTRA + BiLSTM 모델은 ELECTRA 단독 모델보다 정확도가 2.39%, ELECTRA + BiLSTM + RNN 모델은 2.38% 더 향상되었다. 자체 구축 데이터 모델은 NSMC 로 학습시킨 모델보다 ELECTRA 단독 모델은 7.63%의 향상을 보였고, ELECTRA + BiLSTM 모델은 8.00%의 향상을 보였다. ELECTRA + BiLSTM + RNN 모델은 7.89%의 향상을 보였다.

#### 결론

2020.09.15 기준 ELECTRA + BiLSTM 모델이 가장 좋은 성능을 보이는 것으로 판단되었다. 최신의 데이터를 평가 데이터로 사용하는 것을 염두해둔다면, 자체구축 데이터 셋으로 모델을 학습시키는 것이 가장 높은 성능을 보인다.

