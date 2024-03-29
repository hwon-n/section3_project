# 게임에 흥미를 가질 인원 예측해보기 

## 💻 프로젝트 소개

전체적인 데이터 Pipeline을 경험해보자는 목적을 갖고 진행한 프로젝트입니다. 

만약 게임을 제작할 때 자신이 제작해보고 싶은 게임의 장르, 태그, 연령가 등을 선택하면 몇 명이 관심을 가질지 재미로 예측해볼 수 있습니다. 

<br />


## 🎮 개발 기간

21.12.08 - 21.12.13

<br />

## 🛠 사용 툴

* Colab
* Visual Studio Code
* Python
  * pandas
  * sklearn
  * Flask
  * pymongo
  * pickle
* HTML
* mongoDB
* metabase
* heroku

<br />

## 🧷 전체적인 Pipeline

![image](https://user-images.githubusercontent.com/52039588/217835791-d508cc2c-55e0-4e18-92a9-40aa9e8ac9c9.png)


#### 🔍 굳이 CSV 파일을 사용한 이유

원래 local 환경에서 API를 활용해서 바로 DataFrame에 데이터를 저장한 뒤 데이터 전처리를 끝낸 후 mongoDB에 올리는 것을 계획하고 시도했습니다. 
다만 mongoDB에 대략 3000개의 데이터가 저장되면 그 이상의 데이터는 저장이 되지 않는 문제가 발생했습니다. 때문에 local 환경에서 데이터를 받아오는 것을 멈추고 colab으로 옮겨가 데이터를 마저 받아왔습니다.
데이터를 받아오고 데이터 전처리까지 하루만에 끝냈다면 따로 csv 파일을 사용하지 않았겠지만, 아쉽게도 하루만에 끝내지 못해서 이미 받아온 데이터들을 csv에 저장한 뒤 차근차근 진행했기 때문에 csv 파일을 사용했습니다. 


<br />


## 🗃 사용 데이터

[RAWG API](https://api.rawg.io/docs/)를 사용해서 게임 리스트를 받아와 데이터로 사용했습니다.

<br />

|컬럼명|설명|
|----|----|
|added|게임 출시 날짜|
|playtime|게임 플레이 시간|
|platform|출시 플랫폼 수|
|genres|게임 장르|
|stores|게임 판매 스토어|
|tag|게임 설명 태그|
|esrb_rating|연령가|



<br />

  
## 🔎 주요 내용


### 웹 페이지 구현

![image](https://user-images.githubusercontent.com/52039588/217909682-d3024576-d714-4b62-9a2b-12ec5345d4dc.png)


### 데이터 적재하기

API를 사용해 데이터를 csv 파일로 저장해 준 뒤 전처리를 진행해 주었습니다. 그리고 전처리가 완료된 데이터들을 다시 mongoDB에 적재해 주었습니다. mongoDB에 적재한 이유는 metabase를 사용해서 쉽게 데이터 분석을 하기 위해서입니다. 

그리고 사용자에게서 데이터를 입력받아서 머신러닝 모델이 예측을 한 결과도 mongoDB에 저장해주었습니다. MongoDB에 저장한 뒤 어떠한 결과가 제일 많이 나왔는지에 대해서도 한번 살펴보았습니다. 


<br />

### metabase




### 회고글

[Section3 Project 회고](https://velog.io/@woooa/AIB7-Section3-project-%ED%9A%8C%EA%B3%A0)를 velog에 올려놨습니다. 프로젝트를 진행하면서 겪었던 자잘하고 사소한 일들과 그에 대한 아쉬움을 기록한 글입니다. 


<br />
