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

### 🌟 메인 페이지
- 플랫폼의 주요 기능 3가지를 소개하는 페이지
![메디차트 메인화면.png](..%2F%EB%A9%94%EB%94%94%EC%B0%A8%ED%8A%B8%20%EB%A9%94%EC%9D%B8%ED%99%94%EB%A9%B4.png)
### 🔑 로그인 및 회원가입
- 기본 회원가입 및 로그인 기능 제공
![image 1.png](..%2Fimage%201.png)
![image.png](..%2Fimage.png)
### 📄 건강진단서 해석
- 의학용어로 작성된 건강진단서를 쉽고 직관적으로 해석
- **언어 지원**: 한국어, 일본어, 중국어
![image 2.png](..%2Fimage%202.png)
### 🩺 검진정보 입력
- 사용자가 건강검진 정보를 입력하고 저장
![image 3.png](..%2Fimage%203.png)
### 📊 질병 예측
- 주요 질병(당뇨, 심장병, 고혈압 등)의 발병 확률 예측 및 시각화
![image 4.png](..%2Fimage%204.png)
### 📣 공지사항 및 고객센터
- 최신 공지사항 확인 및 고객센터 지원
![image 5.png](..%2Fimage%205.png)
### 🛠 관리자 페이지
- 가입자 관리 및 공지사항 작성
![image 6.png](..%2Fimage%206.png)
---

## 구현 예정 기능
- **AI 챗봇**: 건강 관련 질문에 실시간 답변 제공
- ![image 7.png](..%2Fimage%207.png)
- **검진센터 찾기**: 사용자 위치 기반 병원 검색
![image 8.png](..%2Fimage%208.png)
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
