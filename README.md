### 파이썬 기본 문법 공부

---

`git add` 코드 입력 후 다음과 같은 에러 발생

> "CRLF will be replaced by LF ..."

유닉스 OS: CRLF will be replaced by LF in…
윈도우: LF will be replaced by CRLF in…

**해결 방법**

`git config --global core.autocrlf true or false`

시스템 전체가 아닐 경우 `--global` 을 제외하여 입력한다.
