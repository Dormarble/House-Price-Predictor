
CREATE TABLE `complex` (
	`APT_CODE` varchar(10) primary key,				# 아파트 코드
    `APT_NM` varchar(20) not null,					# 아파트 명
    `CODEAPTNM` int(2) not null,					# 단지 분류
    `APTADDR` varchar(50) unique not null,			# 법정동 주소
    `DOROJUSO` varchar(50) unique not null,			# 도로명 주소
    `ADRES_CITY` int(5) not null,					# 도시
    `ADRES_GU` int(5) not null,						# 구
    `ADRES_DONG` int(5) not null,					# 동
    `ADRES_RMNDR` varchar(40),						# 나머지 주소
    `ADRES_DORO` varchar(10) not null,				# 주소(도로명)
    `ADRES_DORO_RMNDR` varchar(8) not null,			# 주소(도로 상세 주소)
    `TELNO` varchar(12) not null,					# 전화번호
    `HSHLDR_TY` int(2) not null,					# 분양형태
    `GNRL_MANAGECT_MANAGE_STLE` int(2) not null,	# 관리방식
    `CRRDPR_TY` int(2) not null,					# 복도 유형
    `HEAT_MTHD` int(2) not null,					# 난방 방식
    `ALL_DONG_CO` int(2) not null,					# 전체 동수
    `ALL_HSHLD_CO` int(4) not null,					# 전체 세대 수
    `CO_WO` varchar(20),							# 건설사(시공사)
    `CO_EX` varchar(20),							# 시행사
    `USE_INSPCT_DE` date not null,					# 사용승인일
	`TOTAR` int(10) not null,						# 연면적
    `PRIVAREA` int(10) not null,					# 주거 전용 면적
    `MANAGECT_LEVY_AR` int(10) not null,			# 관리비 부과 면적
    `KAPTMPAREA60` int(4) not null,					# 전용면적별 세대현황(~60)
    `KAPTMPAREA85` int(4) not null,					# 전용면적별 세대현황(60~85)
    `KAPTMPAREA135` int(4) not null,				# 전용면적별 세대현황(85~135)
    `KAPTMPAREA136` int(4) not null,				# 전용면적별 세대현황(135~)
    `API_UPDATE_DATE` date not null,				# 수정일자
    `EXPENSCTMANAGESTLE` int(1) not null,			# 경비비관리형태
    `HSHLD_ELCTY_CNTRCT_MTH` int(2),				# 세대전기계약방법
    `BU_AR` float not null,							# 건축면적
    `CNT_PA` int(4) not null,						# 주차대수
    `GUBUN` int(1) not null,						# 기타/의무/임대/임의
    `USE_CONFM_DE` date not null					# 단지승인일
    );
    
CREATE TABLE `address` (
	`CITY` varchar(14) not null,				# 시도
	`GU` varchar(10) not null,					# 시군구
	`ADMIN_DISTRICT_NM` varchar(40) not null,	# 행정구역명
	`ADMIN_DONG` varchar(40) not null,			# 행정동
	`CORTAR_DONG` varchar(20) not null,			# 법정동
	`ADMIN_DISTRICT_ID` int(7) not null,		# 행정구역분류
	`ADMIN_IN_CODE` int(10) not null,			# 행정기관 코드
	`CORTAR_CODE` int(10) not null,			# 법정동 코드
    `ADMIN_DONG_ENG` varchar(100)
);


