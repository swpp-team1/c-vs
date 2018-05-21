small_categories = ['짜장', '짬뽕', '닭가슴살', '그라탕', '치킨마요', '크랩', '불닭', '깐풍기', '비빔참치', '참치마요', '참치', '통햄', '머스타드', '오리', '불고기', '스팸김치', '스팸마요', '스팸', '딸기', '카레', '두루치기', '닭갈비', '양념치킨', '스테이크', '우삼겹', '삼겹', '꼬막', '단호박', '베이컨', '한우', '고추장', '시저', '비프', '토마토', '명란', '계란말이', '연어', '탕수육', '오므라이스', '고구마', '유부', '야끼', '장조림', '강정', '망고', '떡볶이', '찌개', '키위']
def classifyProducts(product):
    if product.find('삼각김밥') != -1 or product.find('주)') != -1 or product.find('삼각)') != -1:
        large_category = '삼각김밥'
    elif product.find('튀김') != -1:
        large_category = '튀김'
    elif product.find('김밥') != -1 or product.find('김)') != -1:
        large_category = '김밥'
    elif product.find('도시락') != -1 or product.find('도)') != -1:
        large_category = '도시락'
    elif product.find('샌드위치') != -1 or product.find('샌)') != -1:
        large_category = '샌드위치'
    elif product.find('햄버거') != -1 or product.find('햄)') != -1:
        large_category = '햄버거'
    elif product.find('샐러드') != -1:
        large_category = '샐러드'
    elif product.find('파스타') != -1 or product.find('스파게티') != -1:
        large_category = '스파게티'
    elif product.find('우동') != -1:
        large_category = '우동'
    elif product.find('핫도그') != -1:
        large_category = '핫도그'
    elif product.find('밥') != -1:
        large_category = '밥'
    elif product.find('만두') != -1:
        large_category = '만두'
    elif product.find('국수') != -1:
        large_category = '국수'
    else :
        large_category = None
    
    for category_name in small_categories:
        if product.find(category_name) != -1:
            small_category = category_name
            return {'large_category': large_category, 'small_category': small_category}
    
    if product.find('김치볶음') != -1 or product.find('김볶') != -1:
        small_category = '김볶'
    elif product.find('비빔밥') != -1 or product.find('전주') != -1:
        small_category = '비빔밥'
    elif product.find('소시지') != -1 or product.find('소세지') != -1:
        small_category = '소시지'
    elif product.find('쉬림프') != -1 or product.find('새우') != -1:
        small_category = '새우'
    elif product.find('제육') != -1 or product.find('불백') != -1:
        small_category = '제육'
    elif product.find('돈까스') != -1 or product.find('돈카츠') != -1:
        small_category = '돈까스'
    elif product.find('치킨') != -1 or product.find('닭') != -1:
        small_category = '치킨'
    elif product.find('머쉬룸') != -1 or product.find('버섯') != -1:
        small_category = '버섯'
    elif product.find('에그') != -1 or product.find('계란') != -1:
        small_category = '계란'
    elif product.find('감자') != -1 or product.find('포테이토') != -1:
        small_category = '감자'
    elif product.find('커피') != -1 or product.find('아메리카노') != -1:
        small_category = '커피'
    elif product.find('사과') != -1 or product.find('애플') != -1:
        small_category = '사과'
    elif product.find('김치') != -1:
        small_category = '김치'
    else:
        small_category = None
    return {'large_category': large_category, 'small_category': small_category}



