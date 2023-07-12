<template>
  <main>
    <div>
      <h1>업종별 상가 지역 분포</h1>
    </div>

    <div class="button-list">
      <span style="margin-right: 10px;">업종(대분류)을 선택하세요</span><br>
        <button v-for="(name, index) in buttonNames" :key="index" @click="getGraph(name)">
          {{ name }}
        </button>
    </div>

    <div v-if="graphUrl">
      <img :src="graphUrl" />
    </div>
    <br>

  </main>
</template>
  
<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        storeName: '',
        storeInfo: [],
        buttonNames: ['음식', '숙박', '교육', '과학·기술', '소매', '시설관리·임대', '수리·개인', '부동산', '예술·스포츠', '보건의료'],
        storeType: '',
        graphUrl: null,
      };
    },
    methods: {
      getGraph(businessCategory) {
        axios({
          method: 'get',
          url: `http://localhost:5000/graph/${businessCategory}`,
          responseType: 'blob',  // add this line
        })
          .then(response => {
            // blob 형식의 응답을 URL로 변환하여 저장
            const blob = new Blob([response.data], { type: 'image/png' });
            this.graphUrl = URL.createObjectURL(blob);
          });
      
    }
  }
}
</script>
  
<style>

</style>