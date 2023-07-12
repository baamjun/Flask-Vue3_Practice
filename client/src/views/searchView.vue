<script>
import axios from 'axios';

export default {
  data() {
    return {
      storeName: '',  // 상점 이름을 저장할 변수를 추가합니다.
      storeInfo: [],  // 상점 정보를 저장할 변수를 추가합니다.
      isToggled: false
    };
  },
  methods: {
    toggleSwitch() {
      console.log(`Switch is now: ${this.isToggled ? 'On' : 'Off'}`);
    },
    async searchStore() {
      try {
        const searchOption = this.isToggled ? 'contains' : 'exact';  // 토글 스위치의 상태에 따른 검색 옵션을 설정합니다.
        const response = await axios.get(`http://localhost:5000/search?store_name=${this.storeName}&search_option=${searchOption}`);
        this.storeInfo = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  }
};
</script>

<template>
  <main>
    <br>
    <h1>서울시 상가 정보 검색</h1> <br>
    <h2>상호명으로 검색하기</h2>
    
    <div class="toggle-switch" style="display: flex; align-items: center;">
      <span style="margin-right: 10px;">유사한 상호명도 검색하기:</span>
      <input type="checkbox" v-model="isToggled" @change="toggleSwitch" id="switch" />
      <label for="switch" class="switch-label"></label>
      <span v-if="isToggled" style="margin-left: 10px;">ON</span>
      <span v-else style="margin-left: 10px;">OFF</span>
    </div>

    <input class="search-input" v-model="storeName" type="text" placeholder="상점 이름을 입력하세요">
    <button @click="searchStore">검색</button>
    <br>

    <div>
      <br>

      <h2>검색 결과</h2>
      <!-- 검색 결과가 있을 경우에만 테이블을 출력합니다 -->
      <table v-if="storeInfo.length" class="result-table">
        <!-- 컬럼 이름을 출력하는 헤더 -->
        <thead>
          <tr>
            <th>상호명</th>
            <th>상권업종대분류코드</th>
            <th>상권업종대분류명</th>
            <th>도로명주소</th>
            <th>지번주소</th>
            <th>경도</th>
            <th>위도</th>
          </tr>
        </thead>
        <!-- 각 상점의 정보를 출력하는 본문 -->
        <tbody>
          <tr v-for="store in storeInfo" :key="store.상호명">
            <td>{{ store.상호명 }}</td>
            <td>{{ store.상권업종대분류코드 }}</td>
            <td>{{ store.상권업종대분류명 }}</td>
            <td>{{ store.도로명주소 }}</td>
            <td>{{ store.지번주소 }}</td>
            <td>{{ store.경도 }}</td>
            <td>{{ store.위도 }}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </main>
</template>

<style scoped>
  .search-input {
      width: 80%; /* 혹은 원하는 픽셀값 */
  }

  .toggle-switch input[type="checkbox"] {
    height: 0;
    width: 0;
    visibility: hidden;
  }

  .toggle-switch label {
    cursor: pointer;
    text-indent: -9999px;
    width: 50px;
    height: 25px;
    background: grey;
    display: block;
    border-radius: 100px;
    position: relative;
  }

  .toggle-switch label:after {
    content: '';
    position: absolute;
    top: 1px;
    left: 1px;
    width: 20px;
    height: 20px;
    background: #fff;
    border-radius: 90px;
    transition: 0.3s;
  }

  .toggle-switch input:checked + label {
    background: #bada55;
  }

  .toggle-switch input:checked + label:after {
    left: calc(100% - 1px);
    transform: translateX(-100%);
  }

  .result-table td, .result-table th {
  padding: 10px;
}

</style>