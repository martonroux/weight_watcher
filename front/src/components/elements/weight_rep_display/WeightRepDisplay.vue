<script setup>

import WeightRepSingleDisplay from "@/components/elements/weight_rep_display/WeightRepSingleDisplay.vue";
</script>

<template>
  <div class="weight-rep-container">
    <ol class="weight-rep-list">
      <li v-for="(rep, index) in repsList" :key="index">
        <div class="weight-rep-item" :class="{'weight-rep-item-active': index > 0}">
          <WeightRepSingleDisplay :reps-list="rep" :weight-list="weightList[index]"/>
        </div>
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  props: ['repsList', 'weightList']
}
</script>

<style scoped>

.weight-rep-container {
  overflow-x: scroll;
  white-space: nowrap;
}

.weight-rep-item {
  width: max-content;
  overflow-x: auto;
  white-space: nowrap;
}

.weight-rep-list {
  width: max-content;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  overflow-x: auto;
}

.weight-rep-item-active {
  margin-left: 20px;
}

</style>