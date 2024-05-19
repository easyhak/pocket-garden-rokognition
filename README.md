# Pocket Garden

## AWS Rekognition Custom Label Model Explain

- 33 labels
    <details>
    <summary>label</summary>
        <div markdown="1">
            <ul>
                <li>개나리</li>
                <li>금잔화</li>
                <li>나팔꽃</li>
                <li>단풍나무</li>
                <li>달리아</li>
                <li>대나무</li>
                <li>데이지</li>
                <li>라벤더</li>
                <li>라일락</li>
                <li>로즈마리</li>
                <li>매화</li>
                <li>모과</li>
                <li>목련</li>
                <li>무궁화</li>
                <li>튤립</li>
                <li>해바라기</li>
                <li>감나무(감)</li>
                <li>백합</li>
                <li>벚꽃</li>
                <li>복숭아</li>
                <li>사과</li>
                <li>소나무(솔방울)</li>
                <li>수국</li>
                <li>수선화</li>
                <li>안개꽃</li>
                <li>유자</li>
                <li>연꽃</li>
                <li>은행나무(은행잎)</li>
                <li>장미</li>
                <li>제비꽃</li>
                <li>진달래</li>
                <li>카네이션</li>
                <li>코스모스</li>
            </ul>
            
        </div>
    </details>

- 6700's Image datas

## How to Deploy

1. We need AWS Rekognition custom label model and default detect label
2. If you've been trained to be a model start model
```shell
aws rekognition start-project-version \
  --project-version-arn rekognition_arn \
  --min-inference-units 1 \
  --region ap-northeast-2
```
3. Create Lambda Function you need to create custom-detect and detect function
4. The policy needs to be checked. You can found policy in template.yml file or You can deploy by using SAM
5. Create two API using API GateWay
 - /custom - post
 - /detect - post
## API Call Example

### /detect

**Request Body**
```json
{
  "bucket": bucket_name,
  "name": image_name
}
```
---
**Response Body**
```json
[
    "Food",
    "Fruit",
    "Plant",
    "Produce",
    "Persimmon",
    "Pear",
    "American Football (Ball)",
    "Football",
    "Sport",
    "Orange"
]
```
### /custom

**Request Body**
```json
{
  "bucket": bucket_name,
  "name": image_name
}
```
---
**Response Body**
```json
감나무
```

## Others
<a href="https://github.com/Choi-JY1107/2024-Union-Hackathon" >FrontEnd Code</a>   
<a href="https://github.com/Choi-JY1107/2024-Union-Hackathon" src="">BackEnd Code</a>
