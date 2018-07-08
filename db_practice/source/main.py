from exercise_1 import ex1

"""
 Created by IntelliJ IDEA.
 Project: source
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-07
 Time: 오후 11:44
"""

"""
< 파이썬 - 오라클 연동 >

- 오라클에서 자신의 환경에 맞는 instantclient 다운 ::
http://www.oracle.com/technetwork/database/database-technologies/instant-client/overview/index.html

- 아나콘다 (혹은 파이썬) cx_oracle 설치 ::
https://anaconda.org/anaconda/cx_oracle

1. instantclient 의 경로를 환경 변수에 설정.
2. IDE 에서 cx_oracle 설정
3. conn = cx_Oracle.connect("아이디", "비밀번호", "url")

"""


def main():
    print(" < Exercise 1 >")
    ex1.ex1()


if __name__ == "__main__":
    main()
