from flask import Flask, Response, jsonify, send_file
from flask_cors import CORS
from io import BytesIO
from flask import request
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('Agg')
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
plt.rcParams['font.family'] = 'Malgun Gothic'


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# API 호출 구현하기 전, 더미 데이터
df = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_서울_202303.csv")

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/pong', methods=['GET'])
def ping_pong2():
    return "ping!"

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/search', methods=['GET'])
def search_store():
    store_name = request.args.get('store_name', '')  # 상점 이름을 URL 파라미터에서 가져옵니다.
    search_option = request.args.get('search_option', 'exact')  # 검색 옵션을 URL 파라미터에서 가져옵니다.

    if store_name:  # 상점 이름이 제공되었다면, 데이터프레임에서 검색합니다.
        if search_option == 'exact':
            store_info = df[df['상호명'] == store_name][['상호명', '상권업종대분류코드', '상권업종대분류명', '도로명주소', '지번주소', '경도', '위도']].to_dict('records')
        else:  # search_option == 'contains'
            store_info = df[df['상호명'].str.contains(store_name)][['상호명', '상권업종대분류코드', '상권업종대분류명', '도로명주소', '지번주소', '경도', '위도']].to_dict('records')
    else:  # 아니면, 빈 목록을 반환합니다.
        store_info = []
    
    return jsonify(store_info)

'''
    store_name = request.args.get('store_name') # 쿼리 파라미터로 받은 상호명

    # 여기에 공공 API 호출 로직 추가
    # 예를 들어, 아래는 가짜 API URL입니다. 실제 사용할 API URL을 넣어야 합니다.
    api_url = "https://api.public-data.com/store_data"

    response = requests.get(api_url)

    # API 응답을 데이터프레임으로 변환
    #df = pd.DataFrame(response.json())
    '''

# 업종별로 시군구의 수량을 계산하는 함수
def count_business(df, business_category):
    # 선택된 업종의 데이터만 필터링
    selected_df = df[df['상권업종대분류명'] == business_category]
    
    # 시군구별로 해당 업종의 수량 계산
    counts = selected_df['시군구명'].value_counts()
    
    return counts

@app.route('/graph/<business_category>', methods=['GET'])
def get_graph(business_category):
    #business_category = '음식'  # 여기에 원하시는 업종을 입력하세요.
    counts = count_business(df, business_category)
    # 그래프 그리기
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)
    counts.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title(f'시군구별 "{business_category}" 업종 상가 수')
    ax.set_xlabel('시군구')
    ax.set_ylabel('상가 수')

    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)

    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()