# vue-project

Vue 프로젝트 템플릿입니다.
## 미리 설치된 주요 라이브러리

사용에 도움이 될만한 라이브러리를 미리 설치 해두었습니다.
- [Radix Vue](https://www.radix-vue.com/): 스타일이 지정되어 있지 않고, 접근성을 고려하여 설계된 컴포넌트 라이브러리
- [Pinia](https://pinia.vuejs.org/): 상태 관리 라이브러리
- [Vue Router](https://v3.router.vuejs.org): URL PATH 라우팅 라이브러리

## 프로젝트 셋업

윈도우 유저의 경우
1. [Node.JS](https://nodejs.org/en/download)를 설치합니다.
2. **Powershell을 관리자 권한**으로 열고 [코어팩을 활성화](https://github.com/nodejs/corepack) 합니다.
3. 정상적으로 실행되었다면 닫아주세요. (아래에 있는 명령어는 VS code를 열고 일반 권한의 Powershell을 사용하시면 됩니다) 
```
# 관리자 모드 Powershell
corepack enable
```

맥 유저의 경우
1. [Brew](https://brew.sh/)를 설치합니다.
2. [Node.JS](https://formulae.brew.sh/formula/node)를 설치합니다.
3. [코어팩을 활성화](https://github.com/nodejs/corepack) 합니다.
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install node
corepack enable
```

이제 다음 명령을 실행해 패키지들을 설치합니다.  
단, 프로젝트 폴더의 위치에서 실행해야 합니다.
```sh
yarn install
```

### 다양한 명령어들
- `yarn start`: 개발시 컴파일 및 핫로딩 실행
- `yarn build`: 배포용으로 빌드
- `yarn lint`: 코드 포매팅과 [ESLint](https://eslint.org/) 체크
- `yarn fix`: `yarn lint`에서 에러가 났다면, 자동으로 고치기를 시도합니다
- `yarn check`: 타입을 체크합니다
- `yarn test`: [Vitest](https://vitest.dev/)로 테스트 코드를 실행합니다

### Visual Studio 코드 사용
여기서는 템플릿 프로젝트를 열도록 하겠습니다.
![스크린샷 2023-11-14 155748](https://github.com/Mankik/season2/assets/25581533/3a349cda-37d5-473f-9b62-36c70e6f1aad)
![스크린샷 2023-11-14 155843](https://github.com/Mankik/season2/assets/25581533/1ab08305-8900-46fb-8400-c50097c47d42)

린트나 디버거등의 기능을 활성화 하기 위해 신뢰함으로 체크합니다.
![스크린샷 2023-11-14 155955](https://github.com/Mankik/season2/assets/25581533/78b951d5-b750-488f-8b29-ec0e35f39481)

추천하는 확장기능들을 설치합니다.
![스크린샷 2023-11-14 160046](https://github.com/Mankik/season2/assets/25581533/01342d7d-d8b1-4f46-91fe-6b62e1e06a44)
![스크린샷 2023-11-14 160252](https://github.com/Mankik/season2/assets/25581533/e16319e9-00f8-4654-8756-abf5732be01f)

이제 잘 동작하는 모습을 볼 수 있습니다.  
터미널을 열고 명령어도 실행할 수 있습니다.
![스크린샷 2023-11-14 170411](https://github.com/Mankik/season2/assets/25581533/65452c55-c07f-48a4-ae8c-d9d8dcc75e7b)

혹시 `Cannot find module 'vue'. Did you mean to set the 'moduleResolution' option to 'node'`과 같은 문제가 뜬다면 다음 사항들을 체크해주세요.
1. 확장기능에서 [`Vetur`](https://github.com/vuejs/vetur)는 비활성화 해주세요, [`Volar`](https://github.com/vuejs/language-tools)를 사용해야 합니다.
2. Visual Studio 코드의 버전이 [1.77.3](https://stackoverflow.com/questions/75870063/vscode-and-typescript-5-moduleresolution-bundler) 이상인지 확인하십시오.

혹시 성능에 문제가 있다면 [TypeScript and JavaScript](https://github.com/vuejs/language-tools/discussions/471#discussioncomment-1361669)를 워크스페이스에서 비활성화 해볼 수 있습니다.
![image](https://github.com/Mankik/season2/assets/25581533/4cc862cc-d473-45bb-a5de-4aa1bdacdf7f)



## Git 규칙
이 레포에 권장하는 Git 규칙입니다.

### 1. 커밋 기준
- 의미: 항상 의미가 있는 커밋을 진행합니다.
- 작업당 하나: 다양한 작업이 혼합되어 있으면 구별하기 어렵습니다.
  - 의미만 있다면 1~2줄짜리 커밋도 상관없습니다.
  - 작업당 하나씩하게 되면 [되돌리기(revert)](https://git-scm.com/docs/git-revert)가 가능해집니다.
- 자주: 가능한 자주 커밋합니다. 대규모 변경은 코드에 문제가 생길 여지가 많아지며, 리뷰 또한 어려워집니다.
  - 한시간 내에 리뷰하려면 [200라인 안쪽](https://smallbusinessprogramming.com/optimal-pull-request-size/) 이어야 합니다.
  - 특수한 경우가 아니라면 한 커밋당 300~400라인 안쪽으로 최대한 유지하세요. 500라인보다 크면 [리뷰는 거의 불가능](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)해집니다.

### 2. 커밋 메세지
- 이슈가 있다면 커밋 메세지에 이슈번호를 넣어야 합니다.
- 한눈에 알아볼 수 있게 설명하세요.
  - 외국인이 사용하지 않으므로 한글이어도 상관없습니다.
- 가능한 일관적인 커밋 메세지를 지킵니다.
  - `Type: Message` 형식: 타입을 반드시 명시합니다.
  - `Type: Component - Message` 형식: [리눅스](https://github.com/torvalds/linux)처럼 컴포넌트 정보를 넣어도 좋습니다.

저희가 사용하는 커밋 메세지 타입들입니다.
- `Fix`: 버그 수정
- `Feat`: 기능 추가
- `Docs`: 문서
- `Style`: 코딩 스타일
- `Refactor`: 리팩토링
- `Perf`: 성능 향상
- `Test`: 테스트코드
- `Chore`: 빌드 프로세스, 라이브러리, 툴링

예를 들어 채팅방에서 AI 메세지에 대한 평점 팝업을 만들었을 때는 다음과 같이 쓸 수 있습니다.
```
Feat: ChatRoom - Rating pop-up for AI messages
```

### 3. 코드 리뷰
리뷰시의 일반적인 규칙들은 다음과 같습니다.

- 리뷰할 코드는 300~400 라인 안쪽으로
- 다른 아이디어는 PR을 분리하고, 각각 보내기
- 충분한 정보 명시
- 리뷰 코멘트 시 강도

```
P1: 꼭 반영해 주세요 (Request changes)
P2: 적극적으로 고려해 주세요 (Request changes)
P3: 웬만하면 반영해 주세요 (Comment)
P4: 반영해도 좋고 넘어가도 좋습니다 (Approve)
P5: 그냥 사소한 의견입니다 (Approve)
```

### 4. 클라이언트

클라이언트는 강제하지 않지만 추천하는 것은 있습니다.

VS Code 확장:
1. [EdaMagit](https://marketplace.visualstudio.com/items?itemName=kahole.magit): 파일에서 일부만 커밋할 수 있도록 돕습니다.
2. [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens): 누가 코드를 수정했는지 내역을 보기 쉽게 만들어줍니다.

CLI 도구:
1. [Git Branchless](https://github.com/arxanas/git-branchless): 사용법은 [제 블로그](https://black7375.tistory.com/92#%ED%88%AC%EA%B8%B0%EC%A0%81-%EC%BB%A4%EB%B0%8B%EA%B3%BC-%EC%84%A0%ED%98%95%EC%A0%81-%EA%B8%B0%EB%A1%9D)를 참고
2. [Zsh setting](https://github.com/black7375/BlaCk-Void-Zsh): 제가 만든 ZSH 환경 세팅 입니다. Mac / Linux만 지원해요.

### 5. Git 설정
저희 팀에 권장하는 Git 설정을 설정하십시오.

편의를 위해 전역 설정인 `--global`을 사용하였으나 이 프로젝트에서만 설정을 하고 싶다면,
터미널로 클론받은 프로젝트 위치에 들어간 다음에 설정을 하면 됩니다.

먼저 윈도우(Windows)와 맥(Mac), 리눅스(Linux)간의 [줄 끝](https://docs.github.com/ko/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)처리를 맞춥니다.

Windows:
```shell
git config --global core.autocrlf true
```

Mac / Linux:
```shell
git config --global core.autocrlf input
```

나머지 설정은 공유하여 사용합니다.
```shell
## Fix git status broken with CJK
git config --global core.quotepath false

## Branch command sort
git config --global branch.sort -committerdate

## Push the branch to a remote with the same name
git config --global push.autosetupremote true

## Safe push (Verify last push matches server before branch update)
git config --global alias.fpush push --force-with-lease

## Always pull with rebase
git config --global pull.rebase true

## Auto stash before, pop after
git config --global rebase.autostash true

## Memorizes the conflict and the resolution
git config --global rerere.enabled true
git config --global rerere.autoUpdate true

## Better diff algorithm
## https://luppeng.wordpress.com/2020/10/10/when-to-use-each-of-the-git-diff-algorithms/
git config --global diff.algorithm histogram

## Avoid data corruption
git config --global transfer.fsckobjects true
git config --global fetch.fsckobjects true
git config --global receive.fsckObjects true
```
