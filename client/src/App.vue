<template>
  <div id="app">
    <RouterLink to="/"><h1>Welcome to the Home Page!</h1></RouterLink>
    <br>
    <h1>상권 정보 검색 서비스</h1> <RouterLink to="/about">이용 방법</RouterLink>
    <span>출처 데이터 :&nbsp;<a href="https://www.data.go.kr/data/15083033/fileData.do" target="_blank" rel="noopener">국가중점데이터 - 상권정보 데이터</a></span>
    <br>
    <nav>
      <ul>
          <h3>
          <li><RouterLink to="/search">상호명으로 검색</RouterLink></li> <br>
          <li><RouterLink to="/graph">업종별 지역 분포</RouterLink></li> </h3> <br>
          <!-- More links... -->
      </ul>
    </nav> 
  </div>
  <RouterView />
</template>

<script set up>
import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'

export default {
  data() {
    return {
      
    };
  },
  methods: {
  },
};
</script>

<style>

</style>
