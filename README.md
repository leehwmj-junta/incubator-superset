OS dependencies
---------------

Superset은 Superset의 메타 데이터베이스 안에 데이터베이스 커넥션 정보들을 저장한다.
그래서 superset은 연결 비밀번호를 암호화 하기위해 "cryptography"라는 Python 라이브러리를 사용한다.
불행하게도 이 라이브러리는 OS 레벨에 종속적이다.


아래에 이어질 "Superset installation and initialization"을 시도 했는데, 에러 등이 발생하면
이 단계로 돌아와서 확인 해 볼 수 있다.

데비안이나 우분투의 경우, 아래의 명령어를 실행하면 필요한 종석성들이 설치 되었는지 확인 할 수 있다.

    sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip libsasl2-dev libldap2-dev



Making own build ("Superset installation and initialization")
---------------------


빌드를 위해서 0.22 branch를 checkout하고(차후에 branch 명 변경 예정), 아래의 과정을 수행 하면 된다.

아래는 build 및 install

    # assuming $SUPERSET_HOME as the root of the repo
    cd $SUPERSET_HOME/superset/assets
    yarn
    yarn run build
    cd $SUPERSET_HOME
    python setup.py install

아래는 initialization

    # 관리자 계정 만들기
    (유저 아이디, 이름, 성, 이메일주소, 비밀번호, 비밀번호 확인 순서로 입력)
    fabmanager create-admin --app superset

    # 데이터베이스 초기화 (내장된 메타데이터베이스를 초기화 함)
    superset db upgrade

    # 예제 데이터들을 불러온다.
    superset load_examples

    # 기본 룰과 권한을 생성한다.
    superset init

    # 8088 포트에서 웹 서버를 실행한다. -p <port number> 를 붙이면 다른 포트로 사용 가능하다
    superset runserver

    # -d 스위치를 사용하면 개발자 웹 서버를 실행 할 수 있다.
    # superset runserver -d

설치가 완료 된 뒤, 브라우저에서 [http://localhost:8088](http://localhost:8088) 로 접속 하고,  
위에서 만든 관리자 계정 정보를 입력하여 로그인  
Sources -> Databases로 들어가서 list의 Database 항목에 main 이 있으면 셋팅이 성공 한 것이다.