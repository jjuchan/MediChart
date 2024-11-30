# MediChart

### 🧑‍⚕️ 현대인을 위한 건강 플랫폼 MediChart
**MediChart**는 바쁜 일상 속 자신의 건강을 놓치는 현대인들을 위한 **질병 예측 및 건강진단서 해석 플랫폼**입니다.

- **프로젝트 URL**: [MediChart](http://223.130.155.178)
- **테스트 계정**:
 - **ID**: `test@naver.com`
 - **PW**: `q1w2e3r4!@`
- **개발 기간**: 2024.07.05 ~ 2024.08.06

> **주의**: 건강진단서 해석 기능은 제공된 테스트용 이미지를 사용하세요.

---

## :blue_heart: About Us
### 🧑‍💻 응답없음 팀
| ![정형진](https://avatars.githubusercontent.com/u/112332792?v=4) | ![김민재](https://avatars.githubusercontent.com/u/163969011?v=4) | ![윤주찬](https://avatars.githubusercontent.com/u/163832764?v=4) | ![이태현](https://avatars.githubusercontent.com/u/130521454?v=4) | ![박계영](https://avatars.githubusercontent.com/u/102974568?v=4) | ![최혜빈](https://avatars.githubusercontent.com/u/164338512?v=4) |  
| :---: | :---: | :---: | :---: | :---: | :---: |  
| 정형진<br>[@JeongBuBu](https://github.com/JeongBuBu) | 김민재<br>[@KnD0715](https://github.com/KnD0715) | 윤주찬<br>[@jjuchan](https://github.com/jjuchan) | 이태현<br>[@judgerTH](https://github.com/judgerTH) | 박계영<br>[@himelons](https://github.com/himelons) | 최혜빈<br>[@h9421](https://github.com/h9421) |  
| 백엔드 | 백엔드 | 백엔드 | 백엔드/프론트엔드 | 프론트엔드 | 프론트엔드 |

---

## 주요 기능
- 로그인
- 건강진단서 해석
- 검진정보 입력
- 질병 예측
- 관리자 페이지
- (구현 예정) 소셜 로그인
- (구현 예정) AI 챗봇
- (구현 예정) 검진센터 찾기

---

## :gear: 개발 환경 요약

### 주요 기술 스택
- **Java**: 17
- **Spring Boot**: 3.3.1
- **Database**: MySQL
- **View**: Thymeleaf, Thymeleaf Layout Dialect, JSTL
- **Security**: Spring Security, OAuth2, JWT
- **Cloud**: Google Cloud Translate, Vision, Dialogflow
- **Build Tool**: Gradle

### 주요 의존성
- **Spring Boot Starter**: Web, Data JPA, Security, OAuth2 Client, Mail, Validation, WebSocket
- **Google Cloud**: Translate API, Vision API, Dialogflow API
- **JWT**: `jjwt-api`, `jjwt-impl`, `jjwt-jackson`
- **테스트**: Spring Boot Test, Spring Security Test, JUnit

### React 빌드 작업
- 프론트엔드 경로: `src/main/reactfront`
- NPM 설치 및 빌드:
 - Windows: `npm.cmd install`, `npm.cmd run build`
 - 기타 OS: `npm install`, `npm run build`
- 빌드 결과 복사: `src/main/resources/static`

---

## 주요 페이지 및 기능 설명

### [메인페이지]
#### ✨  MediChart의 주요 기능 3가지를 소개하는 페이지입니다.
![image](https://github.com/user-attachments/assets/b14b2326-5f00-465b-a72c-ad3b98bfdb9f)

### [로그인 및 회원가입]
![스크린샷 2024-08-05 184113](https://github.com/user-attachments/assets/f6520993-f2f5-49e5-9423-83ad66963b08)
![스크린샷 2024-08-05 184127](https://github.com/user-attachments/assets/d84c89d9-10a2-4252-bb50-3854d975daa6)

### [건강진단서 해석]
#### ✨ 어려운 의학용어로 된 건강진단서를 쉽게 이해할 수 있도록 해석해 주는 페이지입니다.<br/>
● 원하는 언어를 선택합니다. (한국어/일본어/중국어) <br/>
● 건강진단서를 파일로 첨부합니다.<br/>
● 원본 텍스트와 번역된 텍스트를 한 번에 확인할 수 있습니다.<br/>
![image](https://github.com/user-attachments/assets/bc9c91f9-f191-4b02-897d-2e3a8115fe0b)
### [검진정보 입력]
#### ✨ 질병 예측을 위해 사용자의 건강검진 정보를 입력받는 페이지입니다.
● 정보를 입력하고 등록 버튼을 누르면 저장되었다는 문구가 페이지 상단에 표시됩니다.<br/>
● 등록 버튼 클릭 후 모든 정보가 입력되지 않았을 경우 입력해달라는 경고 문구가 페이지 상단에 나타납니다.

![image](https://github.com/user-attachments/assets/a01969c4-aebb-4c45-9120-b526b34c2738)
###  [질병 예측]
#### ✨ 사용자가 입력한 검진 정보를 토대로 질병이 발병할 확률을 예측하는 페이지입니다.
● 결과확인 버튼을 누르면 사용자의 검진 정보 데이터를 가지고 질병의 위험도를 예측해주는 그래프가 나타납니다.<br/>
● 그래프는 주의, 경고, 위험 순으로 질병의 발병 확률을 표시합니다.<br/>
● 당뇨병, 심장병, 고혈압, 신장질환, 비만, 뇌졸증의 발병 확률을 예측합니다.
![image](https://github.com/user-attachments/assets/ca8d020b-3aba-4e12-a468-c80fedcf91d5)

###  [공지사항 & 고객센터]
![image](https://github.com/user-attachments/assets/e6221bc6-ae70-4ea7-bd60-5282c99eee4f)

###  [관리자페이지]
#### ✨ 공지사항 및 가입자 수를 관리하는 페이지입니다.
- 관리자페이지 버튼은 푸터에 기입되어 있습니다.
  ![관리자 페이지](https://github.com/user-attachments/assets/3fe31b03-b6d3-4fde-bc39-1665f5e28b2b)
  </br></br>

# 구현 예정

###  [AI 챗봇]
#### ✨ 언제 어디서나 건강 관련 질문을 실시간으로 답변 받을 수 있습니다.
● 정보를 입력하고 등록 버튼을 누르면 저장되었다는 문구가 페이지 상단에 표시됩니다. <br/>
● 등록 버튼 클릭 후 모든 정보가 입력되지 않았을 경우 입력해달라는 경고 문구가 페이지 상단에 나타납니다.<br/>
<img src="https://github.com/user-attachments/assets/42b3d121-071c-4a7d-ab18-96a439de2b9b" width="400" height="600"/>

###  [검진센터 찾기]
#### ✨ 자신의 위치에서 가까운 병원을 찾을 수 있습니다.
![image](https://github.com/user-attachments/assets/92eb5c97-8c7d-48e0-9615-ff7fac7434fa)
---

## 🛸 기술 스택

### 공통
![GitHub](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)  
![Git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white)

### 프론트엔드
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=black)  
![CSS](https://img.shields.io/badge/Css-1572B6?style=for-the-badge&logo=Css&logoColor=white)  
![HTML5](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white)  
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### 백엔드
![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)  
![Node.js](https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white)  
![Java](https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white)  
![Spring](https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white)  
